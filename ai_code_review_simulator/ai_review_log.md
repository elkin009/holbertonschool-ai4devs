## AI Review Log

### Inline Comments
- (line 12) Variable `usr` should be renamed to `user` for clarity.
- (line 28) Add input validation for `status` parameter before querying.
- (line 42) Magic number `7` should be extracted to a named constant `DEFAULT_DAYS`.
- (line 55) Missing docstring for `filter_tasks()` function.
- (line 67) Use `is None` instead of `== None` for null checks.
- (line 89) Avoid mutable default argument `def filter_tasks(filters=[])`.
- (line 103) `except Exception` is too broad; catch specific exceptions.
- (line 120) Return type annotation missing on `filter_tasks()`.

### Global Feedback
- Suggest adding error handling for empty query results.
- Recommend splitting `filter_tasks()` into smaller, single-responsibility functions.
- Add pagination support for large result sets.
- Consider caching frequent filter queries for performance improvement.
