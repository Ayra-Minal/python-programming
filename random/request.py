def order_requests(requests, k):
    seen = []
    for item in reversed(requests):
        if item not in seen:
            seen.append(item)
            if len(seen) == k:
                break
    return seen

requests = ["item1","item2","item3","item1","item3","item4","item3"]
k = 3
ans = order_requests(requests, k)
print(ans)
