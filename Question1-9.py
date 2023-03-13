# Title: Problem for Covid - 19 Data Analysis Project using Python
# Perform following analysis on above dataset : 1. Import the dataset using Pandas from above mentioned url.


import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv")

print(df)

# 2. High Level Data Understanding:
# a. Find no. of rows & columns in the dataset

print("NUMBER OF ROWS-", df.shape[0])
print("NUMBER OF COLUMNS-", df.shape[1])

# b. Data types of columns.

print(df.dtypes)

# c. Info & describe of data in dataframe.

print(df.info())
print(df.describe())

# 3. Low Level Data Understanding :
# a. Find count of unique values in location column.

print(df.location.value_counts())

# b. Find which continent has maximum frequency using values counts.

print(df.continent.value_counts())

print(df.continent.mode())

# c. Find maximum & mean value in 'total_cases'.

print(df.total_cases.max())

# d. Find 25%,50% & 75% quartile value in 'total_deaths'.

print("25% QUARTILE VALUE: ", df.total_deaths.quantile(0.25))
print("50% QUARTILE VALUE: ", df.total_deaths.quantile(0.50))
print("75% QUARTILE VALUE: ", df.total_deaths.quantile(0.75))

#  e. Find which continent has maximum 'human_development_index'.

max_hdi = df.groupby('continent')['human_development_index'].sum()

print(max_hdi.sort_values(ascending=False).head(1))

# f. Find which continent has minimum 'gdp_per_capita'.

min_gdppc = df.groupby('continent')['gdp_per_capita'].sum()

print(min_gdppc.sort_values(ascending=True).head(1))

# 4. Filter the dataframe with only this columns ['continent','location','date','total_cases','total_deaths','gdp_per_ca pita',' human_development_index'] and update the data frame.

columns = ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']

print(df[columns])

# 5. Data Cleaning

# a. Remove all duplicates observations

print(df.head())
df.drop_duplicates(inplace=True)
print(df.duplicated().unique())

# b. Find missing values in all columns

print((df.isna().sum)())

# c. Remove all observations where continent column value is missing Tip : using subset parameter in dropna

df.dropna(subset=["continent"], inplace=True)
print(df)

#  d. Fill all missing values with 0**

df.fillna(0, inplace=True)
print(df)

# 6. Date time format :

# a. Convert date column in datetime format using pandas.to_datetime

print(type(df.date[0]))

df['date'] = pd.to_datetime(df['date'])
print(type(df.date[0]))

# b. Create new column month after extracting month data from date column

df['month'] = df['date'].dt.month
print(df.columns)

# 7. Data Aggregation:

# a. Find max value in all columns using groupby function on 'continent' column Tip: use reset_index() after applying groupby

print((df.groupby('continent').max()).reset_index())

# b. Store the result in a new dataframe named 'df_groupby'. (Use df_groupby dataframe for all further analysis)

df_groupby = df.groupby('continent').max().reset_index()
print(df_groupby)

# 8. Feature Engineering :

# a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'

df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']
print(df_groupby[['continent', 'total_deaths_to_total_cases']])

# 9. Data Visualization :

# a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.

import seaborn as sns
print(sns.displot(df_groupby['gdp_per_capita'], kde=False))

# b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'

print(sns.scatterplot(data=df_groupby, x='gdp_per_capita', y='total_cases'))

# c. Plot Pairplot on df_groupby dataset.

print(sns.pairplot(df_groupby))

# d. Plot a bar plot of 'continent' column with 'total_cases' . Tip : using kind='bar' in seaborn catplot

print(sns.catplot(data=df_groupby, x='continent', y='total_cases', kind='bar'))

# 10.Save the df_groupby dataframe in your local drive using pandas.to_csv function .

df_groupby.to_csv(r'C:\Users\dell\OneDrive\Desktop\datawranglingproject.csv')