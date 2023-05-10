# Internet Speed Tester
The python script checking for internet speed is run every hour (using a cronjob), this data is appended to a CSV file. Another python script is run every day (using another cronjob) to plot a graph of internet speed vs time. Mostly built as a use case for working with cronjob and matplotlib

## Tech Used:
* matplotlib
* numpy
* pandas
* cronjobs
* speedtest-cli

## Resources regarding Cronjobs:
If you have a linux based system, learn how to set up cronjobs. Here are some resources that helped me learn it (Make sure you have given the correct permissions to acess your files):
* https://linuxhint.com/run-multiple-commands-same-cron-job/
* https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
* https://unix.stackexchange.com/questions/502490/how-to-schedule-cron-jobs-in-linux
* https://stackoverflow.com/questions/892104/how-to-give-permission-for-the-cron-job-file
* https://linuxhandbook.com/check-crontab-logs/
