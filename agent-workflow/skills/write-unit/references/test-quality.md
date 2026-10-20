# Test Quality

The project's own test rules win where they conflict.

- **Behavior, not internals.** Test through the public interface, at the seam the plan step names. A refactor that keeps behavior must not break the test.
- **No implementation coupling.** Don't mock the code's own modules, call private methods, or check through a side channel such as a database query.
- **No tautologies.** Take the expected value from a literal or worked example, never from the code's own formula.
- **Mock boundaries only:** external APIs, time, randomness, and sometimes the database or file system. Inject them.
- **One slice at a time.** Never write many specs before any code.
