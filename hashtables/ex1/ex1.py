def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    store = {}

    for i in range(length):

        weight = weights[i]
        x = limit - weight

        if x not in store:
            store[weight] = i
        elif x in store:
            if i > store[x]:
                return (i, store[x])
            else:
                return (store[x], i)

    return None
