def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    store = {}
    # result = []

    for arr in arrays:
        for num in arr:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
    result = [num[0] for num in store.items() if num[1] == len(arrays)]
    # for each in store:
    #     if store[each] == len(arrays):
    #         result.append(store[each])
    #         print(result)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
