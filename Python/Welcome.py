import pandas

coronavirusdata=pandas.read_csv("/Users/shivtejpatil/Downloads/COVID-19 Cases.csv")
pandas.set_option('display.max_columns',None)
pandas.set_option('display.max_rows',None)
print(coronavirusdata.groupby(['Country_Region','Date','Case_Type'])['Cases'].sum())
fsf


