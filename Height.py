import plotly.figure_factory as ff
import pandas as pd 
import csv
df=pd.read_csv("Weight.csv")
heightList=df["Height(Inches)"].tolist()
fig=ff.create_distplot([heightList], ["Height"], show_hist=False)
fig.show()

