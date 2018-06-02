from routes import routes, mean
from travelingSales import minDistance, distance
from ticketMap import cities
from fractions import Fraction
import itertools

# Credit for the code below goes to Peter Norvig
def P(event, space): 
    "The probability of an event, given a sample space."
    return Fraction(cases(favorable(event, space)), 
                    cases(space))

favorable = set.intersection # Outcomes that are in the event and in the sample space
cases     = len              # The number of cases is the length, or size, of a set

def combos(items, n):
    "All combinations of n items; each combo as a space-separated str."
    return set(map(' '.join, itertools.combinations(items, n)))
# End Norvig code

def dec(event, space):
    "The probability of an event, given a sample space."
    return float(cases(favorable(event, space))/cases(space))

# P = Pink, W = White, B = Blue, Y = Yellow, O = Orange, BK = Black, R = Red
# G = Green, A = Locomotive (used as any color, there are 14 of these)
trainTypes = ['P', 'W', 'B', 'Y', 'O', 'BK', 'R', 'G', 'A']
trainDeck = {'{}{}'.format(c, x) for x in range(12) for c in trainTypes}
trainDeck.add('A12')
trainDeck.add('A13')

def probNumOfColor(color, n):
    """Return the probability of getting the number n of a color of train,
       including locomotives."""
    hands = combos(list(trainDeck), n)
    event = set()
    for hand in hands:
        colors = [card[0] for card in hand]
        numColor = colors.count(color)
        numLocs = colors.count('A')
        if numColor+numLocs >= n:
            event.add(hand)
    return float(P(event, hands))

numTrainsScore = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}

def routeScore(routeList):
    'Return the score of a route for just placing the trains.'
    distances = [distance(routeList[i], routeList[i+1]) for i in range(len(routeList)-1)]
    return sum([numTrainsScore[x] for x in distances])

def minRouteScore(route):
    '''Return the score of the trains on the min route plus the score for
       completing the route.'''
    _, routeList = minDistance(route[0], route[1])
    return routeScore(routeList) + routes[route]

def printMinRouteScores():
    #print("Route" + " "*27 + "Route Score Total Score Num. Trains")
    print("{:^33} {} | {} | {:^6} | {:^9}".format("", "Bonus", "Total", "Num.", "Score"))
    print("{:^33} {} | {} | {} | {}".format("Route", "Score", "Score", "Trains", "Per Train"))
    minScores = [minRouteScore(route) for route in routes]
    zipped = zip(routes, minScores)
    for route, score in sorted(zipped, key=lambda x: x[1], reverse=True):
        numTrains, _ = minDistance(route[0], route[1])
        print("{0[0]:<15} to {0[1]:<14}  {1:4d} |  {2:4d} |  {3:5d} |  {4: >8.2f}".format(route,
                                                                              routes[route],
                                                                              score,
                                                                              numTrains, score/float(numTrains)))

def getMeanMinScore():
    return mean([minRouteScore(route) for route in routes])

if __name__ == "__main__":
    #_, route = minDistance('Seattle', 'New York')
    #print("Score from Seattle to New York at min distance: {}".format(routeScore(route)))
    printMinRouteScores()
    print("Average min total score for routes: {:.2f}".format(getMeanMinScore()))
    #print("Probability of getting 5 Blue is {}".format(probNumOfColor('B', 5)))
    print("Probability of getting 4 Blue or locomotive is {:.3f}".format(probNumOfColor('B', 4)))
    print("Probability of getting 3 Blue or locomotive is {:.3f}".format(probNumOfColor('B', 3)))
    print("Probability of getting 2 Blue or locomotive is {:.3f}".format(probNumOfColor('B', 2)))
    print("Probability of getting 1 Blue or locomotive is {:.3f}".format(probNumOfColor('B', 1)))
    print("Probability of getting 1 Locomotive is {:.3f}".format(float(14)/110))
    """print(routeScore(['Montreal', 'Sault St. Marie', 'Duluth', 'Winnipeg', 'Calgary', 'Vancouver']))
    print(routeScore(['Los Angeles', 'El Paso', 'Oklahoma City', 'Kansas City', 'Saint Louis', 'Pittsburgh', 'New York']))
    print(routeScore(['Los Angeles', 'Phoenix', 'Santa Fe', 'Oklahoma City', 'Little Rock', 'Nashville', 'Pittsburgh', 'New York']))"""
