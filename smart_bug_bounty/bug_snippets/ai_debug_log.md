# AI Debug Log

**Project:** Smart Bug Bounty
**Directory:** `smart_bug_bounty/bug_snippets/`
**AI Tool Used:** Claude (Anthropic)
**Date:** 2026-05-13

---

## bug1.py

**AI Explanation:**
The `get_top_students()` function sorts students in ascending order by score using `sorted(..., key=lambda x: x['score'])`, but then returns the first `n` elements with `sorted_students[:n]`. Since the list is sorted from lowest to highest, this returns the bottom students, not the top ones. The fix is to sort in descending order by adding `reverse=True`.

**Suggested Fix:** Add `reverse=True` to the `sorted()` call:
```python
