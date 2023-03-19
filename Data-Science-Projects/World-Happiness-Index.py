# World Happiness Index

import pandas as pd
import plotly.graph_objects as go
from plotly import subplots
import matplotlib.pyplot as mp
import plotly.express as px
import seaborn as sb
import numpy as np

##### Data Exploration Step

# Read the happiness data into pandas dataframe

pd.options.display .max_columns = 999
pd.options.display .max_rows = 999

data_2015 = pd.read_csv('2015.csv')
data_2016 = pd.read_csv('2016.csv')
data_2017 = pd.read_csv('2017.csv')
data_2018 = pd.read_csv('2018.csv')
data_2019 = pd.read_csv('2019.csv')

#Check the columns if they match up with each other
column_names_15 = list(data_2015.columns)
column_names_16 = list(data_2016.columns)
column_names_17 = list(data_2017.columns)
column_names_18 = list(data_2018.columns)
column_names_19 = list(data_2019.columns)

print(column_names_15)
print(column_names_16)
print(column_names_17)
print(column_names_18)
print(column_names_19)

'''
We see that the data from different years differ from each other in aspect of columns names and order. We will deal with
this in the next step -Data Cleaning 
'''

#Check if there is any missing value

print("# of NaN values for the 2015 data:\n", data_2015.isna().sum())
print("# of NaN values for the 2016 data:\n", data_2016.isna().sum())
print("# of NaN values for the 2017 data:\n", data_2017.isna().sum())
print("# of NaN values for the 2018 data:\n", data_2018.isna().sum())
print("# of NaN values for the 2019 data:\n", data_2019.isna().sum())

'''
We see that the data from year 2018 has 1 missing value in 'Perceptions of Corruption' column. We will deal with this in
the next step either.
'''

#Check if there is any outliers

'''
To detect outliers, we will use plotly
'''

#Check if there is any outliers
fig_2015 = subplots.make_subplots(rows = 3 , cols = 3)

i=1
j=1

for feature in range(3,len(column_names_15)):
    fig_2015.add_trace(go.Box(name=column_names_15[feature],y=data_2015[column_names_15[feature]]), row=i, col=j)
    if j == 3:
        i += 1
        j = 0
    j += 1

fig_2015.update_layout(title_text="2015 Data Outliers")

fig_2015.show()

'''
We see that there are some outliers in: standard error, family, trust, generosity and dystopia residual. However, only
the value '0' in the 'Family' column seems like a data error.

We will check which country is this 'family outlier'
'''

#Check who the outlier is
for val in range(len(data_2015['Family'])):
    if data_2015['Family'][val] == 0:
        id = val

print('Outlier country is: ',data_2015['Country'][val])

'''
We see that Togo has the value of '0' for 'Family' column. It may not be a data entry error, so we will keep an eye on it.
'''

#####
'''
We do the same process for other given years
'''
#Check if there is any outliers
fig_2016 = subplots.make_subplots(rows = 3 , cols = 4)

i=1
j=1

for feature in range(3,len(column_names_16)):
    fig_2016.add_trace(go.Box(name=column_names_16[feature],y=data_2016[column_names_16[feature]]), row=i, col=j)
    if j == 4:
        i += 1
        j = 0
    j += 1

fig_2016.update_layout(title_text="2016 Data Outliers")

fig_2016.show()

'''
We see that there are some outliers in: family, trust, generosity and dystopia residual. However, only
the value '0' in the 'Family' column seems like a data error.

We will check which country is this 'family outlier'
'''

#Check who the outlier is
for val in range(len(data_2016['Family'])):
    if data_2016['Family'][val] == 0:
        id = val

print('Outlier country is: ',data_2016['Country'][val])

'''
We see that Burundi has the value of '0' for 'Family' column. It may not be a data entry error, so we will keep an eye on it.
'''

#####

'''
We do the same process for 2017 data. However we see that column names are not very user experience friendly. First we will change those
column names.
'''

