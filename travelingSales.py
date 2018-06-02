from ticketMap import cities
import copy
from operator import attrgetter

def distance(firstCity, secondCity):
    'Return the distance between two cities'
    return cities[firstCity][secondCity][0]

def routeLength(route):
    'Return the length of a route'
    return sum([distance(route[i], route[i+1]) for i in range(len(route)-1)])

def testRouteLength():
    route = ['Calgary', 'Winnipeg', 'Duluth', 'Chicago', 'Pittsburgh']
    assert routeLength(route) == 16
    print("Test of route length passed!")

citiesVisted = {}

def aPossibleRoute(firstCity, secondCity):
    '''Find a possible route from one city to another. This is a depth first
       search.'''
    if secondCity in cities[firstCity]:
        return [firstCity, secondCity]
    else:
        for city in cities[firstCity]:
            return [firstCity] + aPossibleRoute(city, secondCity)

def anotherPossibleRoute(firstCity, secondCity):
    'Find all possible routes between two cities.'
    allRoutes = []
    singleRoute = [firstCity]
    for city1 in cities[firstCity]:
        singleRoute.append(city1)
        for city2 in cities[city1]:
            if city2 == secondCity:
                tmpRoute = copy.copy(singleRoute)
                singleRoute.append(city2)
                allRoutes.append(singleRoute)
                singleRoute = copy.copy(tmpRoute)
        singleRoute = [firstCity]
    return allRoutes

def minDistances(city):
    """Dijkstra's shortest path algorithm. Order of route is a sort from
       smallest distance to largest."""
    sptSet = set()
    verticies = {aCity: 100 for aCity in cities}
    verticies[city] = 0
    verticiesSet = {vertex for vertex in verticies}
    def vertDist(vertex): return verticies[vertex]
    pred = {}
    while not all([vertex in sptSet for vertex in verticies]):
        u = min(verticiesSet-sptSet, key=vertDist)
        sptSet.add(u)
        for aCity in cities[u]:
            #if aCity not in sptSet:
            newDistance = verticies[u] + distance(u, aCity)
            if newDistance < verticies[aCity]:    
                verticies[aCity] = newDistance
                pred[aCity] = u
    return verticies, pred

def tracePreds(pred, endCity, startCity):
    if pred[endCity] == startCity:
        return [endCity, startCity]
    else:
        return [endCity]+ tracePreds(pred, pred[endCity], startCity)

def minDistance(city1, city2):
    "The minimum distance between two cities."
    verticies, pred = minDistances(city1)
    return verticies[city2], tracePreds(pred, city2, city1)

def printMinDistance(city1, city2):
    minDist, route = minDistance(city1, city2)
    print("Minimum distance between {} and {} is {}".format(city1, city2, minDist))
    print("Route is {}".format(" -> ".join(route)))

if __name__ == "__main__":
    testRouteLength()
    route = ['Calgary', 'Winnipeg', 'Duluth', 'Chicago', 'Pittsburgh']
    print("Route length: {}".format(routeLength(route)))
    city1 = 'New York'
    city2 = 'Los Angeles'
    printMinDistance(city1, city2)
    printMinDistance('New York', 'Washington')
    printMinDistance('Miami', 'Vancouver')
    printMinDistance('Seattle', 'New York')
    printMinDistance('Boston', 'Miami')
    printMinDistance('Vancouver', 'Montreal')
    printMinDistance('New York', 'Los Angeles')
