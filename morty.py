#Library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from benfordslaw import benfordslaw

#Initialize
bl = benfordslaw(alpha=0.5)

#dataset 
df = pd.read_csv('caso_full.csv', sep=',')

