#Importing the necessary packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

players = pd.read_csv('/players_20.csv')

print(" Dataset Length :: ", len(players))
print(" Dataset Shape :: ", players.shape)