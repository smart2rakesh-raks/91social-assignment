import os
import datetime

path = "test.log"
directory = os.path.join(path)
data = ""
for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith(".log"):
            file = open(file, 'rU')
            data += file.read()
            file.close()
           
date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
file_name =  date_time + ".txt"
file = open(file_name, 'w')
file.write(data)
file.close()





