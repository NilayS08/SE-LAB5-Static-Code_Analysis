**Question 1**
- Easiest: removing the unused import and adding missing blank lines; they were purely stylistic and risk-free.
- Hardest: replacing bare except with specific exceptions and removing eval; both required reasoning about failure modes and security impact.

**Question 2**
- Style-related renames to snake_case can be noisy if functions are part of a public API, even if they improve consistency.
- Global usage warnings can be acceptable in a small, single-file script, though they signal maintainability risks.

**Question 3**
- Add pre-commit hooks to run linters and security checks locally before commits.
- Gate CI with separate jobs for style, lint, and security; fail on high-severity issues and track trends for the rest.

**Question 4**
- Clearer, more consistent code via snake_case, docstrings, and f-strings.
- Better robustness and security by targeted exception handling and removing eval.