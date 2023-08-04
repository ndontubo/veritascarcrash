
import pandas as pd

data_new = pd.read_csv('Crash_Table.csv')
data_new['corn'] = new_col
data_new.to_csv('Crash_Table.csv')
