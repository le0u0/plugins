# Architecture

## Agents and skills

`manager` runs in the main thread. It assigns each job to one of five agents. Each agent holds several skills and does its job itself. Only agents carry role names; skills are named by action.

```mermaid
flowchart TD
    U([User]) <--> M[manager<br/>main thread]
    M -->|think, plan job| P[planner]
    M -->|ticket triage| H[helper]
    M -->|develop, write specs, review fix| D[developer]
    M -->|run unit tests| U[unit-tester]
    M -->|run e2e tests| E[e2e-tester]
    M -->|review job| R[reviewer]

    P --- P1[think] & P3[plan]
    H --- H1[triage-ticket]
    D --- D1[develop] & D2[write-unit] & D5[write-e2e] & D4[resolve-review]
    U --- U1[run-unit]
    E --- E2[run-e2e]
    R --- R1[review]
```

## Ticket flow

```mermaid
flowchart LR
    T[Ticket] --> TH[think<br/>questions batch]
    TH -->|answers via manager| TH
    TH -->|user says plan| PL[plan]
    PL -->|user approves plan| S[develop<br/>one step]
    S -->|user approves step| S
    S -->|last step| RV[review]
    RV -->|selected findings| RS[resolve-review]
    RS -->|re-review| RV
```

## Manager loop

```mermaid
flowchart TD
    A[Write one criterion per outcome] --> B[Assign job:<br/>paths, current step, authorization]
    B --> C[Agent report, max 8 lines]
    C --> D{Manager verifies itself:<br/>diff, hunks, artifacts, test evidence}
    D -->|gap| B
    D -->|pass or fail| F[Append to jobs.md]
    F --> G[Up to 3 lines to user,<br/>then Back to: open topic]
```

## Think relay

`planner` cannot talk to the user directly. It returns one numbered batch of at most seven questions, each with a recommended answer. The manager shows the batch unchanged and sends the answers back to the same planner. Each round costs a little manager context; the planner's own context stays cached. Fewer rounds cost fewer tokens, so answer by number.

## Why this structure

- **Fewer agents, fewer re-reads.** Each new agent re-reads rules, plan, and diff. Earlier, one plan step started about four agents: developer, spec writer, and two runners. Now one `developer` writes the specs and code for a step, and `unit-tester` and `e2e-tester` do the runs.
- **One developer per tier per ticket.** A plan step goes to the ticket's existing `developer` of the step's tier (standard by default, advanced for a complicated step), so a 12-step ticket starts at most two developers, not twelve. `checklist.md` carries progress between steps. Trade-off: a developer's context grows over the ticket. Within a ticket, agents stay alive and get later work by SendMessage to the same ID, so a re-test or re-review does not re-read the rules, plan, and diff. Finished agents cost nothing while idle. The manager records each ID in `jobs.md`; if an agent is gone, it starts a fresh one that reads the plan, `checklist.md`, and `jobs.md`.
- **Reviewer reuse.** The same `reviewer` re-reviews the ticket and updates `review.md` in place. Trade-off: a re-review carries its earlier findings, so it is less independent than a fresh read.
- **Manager verifies, not trusts.** An agent's "done" is a claim. The manager checks the diff, artifacts, and test result itself before reporting.
- **Short reports.** Agents report in at most eight lines; the manager announces a job in one line and reports it in at most three. Detail lives in `jobs.md` in the task folder.
- **Model by agent and tier.** Skills are grouped by weight into light, standard and advanced. The manager passes `model` and `effort` on every start and may start a developer or reviewer at another tier for a complicated or simple job. See [models](models.md).
- **Claude Code first.** Agents and hooks work only in Claude Code. Skills stay plain `SKILL.md` files, so other hosts run them directly on the chat's own model, with no subagents.
