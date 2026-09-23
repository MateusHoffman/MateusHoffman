"""Smoke test file for the OpenClaw pr-reviewer pipeline.

Contains three deliberate issues, one per specialist lane, so the review
can be checked for real findings instead of a rubber-stamp approval.
"""

API_KEY = "sk-live-abc123def456ghi789"  # security: hardcoded credential


def get_all_user_orders(user_ids, db):
    # performance: N+1 query inside a loop instead of a single batched query
    results = []
    for uid in user_ids:
        order = db.query(f"SELECT * FROM orders WHERE user_id = {uid}")
        results.append(order)
    return results


def last_n_items(items, n):
    # quality: off-by-one, drops the last element instead of keeping last n
    return items[len(items) - n - 1:-1]
