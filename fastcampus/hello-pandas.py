import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins').dropna()
print(type(penguins))

penguins.info()

penguins
a = 'test'