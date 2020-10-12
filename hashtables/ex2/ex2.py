#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    store = {}
    route = []

    for ticket in tickets:
        store[ticket.source] = ticket.destination
    for i in range(length):
        if len(route) == 0:
            route.append(store['NONE'])
        else:
            route.append(store[route[i-1]])




    return route
