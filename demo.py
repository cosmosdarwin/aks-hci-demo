# Note: Requires Python 3 and assumes the local time is UTC (+0).

import subprocess
import time
from datetime import datetime, timedelta

# 1a. Start shell to run 'cat /proc/1/cpuset'
RAW_OUTPUT = subprocess.check_output("cat /proc/1/cpuset", shell=True, universal_newlines=True)

# 1b. Trim off the newline
CONTAINER_ID = RAW_OUTPUT.split("\n")[0]

# 2a. Start shell to run 'stat /proc/1/cmdline'
RAW_OUTPUT = subprocess.check_output("stat /proc/1/cmdline", shell=True, universal_newlines=True)

# 2b. Extract process start time as line 5, chars 8-27, and parse
CONTAINER_START_TIME = datetime.strptime(RAW_OUTPUT.split("\n")[5][8:27], "%Y-%m-%d %H:%M:%S")

LOG_FILE_PATH = "/storage/log.txt"

while (True):
  CURRENT_UTC_TIME = datetime.utcnow()

  if (CURRENT_UTC_TIME.second == 0):

    SHORT_TIMESTAMP = CURRENT_UTC_TIME.strftime("%I:%M:%S %p")
    CONTAINER_AGE = int((CURRENT_UTC_TIME - CONTAINER_START_TIME).total_seconds()/60)

    log = open(LOG_FILE_PATH, "a+")
    log.write("[{}] Hello from container {}! I've been running for {} minutes.\n".format(SHORT_TIMESTAMP, CONTAINER_ID, CONTAINER_AGE))
    log.close()

  time.sleep(1)