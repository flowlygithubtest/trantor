# python code to print label , reponsecode, resp message and failure_message for the requests with status code is non succes
import csv
from datetime import datetime
import time
from pytz import timezone
import pytz
def csv_reader(file1, file2):
    date_format='%Y-%m-%d %H:%M:%S %Z'
    
    with open(file2) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        row=1
        for row in reader:
            status_code = row['responseCode']
            if(status_code != '200'):
                label= row['label']
                response_code = row['responseCode'] 
                response_message=row['responseMessage'] 
                failure_message= row['failureMessage']
                timestamp = row['timeStamp']
                dt_object = datetime.fromtimestamp(int(timestamp)/1000)
                date = dt_object.astimezone(timezone('US/Pacific'))    
                print(label, " ",response_code," ",response_message," ",failure_message)
csv_reader("Jmeter_log1.jtl","Jmeter_log2.jtl")