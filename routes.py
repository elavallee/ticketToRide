from collections import Counter

routes = {('Seattle', 'New York'):              22,
          ('Sault St. Marie', 'Nashville'):      8,
          ('Los Angeles', 'New York'):          21,
          ('San Francisco', 'Atlanta'):         17,
          ('Sault St. Marie', 'Oklahoma City'):  9,
          ('Duluth', 'Houston'):                 8,
          ('New York', 'Atlanta'):               6,
          ('Boston', 'Miami'):                  12,
          ('Helena', 'Los Angeles'):             8,
          ('Los Angeles', 'Chicago'):           16,
          ('Portland', 'Nashville'):            17,
          ('Montreal', 'Atlanta'):               9,
          ('Denver', 'El Paso'):                 4,
          ('Portland', 'Phoenix'):              11,
          ('Vancouver', 'Montreal'):            20,
          ('Montreal', 'New Orleans'):          13,
          ('Chicago', 'Santa Fe'):               9,
          ('Seattle', 'Los Angeles'):            9,
          ('Calgary', 'Phoenix'):               13,
          ('Dallas', 'New York'):               11,
          ('Winnipeg', 'Houston'):              12,
          ('Toronto', 'Miami'):                 10,
          ('Kansas City', 'Houston'):            5,
          ('Duluth', 'El Paso'):                10,
          ('Winnipeg', 'Little Rock'):          11,
          ('Calgary', 'Salt Lake City'):         7,
          ('Vancouver', 'Santa Fe'):            13,
          ('Los Angeles', 'Miami'):             20,
          ('Chicago', 'New Orleans'):            7,
          ('Denver', 'Pittsburgh'):             11}

def mean(aList):
    "Calculate the average of numbers in a list."
    return sum(aList)/float(len(aList))

if __name__ == "__main__":
    print("Average points of all routes: {}".format(mean(routes.values())))
    print("Most frequent point value: {}".format(Counter(routes.values()).most_common()))