#Change the column names of the data from 2017
data_2017= data_2017.rename(columns = { 'Happiness.Rank':'Happiness Rank','Happiness.Score':'Happiness Score', 'Whisker.high': 'Whisker High',
                             'Whisker.low': 'Whisker Low', 'Economy..GDP.per.Capita.':'Economy (GDP per Capita)',
                             'Health..Life.Expectancy.':'Health (Life Expectancy)','Trust..Government.Corruption.':'Trust (Government Corruption)',
                             'Dystopia.Residual': 'Dystopia Residual'})

column_names_17 = list(data_2017.columns)

#Check if there is any outliers
fig_2017 = subplots.make_subplots(rows = 3 , cols = 4)

i=1
j=1

for feature in range(2,len(column_names_17)):
    fig_2017.add_trace(go.Box(name=column_names_17[feature],y=data_2017[column_names_17[feature]]), row=i, col=j)
    if j == 4:
        i += 1
        j = 0
    j += 1

fig_2017.update_layout(title_text="2017 Data Outliers")

fig_2017.show()

'''
We see that there are some outliers in: family, trust, generosity and dystopia residual. However, only
the value '0' in the 'Family' column seems like a data error.

We will check which country is this 'family outlier'
'''

#Check who the outlier is
for val in range(len(data_2017['Family'])):
    if data_2017['Family'][val] == 0:
        id = val

print('Outlier country is: ',data_2017['Country'][val])

'''
We see that Central African Republic has the value of '0' for 'Family' column. It may not be a data entry error, so we will keep an eye on it.
'''

#####

#Check if there is any outliers
fig_2018 = subplots.make_subplots(rows = 3 , cols = 3)

i=1
j=1

for feature in range(3,len(column_names_18)):
    fig_2018.add_trace(go.Box(name=column_names_18[feature],y=data_2018[column_names_18[feature]]), row=i, col=j)
    if j == 3:
        i += 1
        j = 0
    j += 1

fig_2018.update_layout(title_text="2018 Data Outliers")

fig_2018.show()

'''
We see that there are some outliers in: social support, gdp per capita, generosity, corruption and freedom. However, only
the value '0' in the 'Social support' column seems like a data error.

We will check which country is this 'Social support'
'''

#Check who the outlier is
for val in range(len(data_2018['Social support'])):
    if data_2018['Social support'][val] == 0:
        id = val

print('Outlier country is: ',data_2018['Country or region'][val])

'''
We see that Burundi has the value of '0' for 'Social support' column. It may not be a data entry error, so we will keep an eye on it.
'''

#####

#Check if there is any outliers
fig_2019 = subplots.make_subplots(rows = 3 , cols = 3)

i=1
j=1

for feature in range(3,len(column_names_19)):
    fig_2019.add_trace(go.Box(name=column_names_19[feature],y=data_2019[column_names_19[feature]]), row=i, col=j)
    if j == 3:
        i += 1
        j = 0
    j += 1

fig_2019.update_layout(title_text="2019 Data Outliers")

fig_2019.show()

'''
We see that there are some outliers in: social support, healthy life expectancy, generosity, corruption and freedom. However, only
the value '0' in the 'Social support' column seems like a data error.

We will check which country is this 'Social support'
'''

#Check who the outlier is
for val in range(len(data_2019['Social support'])):
    if data_2019['Social support'][val] == 0:
        id = val

print('Outlier country is: ',data_2019['Country or region'][val])

'''
We see that South Sudan has the value of '0' for 'Social support' column. It may not be a data entry error, so we will keep an eye on it.
'''

#####

'''
We check if there is any duplication in dataset
'''

#Check if there is any duplications
if True in list(data_2015.duplicated(subset=['Country'])):
    print('There is duplication in 2015 data')
if True in list(data_2016.duplicated(subset=['Country'])):
    print('There is duplication in 2016 data')
if True in list(data_2017.duplicated(subset=['Country'])):
    print('There is duplication in 2017 data')
if True in list(data_2018.duplicated(subset=['Country or region'])):
    print('There is duplication in 2018 data')
if True in list(data_2019.duplicated(subset=['Country or region'])):
    print('There is duplication in 2019 data')

##### Data Cleaning Step

'''
We should standardize the current datasets. We will rename the columns and drop some if needed. This will help comparing years.
Also we will deal with the missing value from the 2018 data.
'''

all_data = [data_2015,data_2016,data_2017,data_2018,data_2019]

