from slack import Slack
from log import Log
from config import Config

import sys


def main(argv):
    # Initialize log
    log = Log("main")

    # Write log messages to stdout if debugging
    if "debug" in argv:
        Log.stdout = True

    try:
        # Set static class var for config path
        Config.path = "config.json"

        log.info("Starting bot")

        s = Slack()
        s.send_test()

        log.info("Exiting")
    except Exception as e:
        log.error("unhandled exception, exiting: {e}".format(e=str(e)))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
