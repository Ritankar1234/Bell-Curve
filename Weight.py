import plotly.figure_factory as ff
import pandas as pd
import csv
df=pd.read_csv("Weight.csv")
weightList=df[("Weight(Pounds)")].tolist()
fig=ff.create_distplot([weightList], ["Weight"], show_hist=False)
fig.show()