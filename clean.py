import sys
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

contact_info_file = sys.argv[1]
other_info_file = sys.argv[2]
output_file = sys.argv[3]


contact_data = pd.read_csv(contact_info_file)
other_data = pd.read_csv(other_info_file)

output = pd.merge(contact_data, other_data, left_on='respondent_id', right_on='id')
output = output.drop(columns='id')
output = output.dropna(how='any')

output = output[~output['job'].str.contains('insurance') == True]
output = output[~output['job'].str.contains('Insurance') == True]
output.to_csv(output_file, index=False)

print(output.info())
