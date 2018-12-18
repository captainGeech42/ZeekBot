from datetime import datetime
import os
import threading


class Log:
    def __init__(self, type: str):
        self.type = type


    def info(self, msg: str):
        self._build_msg("info", msg)


    def warning(self, msg: str):
        self._build_msg("warning", msg)


    def error(self, msg: str):
        self._build_msg("error", msg)

    
    def _get_ts(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def _build_msg(self, status: str, msg: str) -> str:
        return "{ts} {type} [{status}] {msg}".format(self._get_ts(), self.type, status, msg)


log_lock = threading.Lock()

def _write_msg(msg):
    log_lock.acquire()
    with open("bot.log", "a") as f:
        f.write("{msg}{newline}".format(msg, os.linesep))
    log_lock.release()