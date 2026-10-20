# Code Smells

Signs the changed code may be badly structured. Judgement calls, never hard violations: write "possible <smell>". The project's own rules override them. Skip what tooling enforces, and anything outside the changed lines.

- **Mysterious name:** a name that doesn't say what the thing does or holds.
- **Duplicated code:** the same logic in more than one place in the change.
- **Feature envy:** a method that uses another object's data more than its own.
- **Data clumps:** the same few fields or parameters always travel together.
- **Primitive obsession:** a string or number standing in for a real concept.
- **Repeated switches:** the same `switch` or `if` chain on one type, in several places.
- **Shotgun surgery:** one small change forces edits in many files.
- **Divergent change:** one file edited for several unrelated reasons.
- **Speculative generality:** options or abstractions for needs nobody has.
- **Message chains:** long `a.b().c().d()` walks the caller shouldn't know about.
- **Middle man:** a class or function that only passes calls on.
- **Refused bequest:** a subclass that ignores or overrides most of what it inherits.
