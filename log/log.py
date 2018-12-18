from datetime import datetime
import os
import threading


class Log:
    def __init__(self, type: str) -> None:
        self.type = type


    def info(self, msg: str) -> None:
        msg = self._build_msg("info", msg)
        _write_msg(msg)


    def warning(self, msg: str) -> None:
        msg = self._build_msg("warning", msg)
        _write_msg(msg)


    def error(self, msg: str) -> None:
        msg = self._build_msg("error", msg)
        _write_msg(msg)

    
    def _get_ts(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def _build_msg(self, status: str, msg: str) -> str:
        return "{ts} {type} [{status}] {msg}".format(ts=self._get_ts(), type=self.type, status=status, msg=msg)


# There can be multiple instances of the Log class
# but we only want it being written to one place,
# and don't want to have conflicting writes. So we
# have a global function that uses a lock to ensure
# we don't have a race condition on file i/o.

log_lock = threading.Lock()

def _write_msg(msg: str) -> None:
    log_lock.acquire()
    with open("bot.log", "a") as f:
        f.write("{msg}{newline}".format(msg=msg, newline=os.linesep))
    log_lock.release()