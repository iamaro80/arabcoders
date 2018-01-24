import os
import time

while True:
    os.system('speedtest-cli --server 3650  --csv --csv-delimiter "," >>"C:\speedtest\orange-speedtest.csv"')
    time.sleep(60)
