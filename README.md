# Internet Speed Tester
The python script checking for internet speed is run every hour (using a cronjob), this data is appended to a CSV file. Another python script is run every day (using another cronjob) to plot a graph of internet speed vs time.

## Tech Used:
* matplotlib
* numpy
* pandas
* speedtest-cli
