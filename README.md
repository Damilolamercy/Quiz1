# Quiz1

#standard deviation and 75th percentile of measure of energy per unit (Fuel_mmbtu_per_unit) in two decimal places?
import pandas as pd
Fuel_data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv',error_bad_lines=False)
Fuel_data.describe(include='all')
