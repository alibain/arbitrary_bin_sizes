import pandas as pd
import numpy as np
def data_binned(df,minbin,stepsize):
    sorted_data=df.sort_values(by=[df.columns[0]]) #sort dataframe from low to high by x column
    out=pd.DataFrame(columns=['x','σx','y','σy']) #output dataframe
    dx=[]#dummy x-array
    dy=[]#dummy y-array
    i=0
    a=minbin
    b=stepsize
    while i<len(sorted_data): #loop through sorted data
        j=sorted_data.iloc[i].x
        if j >= a and j < b: #is x-value in the bin?
        #if yes, appned to dummy array
        #if no, take mean and sdv of dummy arrays and move to next bin
            dx=np.append(dx,j) 
            dy=np.append(dy,sorted_data.iloc[i].y)
            i=i+1
            #print(i)
        elif len(dx)>0: # for bin with data, calculate means and sdvs and move to next bin
            mx=np.mean(dx)
            mxe=np.std(dx)
            my=np.mean(dy)
            mye=np.std(dy)
            dx=[]#empty dummy x-array
            dy=[]#empty dummy y-array
            out.loc[len(out)]=[mx,mxe,my,mye] #append binned data to dataframe
            a=b
            b=b+stepsize
        else: # bin without data, move to next bin
            a=b
            b=b+stepsize
    #mean and sdv of final bin
    mx=np.mean(dx)
    mxe=np.std(dx)
    my=np.mean(dy)
    mye=np.std(dy)
    out.loc[len(out)]=[mx,mxe,my,mye]
    out=out.dropna()
    return out 
