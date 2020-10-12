def has_negatives(a):
    """
    YOUR CODE HERE
    """
    store = {}
    result = []

    for num in a:
        if num:
            store[num] = 1
            if -num in store:
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
