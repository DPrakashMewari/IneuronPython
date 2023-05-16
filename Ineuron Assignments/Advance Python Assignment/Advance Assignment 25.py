# Q1. What is the distinction between a numpy array and a pandas data frame? Is there a way to convert between the two if there is ?
# Ans: Numpy Ndarray provides a lot of convenient and optimized methods for performing several mathematical operations on vectors.

# Pandas Dataframe is an in-memory 2-dimensional tabular representation of data. In simpler words, it can be seen as a spreadsheet having rows and columns.

# Conversion : Dataframe=pandas.DataFrame(array)

# Q2. Identify some of the plotting techniques that are used to produce a stock-market chart ?
# Ans: Bar chart, Line Chart, are used for plotting.

# Q3. Why is it essential to print a legend on a stock market chart ?
# Ans: Legend Param will help comparison between different stocks, so will be essential on a stock market chart


# Q4. What is the best way to limit the length of a pandas data frame to less than a year ?
# To limit the length of a Pandas DataFrame to less than a year, 
# you can filter the DataFrame based on the date range.
# Assuming your DataFrame has a column representing dates, you can use the following steps:
# Ensure the date column is of the appropriate datetime data type. If it is not already, 
# you can convert it using the pd.to_datetime() function:
# df['date'] = pd.to_datetime(df['date'])


# Q5. What is the definition of a 180-day moving average ?
# Ans: : The 180-day moving average is represented as a line on charts and represents 
# the average price over the past 180 days. The moving average can give traders a
#  sense regarding whether the trend is up or down, 
# while also identifying potential support or resistance areas.