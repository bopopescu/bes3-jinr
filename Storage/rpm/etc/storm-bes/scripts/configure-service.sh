#!/bin/bash

if [ ! -f /etc/storm-bes/siteinfo/storm.def ]; then
    echo "Main configuration file was not found. Please run 'make-configs.sh' first"
    exit 1
fi

if [ ! -f /etc/grid-security/hostcert.pem ] || [ ! -f /etc/grid-security/hostkey.pem ]; then
    echo "Host certificate hostcert.pem and/or hostkey.pem was not found in /etc/grid-security"
    exit 2
fi


/opt/glite/yaim/bin/yaim -c -d 6 -s /etc/storm-bes/siteinfo/storm.def -n se_storm_backend -n se_storm_frontend -n se_storm_gridftp 2>&1


