#%%
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# %%
train=pd.read_csv('house_train.csv')
test=pd.read_csv('house_test.csv')
sub=pd.read_csv('sample_submission.csv')
# %%