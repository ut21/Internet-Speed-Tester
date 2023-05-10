import speedtest as spd
import csv
import datetime
speed_test=spd.Speedtest()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

upload_speed = bytes_to_mb(speed_test.upload())
download_speed = bytes_to_mb(speed_test.download())

upload=[]
download=[]
time=[]
date=[]
upload.append(upload_speed)
download.append(download_speed)
time.append(datetime.datetime.now().strftime("%H:%M"))
date.append(datetime.datetime.now().date())

speed_data=[datetime.datetime.now().date(),datetime.datetime.now().strftime("%H:%M"), upload_speed, download_speed]

with open('speed_data.csv', 'a') as f:
  csv_writer = csv.writer(f)
  csv_writer.writerow(speed_data)