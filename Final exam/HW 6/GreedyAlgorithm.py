def greedy_search(items, limit):
    items.sort(reverse=True)
    total = 0
    result = []
    for item in items:
        if total + item <= limit:
            total += item
            result.append(item)
    return result

print(f"Greedy Result: {greedy_search([1, 5, 2, 10, 7], 15)}")
