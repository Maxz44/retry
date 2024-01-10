#!/usr/bin/env python3
import sys, subprocess, time, datetime

cmd = " ".join(sys.argv[1:])

wait_time = 1
max_wait_time = 2**6
error = True


# do while
while error:
    rslt = subprocess.run(cmd, shell=True)
    error = rslt.returncode !=0
    if error:
        print(f'[{datetime.datetime.now()}] Waiting {wait_time}s')
        time.sleep(wait_time)
        if wait_time < max_wait_time:
            wait_time = wait_time * 2
