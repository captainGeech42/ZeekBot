from datetime import datetime
import os

def log(msg, error=False):
    line = ""

    line += _get_ts()

    line += " [ERROR] " if error else " [STATUS] "

    line += msg

    line += os.linesep

    with open(_get_fp(), "a") as f:
        f.write(line)

def _get_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _get_fp():
    return "slack.log"