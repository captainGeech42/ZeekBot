from slack import Slack
from log import Log
from config import Config

import sys


def main(argv):
    Config.path = "config.json"

    log = Log("main")
    log.info("Starting bot")

    s = Slack()
    s.send_test()

    log.info("Exiting")


if __name__ == "__main__":
    sys.exit(main(sys.argv))