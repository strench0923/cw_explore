- Fixed a bug in `calc.py`'s `clamp()` function: when `value > high`, it now correctly returns `high` instead of incorrectly returning `low`.

Risks:
- No tests appear to cover `clamp()`'s upper-bound behavior — worth adding a test to prevent regression.
