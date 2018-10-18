import ConfigParser
import io, json, os, requests, sys
import log

class Slack:
    _config_path = "slack/config.ini"

    def __init__(self):
        self.config = {}
        self._read_config()

    def _read_config(self):
        if not os.path.exists(self._config_path): raise EnvironmentError
        
        with open(self._config_path, "r") as f:
            config_file = f.read()
        
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(config_file))

        for section in config.sections():
            self.config[section] = {}
            for option in config.options(section):
                self.config[section][option] = config.get(section, option)

        log.log("Read in {} config values".format(sum(len(x) for x in self.config.itervalues()))) #pylint: disable=E1101
    
    def send_test(self):
        msg = {}
        msg['text'] = "Test message"

        r = requests.post(self.config['api']['webhook_url'], data=json.dumps(msg))
        if r.status_code == 200:
            log.log("Sent test message")
        else:
            log.log("Failed to send test message", error=True)