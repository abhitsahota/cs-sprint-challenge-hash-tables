def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    if length <= 1: 
        return None

    for i in range(length):
        curr = weights[i]

        if curr in cache:

            prev = cache[curr]
            return(i, prev)

        cache[limit - curr] = i

    return None
