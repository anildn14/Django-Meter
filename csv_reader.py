import csv
import operator
from natsort import natsorted,realsorted

with open('D:\\Anil\\Anil_Latest\\Python\\Django\\Meter\\MeterReading\\Sorted_Connection_Histories\\ConnectionList(1-50Meters).csv','r') as a:
	reader = csv.reader(a, delimiter=',')
	sort1=natsorted(reader,key=lambda row: (row[0]))

	for row in sort1:
		print (', '.join(row))

