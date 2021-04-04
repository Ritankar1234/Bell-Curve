import random
diceResult=[]
count=[]
for i in range(0, 100):
  dice1=random.randint(1, 6)
  dice2=random.randint(1, 6)
  diceResult.append(dice1+dice2)
  count.append(i)
import plotly.express as px
#fig=px.bar(x=diceResult, y=count)
#fig.show()
import plotly.figure_factory as ff 
fig=ff.create_distplot([diceResult],["result"], show_hist=False)
fig.show()

