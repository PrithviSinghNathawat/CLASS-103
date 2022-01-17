import pandas as pd
import plotly.express as pe
df=pd.read_csv('line_chart.csv')
figure=pe.scatter(df,x='Country',y='Per capita income')
figure.show()