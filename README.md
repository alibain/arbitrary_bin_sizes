# arbitrary_bin_sizes
bin experimental data by specifying the bin width in x-dimention.

bin_data.py holds the function to bin experimental data by setting bin width
data_binned(df,minbin,stepsize)
df = experimental data in a DataFrame, first column should be x-data and second column y-data.
minbin = minimum value for bins to start at, <= min(x) to bin all data
stepsize = binwidth. Binwidth can be less than 1. 

outputs a dataframe with columns x, \sigma x, y, \sigma y containing the mean and standard deviation for x and y data in databin. Output length will be shorter than expected number of bins if some bins do not contain any data. 
