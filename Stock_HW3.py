#Program to download stock prices from urls onto csv, manipulate and write to new files
import os
from urllib.request import urlopen
import csv

#List for urls of each input file
url = ['https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true',
       'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607806303&period2=1639342303&interval=1d&events=history&includeAdjustedClose=true',
       'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1607806351&period2=1639342351&interval=1d&events=history&includeAdjustedClose=true']
filenames = ['GOOG.csv','IBM.csv','MSFT.csv'] #List for filenames of each input file
for i in range(3): #for operating 3 input files
    local_read_path = os.path.join(os.getcwd(), 'data', filenames[i])
    with urlopen(url[i]) as file, open(local_read_path, 'wb') as f:
        f.write(file.read()) #download input file
    local_write_path = os.path.join(os.getcwd(), 'data', 'output',filenames[i]) #Define path of output file
    this_output_file = open(local_write_path, 'w',newline='') #open output file
    this_csv_writer = csv.writer(this_output_file)

    with open(local_read_path, 'r') as this_csv_file:
        this_csv_reader = csv.reader(this_csv_file, delimiter=",")
        header = next(this_csv_reader) #Read Header of input file
        header.append("Change") #Append new column name
        this_csv_writer.writerow(header) #Write header of output file
        for line in this_csv_reader: #Read each line of input file
            this_date = line[0]
            this_open = line[1]
            this_high = line[2]
            this_low = line[3]
            this_close = line[4]
            this_adj_close = line[5]
            this_adj_vol = line[6]
            this_change = (float(this_close) - float(this_open))/float(this_open) #Calculate new value
            line.append(str(this_change)) #Add the new value to line
            this_csv_writer.writerow(line) #Write the formatted line to output file
    this_output_file.close() #Close output file