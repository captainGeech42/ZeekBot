from log import Log

import json


# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html


class Config:
    class __Config:
        """Singleton class for Config"""
        def __init__(self, path: str):
            self.path = path
            self.log = Log("config")

            if self.path:
                self._load_config()
            else:
                self.log.error("config path not set, exiting")
                exit(1)

        
        def _load_config(self) -> None:
            """Read in JSON config"""
            try:
                with open(self.path, "r") as f:
                    self.config = json.load(f)
                self.log.info("read in config")
            except Exception as e:
                self.log.error("error reading in config: {e}".format(e=str(e)))


    _instance = None
    path = None

    def __new__(cls):
        if not Config._instance:
            Config._instance = Config.__Config(Config.path)
        return Config._instance


    def get_config(self, section: str) -> """Dict[str, str] or Dict[str, Dict[str, str]]""":
        """Return the dictionary of config items for a given section (i.e. "slack", "zeek", etc.)"""
        try:
            return self._instance.config[section]
        except Exception as e:
            self._instance.log.error("error retrieving config for \"{section}\": {e}".format(section=section, e=str(e)))
            return None