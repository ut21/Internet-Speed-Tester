import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

data=pd.read_csv('speed_data.csv')

#only plot data from today
today=datetime.datetime.now().date()
data=data[data['DATE']==str(today)]

upload_speed=data['Upload Speed'].tolist()
download_speed=data['Download Speed'].tolist()
time=data['TIME'].tolist()
date=data['DATE'].tolist()

upload_speed=np.array(upload_speed)
download_speed=np.array(download_speed)
time=np.array(time)
date=np.array(date)

plt.plot(time, upload_speed, label='Upload Speed')
plt.xlabel('Time')
plt.ylabel('Upload Speed (MB)')
plt.title('Upload Speed vs Time for \n' + today.strftime("%B %d, %Y"))
plt.show()
