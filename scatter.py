import pandas as pd
import plotly.express as pe
df=pd.read_csv('data.csv')
figure=pe.scatter(df,x='Country',y='Per capita')
figure.show()