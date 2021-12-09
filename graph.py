import pandas as pd
import plotly.express as px

readFile=pd.read_csv("data.csv")
fig = px.scatter(readFile, x="date", y="cases",color="country")
fig.show()