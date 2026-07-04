This is a one-line bug fix in `clamp()` in `calc.py`.

**Before:** when `value > high`, the function incorrectly returned `low`.
**After:** it now correctly returns `high`.

The `clamp(value, low, high)` function is supposed to cap a value within `[low, high]`. The old code had a copy-paste bug — both the "too low" and "too high" branches returned `low`, meaning any value above the upper bound got clamped down to the lower bound instead of the upper bound. Now the upper-bound branch correctly returns `high`, so `clamp()` behaves as expected in both directions.

No other files were changed.
