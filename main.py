from slack import Slack
from log import Log

import sys

def main(argv):
    s = Slack()
    s.send_test()


if __name__ == "__main__":
    sys.exit(main(sys.argv))