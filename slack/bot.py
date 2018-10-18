from slack import Slack
import log

def main():
    s = Slack()
    s.send_test()

if __name__ == "__main__":
    log.log("Starting bot")

    main()

    log.log("Bot exiting")