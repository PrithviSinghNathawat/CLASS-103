import pandas as pa
import plotly.express as pe
dataFrame=pa.read_csv('data.csv')
figure=pe.bar(dataFrame,x='Country',y='Population')
figure.show()