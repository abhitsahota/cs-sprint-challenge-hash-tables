#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    plans = {}

    route = [None] * length

    for tick in tickets:
        plans[tick.source] = tick.destination

    starting_flight = plans['NONE']

    for flight in range(length):
        route[flight] = starting_flight
        starting_flight = plans[starting_flight]

    return route
