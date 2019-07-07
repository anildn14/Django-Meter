import pandas as pd 
import glob
import pandas as pd
from natsort import natsorted

file = "D:\\Anil\\Anil_Latest\\Python\\Django\\Meter\\MeterReading\\All_Readings.csv"
print "file :",file
df = pd.read_csv(file, header=None,skiprows=1, sep=",")
# df.sort_values([1,0], axis=0, inplace=True)
print "df :",len(set(df[1]))