for data in all_data:
    print(data.columns)

'''
We will drop some columns in order to make them all standardized 
'''

#Drop unwanted columns
data_2015 = data_2015.drop('Standard Error', axis = 1)
data_2015 = data_2015.drop('Dystopia Residual', axis = 1)
data_2015 = data_2015.drop('Region', axis = 1)
data_2016 = data_2016.drop('Region', axis = 1)
data_2016 = data_2016.drop('Lower Confidence Interval', axis = 1)
data_2016 = data_2016.drop('Upper Confidence Interval', axis = 1)
data_2016 = data_2016.drop('Dystopia Residual', axis = 1)
data_2017 = data_2017.drop('Whisker High', axis = 1)
data_2017 = data_2017.drop('Whisker Low', axis = 1)
data_2017 = data_2017.drop('Dystopia Residual', axis = 1)

'''
We see that in datasets, some columns are in different order than other datasets. We will take the 2015 data as standard.
And will relocate them.
'''

#Change the order of columns
data_2017 = data_2017.iloc[:,[0,1,2,3,4,5,6,8,7]]
data_2018 = data_2018.iloc[:,[1,0,2,3,4,5,6,8,7]]
data_2019 = data_2019.iloc[:,[1,0,2,3,4,5,6,8,7]]

'''
We see that column names are not very user experience friendly. We will change column names.
'''
data_2015= data_2015.rename(columns = { 'Health (Life Expectancy)':'Healthy Life Expectancy','Family':'Social Support'})

data_2016= data_2016.rename(columns = { 'Health (Life Expectancy)':'Healthy Life Expectancy','Family':'Social Support'})

data_2017= data_2017.rename(columns = { 'Health (Life Expectancy)':'Healthy Life Expectancy','Family':'Social Support'})

data_2018= data_2018.rename(columns = { 'Country or region':'Country','Overall rank':'Happiness Rank', 'Score': 'Happiness Score',
                             'GDP per capita': 'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom',
                             'Perceptions of corruption':'Trust (Government Corruption)',
                             'Healthy life expectancy':'Healthy Life Expectancy',
                             'Social support':'Social Support'})

data_2019= data_2019.rename(columns = { 'Country or region':'Country','Overall rank':'Happiness Rank', 'Score': 'Happiness Score',
                             'GDP per capita': 'Economy (GDP per Capita)', 'Freedom to make life choices':'Freedom',
                             'Perceptions of corruption':'Trust (Government Corruption)',
                             'Healthy life expectancy':'Healthy Life Expectancy',
                             'Social support':'Social Support'})

column_names_15 = list(data_2015.columns)
column_names_16 = list(data_2016.columns)
column_names_17 = list(data_2017.columns)
column_names_18 = list(data_2018.columns)
column_names_19 = list(data_2019.columns)

'''
After making adjustments to these datasets we will check our datasets
'''

all_data = [data_2015,data_2016,data_2017,data_2018,data_2019]
for data in all_data:

    print(data.columns)

'''
We see that every dataset is standardized now
'''

##### Data Visualization Step

#Drop Unnecessary Data for heatmap
data_2015 = data_2015.drop('Happiness Rank', axis = 1)
data_2016 = data_2016.drop('Happiness Rank', axis = 1)
data_2017 = data_2017.drop('Happiness Rank', axis = 1)
data_2018 = data_2018.drop('Happiness Rank', axis = 1)
data_2019 = data_2019.drop('Happiness Rank', axis = 1)

##### Data Cleaning Step Cont'd
#Replace the missing value with the mean value
mean= data_2018['Trust (Government Corruption)'].mean()
data_2018['Trust (Government Corruption)'].replace(np.nan,mean, inplace = True)

##### Data Visualization Step Cont'd
#Create Heatmap
corr_2015 = px.imshow(data_2015.corr(), color_continuous_scale = 'rdbu_r', title= 'Correlation Heatmap')
corr_2015.update_layout(title_x=0.5)
corr_2015.show()

'''
We see that Economy and Social Support are the top 2 categories in relation to the happiness score.
Also We can say that healthy life expectancy is highly correlated with economy. Another eye-catching info is that generosity
and economical situation is negatively correlated but it almost equals to zero.
'''

