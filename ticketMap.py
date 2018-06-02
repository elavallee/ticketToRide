# cities is a lookup by city name, a tuple is returned where
# element 0 is the number of trains or distance and element 1
# is the color: A = Any color, W = White, B = Blue, BK = Black
# O = Orange, G = Green, Y = Yellow, P = Pink, R = Red
cities = {'Vancouver': {'Calgary': (3, 'A'), 'Seattle': (1, ('A', 'A'))},
          'Calgary': {'Vancouver': (3, 'A'), 'Seattle': (4, 'A'), 'Helena': (4, 'A'), 'Winnipeg': (6, 'W')},
          'Winnipeg': {'Calgary': (6, 'W'), 'Helena': (4, 'B'), 'Duluth': (4, 'BK'), 'Sault St. Marie': (6, 'A')},
          'Sault St. Marie': {'Winnipeg': (6, 'A'), 'Duluth': (3, 'A'), 'Toronto': (2, 'A'), 'Montreal': (5, 'BK')},
          'Montreal': {'Sault St. Marie': (5, 'BK'), 'Toronto': (3, 'A'), 'New York': (3, 'B'), 'Boston': (2, ('A', 'A'))},
          'Boston': {'Montreal': (2, ('A', 'A')), 'New York': (2, ('Y', 'R'))},
          'New York': {'Boston': (2, ('Y', 'R')), 'Montreal': (3, 'B'), 'Pittsburgh': (2, ('W', 'G')), 'Washington': (2, ('O', 'BK'))},
          'Washington': {'New York': (2, ('O', 'BK')), 'Pittsburgh': (2, 'A'), 'Raleigh': (2, ('A', 'A'))},
          'Raleigh': {'Washington': (2, ('A', 'A')), 'Pittsburgh': (2, 'A'), 'Nashville': (3, 'BK'), 'Atlanta': (2, ('A', 'A')), 'Charleston': (2, 'A')},
          'Charleston': {'Raleigh': (2, 'A'), 'Atlanta': (2, 'A'), 'Miami': (4, 'P')},
          'Miami': {'Charleston': (4, 'P'), 'Atlanta': (5, 'B'), 'New Orleans': (6, 'R')},
          'New Orleans': {'Miami': (6, 'R'), 'Atlanta': (4, ('Y', 'O')), 'Little Rock': (3, 'G'), 'Houston': (2, 'A')},
          'Houston': {'New Orleans': (2, 'A'), 'Dallas': (1, ('A', 'A')), 'El Paso': (6, 'G')},
          'El Paso': {'Houston': (6, 'G'), 'Dallas': (4, 'R'), 'Oklahoma City': (5, 'Y'), 'Santa Fe': (2, 'A'), 'Phoenix': (3, 'A'), 'Los Angeles': (6, 'BK')},
          'Los Angeles': {'El Paso': (6, 'BK'), 'Phoenix': (3, 'A'), 'Las Vegas': (2, 'A'), 'San Francisco': (3, ('Y', 'P'))},
          'San Francisco': {'Los Angeles': (3, ('Y', 'P')), 'Salt Lake City': (5, ('O', 'W')), 'Portland': (5, ('G', 'P'))},
          'Portland': {'San Francisco': (5, ('G', 'P')), 'Salt Lake City': (6, 'B'), 'Seattle': (1, ('A', 'A'))},
          'Seattle': {'Portland': (1, ('A', 'A')), 'Vancouver': (1, ('A', 'A')), 'Calgary': (4, 'A'), 'Helena': (6, 'Y')},
          'Helena': {'Seattle': (6, 'Y'), 'Calgary': (4, 'A'), 'Winnipeg': (4, 'B'), 'Duluth': (6, 'O'), 'Omaha': (5, 'R'), 'Denver': (4, 'G'), 'Salt Lake City': (3, 'P')},
          'Duluth': {'Helena': (6, 'O'), 'Winnipeg': (4, 'BK'), 'Sault St. Marie': (3, 'A'), 'Toronto': (6, 'P'), 'Chicago': (3, 'R'), 'Omaha': (2, ('A', 'A'))},
          'Toronto': {'Duluth': (6, 'P'), 'Sault St. Marie': (2, 'A'), 'Montreal': (3, 'A'), 'Pittsburgh': (2, 'A'), 'Chicago': (4, 'W')},
          'Pittsburgh': {'Chicago': (3, ('O', 'BK')), 'Toronto': (2, 'A'), 'New York': (2, ('W', 'G')), 'Washington': (2, 'A'), 'Raleigh': (2, 'A'), 'Nashville': (4, 'Y'), 'Saint Louis': (5, 'G')},
          'Chicago': {'Omaha': (4, 'B'), 'Duluth': (3, 'R'), 'Toronto': (4, 'W'), 'Pittsburgh': (3, ('O', 'BK')), 'Saint Louis': (2, ('G', 'W'))},
          'Omaha': {'Denver': (4, 'P'), 'Helena': (5, 'R'), 'Duluth': (2, ('A', 'A')), 'Chicago': (4, 'B'), 'Kansas City': (1, ('A', 'A'))},
          'Denver': {'Phoenix': (5, 'W'), 'Salt Lake City': (3, ('R', 'Y')), 'Helena': (4, 'G'), 'Omaha': (4, 'P'), 'Kansas City': (4, ('BK', 'O')), 'Oklahoma City': (4, 'R'), 'Santa Fe': (2, 'A')},
          'Salt Lake City': {'San Francisco': (5, ('O', 'W')), 'Portland': (6, 'B'), 'Helena': (3, 'P'), 'Denver': (3, ('R', 'Y')), 'Las Vegas': (3, 'O')},
          'Las Vegas': {'Los Angeles': (2, 'A'), 'Salt Lake City': (3, 'O')},
          'Phoenix': {'Los Angeles': (3, 'A'), 'Denver': (5, 'W'), 'Santa Fe': (3, 'A'), 'El Paso': (3, 'A')},
          'Santa Fe': {'Phoenix': (3, 'A'), 'Denver': (2, 'A'), 'Oklahoma City': (3, 'B'), 'El Paso': (2, 'A')},
          'Oklahoma City': {'Santa Fe': (3, 'B'), 'Denver': (4, 'R'), 'Kansas City': (2, ('A', 'A')), 'Little Rock': (2, 'A'), 'Dallas': (2, ('A', 'A')), 'El Paso': (5, 'Y')},
          'Dallas': {'El Paso': (4, 'R'), 'Oklahoma City': (2, ('A', 'A')), 'Little Rock': (2, 'A'), 'Houston': (1, ('A', 'A'))},
          'Little Rock': {'Dallas': (2, 'A'), 'Oklahoma City': (2, 'A'), 'Saint Louis': (2, 'A'), 'Nashville': (3, 'W'), 'New Orleans': (3, 'G')},
          'Kansas City': {'Denver': (4, ('BK', 'O')), 'Omaha': (1, ('A', 'A')), 'Saint Louis': (2, ('B', 'P')), 'Oklahoma City': (2, ('A', 'A'))},
          'Saint Louis': {'Kansas City': (2, ('B', 'P')), 'Chicago': (2, ('G', 'W')), 'Pittsburgh': (5, 'G'), 'Nashville': (2, 'A'), 'Little Rock': (2, 'A')},
          'Nashville': {'Saint Louis': (2, 'A'), 'Pittsburgh': (4, 'Y'), 'Raleigh': (3, 'BK'), 'Atlanta': (1, 'A'), 'Little Rock': (3, 'W')},
          'Atlanta': {'Nashville': (1, 'A'), 'Raleigh': (2, ('A', 'A')), 'Charleston': (2, 'A'), 'Miami': (5, 'B'), 'New Orleans': (4, ('Y', 'O'))}}

def testCities():
    """A check that the cities were input correctly"""
    for firstCity in cities:
        for secondCity in cities[firstCity]:
            # check distance
            if cities[firstCity][secondCity][0] != cities[secondCity][firstCity][0]:
                print("Distances don't match for {} and {}".format(firstCity, secondCity))
            # check color
            color1 = cities[firstCity][secondCity][1]
            color2 = cities[secondCity][firstCity][1]
            if color1 != color2:
                print("Colors don't match for {} and {}".format(firstCity, secondCity))
    print('Done with city check')

if __name__ == "__main__":
    testCities()
