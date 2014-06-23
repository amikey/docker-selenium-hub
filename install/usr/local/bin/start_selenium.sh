#!/bin/bash

USAGE="Usage: start_selenium <hubConfig>"

HUB_CONFIG="$1"

if [ "$HUB_CONFIG" = "" ]; then
  echo "ERROR: Missing HUB_CONFIG." $USAGE
  exit -1;
fi

export DISPLAY=:99

/etc/init.d/xvfb start
java -jar /var/lib/selenium/selenium-server-standalone-2.42.2.jar \
-role hub -hubConfig $HUB_CONFIG
