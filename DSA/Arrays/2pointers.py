arr = [1, 2, 3, 4, 5]
target = 6

# Find pairs with sum = target
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Pair: ({arr[i]}, {arr[j]})")
