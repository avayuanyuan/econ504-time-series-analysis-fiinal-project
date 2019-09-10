import statsmodels.api as sm
import pandas as pd
X = get_pricing('STX', fields=['price']
                               , start_date='2014-01-01', end_date='2015-01-01')
Y=get_pricing('WDC', fields=['price']
                               , start_date='2014-01-01', end_date='2015-01-01')['price']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print model.params[1]