#Create line graph of countries with their happiness rate through years
happiness_timeline = {
    'Country': [],
    'Happiness Score' : [],
    'Year' : [],

}

for country in data_2015['Country']:
    happiness_timeline['Country'].append(country)

for score in data_2015['Happiness Score']:
    happiness_timeline['Happiness Score'].append(score)

for year in range(len(data_2015['Happiness Score'])):
    happiness_timeline['Year'].append('2015')

for country in data_2016['Country']:
    happiness_timeline['Country'].append(country)

for score in data_2016['Happiness Score']:
    happiness_timeline['Happiness Score'].append(score)

for year in range(len(data_2016['Happiness Score'])):
    happiness_timeline['Year'].append('2016')

for country in data_2017['Country']:
    happiness_timeline['Country'].append(country)

for score in data_2017['Happiness Score']:
    happiness_timeline['Happiness Score'].append(score)

for year in range(len(data_2017['Happiness Score'])):
    happiness_timeline['Year'].append('2017')

for country in data_2018['Country']:
    happiness_timeline['Country'].append(country)

for score in data_2018['Happiness Score']:
    happiness_timeline['Happiness Score'].append(score)

for year in range(len(data_2018['Happiness Score'])):
    happiness_timeline['Year'].append('2018')

for country in data_2019['Country']:
    happiness_timeline['Country'].append(country)

for score in data_2019['Happiness Score']:
    happiness_timeline['Happiness Score'].append(score)

for year in range(len(data_2019['Happiness Score'])):
    happiness_timeline['Year'].append('2019')

happiness_timeline = pd.DataFrame(happiness_timeline)
happiness_timeline = happiness_timeline.sort_values(['Country', 'Year'])

'''
We created a new dataframe that only year, country and happiness score exists in it.
'''
h_index_by_years = {

}

for country in happiness_timeline['Country']:
    if not country in h_index_by_years:
        h_index_by_years[country] = {}
        h_index_by_years[country]['Happiness Score'] = []
        h_index_by_years[country]['Year'] = []

    if country in h_index_by_years:
        h_index_by_years[country]['Happiness Score'].append(happiness_timeline.loc[happiness_timeline['Country'] == country, 'Happiness Score'].iloc[0])
        h_index_by_years[country]['Year'].append(happiness_timeline.loc[happiness_timeline['Country'] == country, 'Year'].iloc[0])
    happiness_timeline.drop(index=happiness_timeline.index[0], axis=0, inplace=True)

'''
We created a new dataframe that contains country dataframes that have year and happiness data in it.
'''

country_dataframes = []
countries = []

for i in h_index_by_years:
    countries.append(i)
    i = pd.DataFrame(h_index_by_years[i])
    country_dataframes.append(i)

happiness_timeline_line_graph = subplots.make_subplots(rows=1,cols=1, y_title='Happiness Score',x_title='Years', column_titles=['Happiness Score Through Years'])

for j in range(len(country_dataframes)):
    happiness_timeline_line_graph.add_trace(go.Line(name=countries[j], x=country_dataframes[j]['Year'],y=country_dataframes[j]['Happiness Score']),1,1)

happiness_timeline_line_graph.show()

'''
We created a line graph that shows 'Happiness Score Through Years' by 'Countries'.
'''

#Create Choropleth Map

choropleth_map_subplot = subplots.make_subplots(rows=3,cols=2, subplot_titles=('2015','2016','2017','2018','2019'),
                                                specs=[[{"type": "scattergeo"}, {"type": "scattergeo"}],
                                                       [{"type": "scattergeo"}, {"type": "scattergeo"}],
                                                       [{"type": "scattergeo"},{"type": "scattergeo"}]])


data_2015_sorted_by_country = data_2015.sort_values('Country')
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Economy (GDP per Capita)', axis=1)
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Social Support', axis=1)
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Healthy Life Expectancy', axis=1)
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Freedom', axis=1)
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Trust (Government Corruption)', axis=1)
data_2015_sorted_by_country = data_2015_sorted_by_country.drop('Generosity', axis=1)


countries_2015 = []
happinesses_2015 = []

