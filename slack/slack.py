from config import Config
from log import Log

import io
import json
import os
import requests
import sys


class Slack:
    def __init__(self):
        self.log = Log("slack")
        self._get_config()

    def _get_config(self):
        """Get relevant config entries from Config"""
        c = Config()
        self.config = c.get_config("slack")

    def send_test(self):
        """Send test message to ensure webhook is working"""
        r = requests.post(
            self.config['webhook_url'], data=json.dumps(self._build_alert_json("asdf", "asdf", "asdf")))

        if r.status_code == 200:
            self.log.info("Sent test message")
        else:
            self.log.error("Failed to send test message (status code = {code})".format(
                code=r.status_code))

    def _build_alert_json(self, fallback: str, notice_type: str, notice_text: str):
        obj = {
            "attachments": [
                {
                    "fallback": "Zeek notice: {}".format(fallback),
                    "pretext": "Zeek generated the following notice:",
                    "fields": [
                        {
                            "title": "Type",
                            "value": "{}".format(notice_type),
                            "short": True
                        },
                        {
                            "title": "Notice",
                            "value": "{}".format(notice_text),
                            "short": True
                        }
                    ],
                    "color": "warning"
                }
            ]
        }

        return obj
