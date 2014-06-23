#!/usr/bin/env python

# Start script for Apache Mahout and Hadoop.
import os
import subprocess
import string
import json

from maestro.guestutils import *
from maestro.extensions.logging.logstash import run_service

HUB_CONFIG = '/var/lib/selenium/hubConfig.json'

with open(HUB_CONFIG, 'r') as f:
    data = json.load(f)
    f.close()

data["host"] = os.environ.get('SELENIUM_HUB_HOST', get_container_internal_address())
data["port"] = os.environ.get('SELENIUM_HUB_PORT', 4444)
data["timeout"] = os.environ.get('SELENIUM_HUB_TIMEOUT', 300000)
data["maxSession"] = os.environ.get('SELENIUM_HUB_MAX_SESSION', 15)

with open(HUB_CONFIG, 'w+') as f:
    f.write(json.dumps(data))
    f.close()

# Start Supervisord in the foreground.
run_service(['/usr/bin/supervisord', '-n'])
