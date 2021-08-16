#Year with the highest average fuel cost per unit delivered
import pandas as pd 
Fuel_data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv',error_bad_lines=False)

Fuel_data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()

#standard deviation and 75th percentile of measure of energy per unit (Fuel_mmbtu_per_unit) in two decimal places? 
import pandas as pd 
Fuel_data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv',error_bad_lines=False) Fuel_data.describe(include='all')

#fuel type code with lowest fuel cost per unit burned 
Fuel_data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean()

#feature with missing values 
Fuel_data.isnull().sum()

#percentage change in fuel per unit burned in 1998 compared to 1994 
Fuel_data.groupby(['report_year','fuel_type_code_pudl'])['fuel_cost_per_unit_burned'].sum()

#skewness and kurtosis of fuel qyantity burned
import pandas as py
Fuel_data.skew(axis=0, skipna= True)

#kurtosis of fuel_qty_burned
Fuel_data.kurt(axis=0, skipna= True)

#feature with second and third lowest correlation with fuel cost per unit price
Fuel_data.corr(method= 'pearson')