for i in data_2015_sorted_by_country['Country']:
    countries_2015.append(i)
for j in data_2015_sorted_by_country['Happiness Score']:
    happinesses_2015.append(j)

choropleth_map_subplot.add_trace(go.Choropleth(
    locations= countries_2015,
    locationmode= 'country names',
    colorscale= 'Portland',
    z= happinesses_2015,
    colorbar= {'title':'Happiness Index'},
    text= ['World Happiness Index']
    ), row=1,col=1)

'''
We will repeat the same process for all given years
'''

data_2016_sorted_by_country = data_2016.sort_values('Country')
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Economy (GDP per Capita)', axis=1)
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Social Support', axis=1)
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Healthy Life Expectancy', axis=1)
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Freedom', axis=1)
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Trust (Government Corruption)', axis=1)
data_2016_sorted_by_country = data_2016_sorted_by_country.drop('Generosity', axis=1)


countries_2016 = []
happinesses_2016 = []

for i in data_2016_sorted_by_country['Country']:
    countries_2016.append(i)
for j in data_2016_sorted_by_country['Happiness Score']:
    happinesses_2016.append(j)

choropleth_map_subplot.add_trace(go.Choropleth(
    locations= countries_2016,
    locationmode= 'country names',
    colorscale= 'Portland',
    z= happinesses_2016,
    text= ['World Happiness Index'],
    showscale=False
    ), row=1,col=2)

'''
This will be the 2017 data
'''
data_2017_sorted_by_country = data_2017.sort_values('Country')
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Economy (GDP per Capita)', axis=1)
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Social Support', axis=1)
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Healthy Life Expectancy', axis=1)
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Freedom', axis=1)
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Trust (Government Corruption)', axis=1)
data_2017_sorted_by_country = data_2017_sorted_by_country.drop('Generosity', axis=1)


countries_2017 = []
happinesses_2017 = []

for i in data_2017_sorted_by_country['Country']:
    countries_2017.append(i)
for j in data_2017_sorted_by_country['Happiness Score']:
    happinesses_2017.append(j)

choropleth_map_subplot.add_trace(go.Choropleth(
    locations= countries_2017,
    locationmode= 'country names',
    colorscale= 'Portland',
    z= happinesses_2017,
    text= ['World Happiness Index'],
    showscale=False
    ), row=2,col=1)

'''
This will be the 2018 data
'''
data_2018_sorted_by_country = data_2018.sort_values('Country')
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Economy (GDP per Capita)', axis=1)
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Social Support', axis=1)
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Healthy Life Expectancy', axis=1)
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Freedom', axis=1)
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Trust (Government Corruption)', axis=1)
data_2018_sorted_by_country = data_2018_sorted_by_country.drop('Generosity', axis=1)


countries_2018 = []
happinesses_2018 = []

for i in data_2018_sorted_by_country['Country']:
    countries_2018.append(i)
for j in data_2018_sorted_by_country['Happiness Score']:
    happinesses_2018.append(j)

choropleth_map_subplot.add_trace(go.Choropleth(
    locations= countries_2018,
    locationmode= 'country names',
    colorscale= 'Portland',
    z= happinesses_2018,
    text= ['World Happiness Index'],
    showscale=False
    ), row=2,col=2)

'''
This will be the 2019 data
'''
data_2019_sorted_by_country = data_2019.sort_values('Country')
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Economy (GDP per Capita)', axis=1)
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Social Support', axis=1)
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Healthy Life Expectancy', axis=1)
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Freedom', axis=1)
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Trust (Government Corruption)', axis=1)
data_2019_sorted_by_country = data_2019_sorted_by_country.drop('Generosity', axis=1)


countries_2019 = []
happinesses_2019 = []

for i in data_2019_sorted_by_country['Country']:
    countries_2019.append(i)
for j in data_2019_sorted_by_country['Happiness Score']:
    happinesses_2019.append(j)

choropleth_map_subplot.add_trace(go.Choropleth(
    locations= countries_2019,
    locationmode= 'country names',
    colorscale= 'Portland',
    z= happinesses_2019,
    text= ['World Happiness Index'],
    showscale=False
    ), row=3,col=1)

choropleth_map_subplot.show()
