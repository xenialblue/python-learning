dict = {"country": ["brazil","russia","indonesia","china","india","south africa"],
        "capital": ["brasilia","moscow","jakarta","beijing","new delhi","pretoria"],
        "area": [8.516, 23.668, 30.2019, 221.2000, 32.9872, 76.9008],
        "populations": [300, 5090, 98723, 92384, 123745, 89732],
        "region": ["south america", "eastern europe", "southeast asia", "central asia", "west asia", "south africa"]}

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "ID", "CH", "ID", "SA"]
cars = pd.read_csv('cars.csv')
print(brics)
print(cars)