#Concrete Strength
import pandas as pd
import plotly.graph_objects as go
from plotly import subplots
import plotly.express as px

# Read the happiness data into pandas dataframe
pd.options.display.max_columns = 999

data = pd.read_excel('Concrete_Data.xls')
data = pd.DataFrame(data)

print(data.head())

#Check if there is any missing value
print("# of NaN values for the data:\n", data.isna().sum())

fig = subplots.make_subplots(rows=3, cols=3)

i = 1
j = 1

for col in range(len(data.columns)-1):
    fig.add_trace(go.Box(name=data.columns[col], y=data[data.columns[col]]), row=i, col=j)
    if j == 3:
        i += 1
        j = 0
    j += 1

fig.update_layout(title_text='Concrete Data Outliers')

fig.show()

print(data.columns)
