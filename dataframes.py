dict = {"country": ["brazil","russia","indonesia","china","india","south africa"],
        "capital": ["brasilia","moscow","jakarta","beijing","new delhi","pretoria"],
        "area": [8.516, 23.668, 30.2019, 221.2000, 32.9872, 76.9008],
        "populations": [300, 5090, 98723, 92384, 123745, 89732]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)