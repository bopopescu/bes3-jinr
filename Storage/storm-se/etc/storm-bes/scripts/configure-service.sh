#!/bin/bash

BES_STORAGE_AREA=/besfs/bes

BASE_DIR=`dirname $0`/..
STORM_HTTPD_CONF_DIR="${BASE_DIR}/httpd/conf.d"
HTTPD_CONF_DIR="/etc/httpd/conf.d"

if [ ! -f /etc/storm-bes/siteinfo/storm.def ]; then
    echo "Main configuration file was not found. Please run 'make-configs.sh' first"
    exit 1
fi

if [ ! -f /etc/grid-security/hostcert.pem ] || [ ! -f /etc/grid-security/hostkey.pem ]; then
    echo "Host certificate hostcert.pem and/or hostkey.pem was not found in /etc/grid-security"
    exit 2
fi

# Storage area permissions: set if it is already exists
# From StoRM's guide:
# "YAIM-StoRM doesn't set the correct permissions if the SA's root directory already exists"
if [ -d "$BES_STORAGE_AREA" ]; then
    if ! id -u storm >/dev/null 2>&1; then
        echo "User 'storm' does not exist, creating"
        useradd -M storm
    fi
    chown -RL storm:storm $BES_STORAGE_AREA
    chmod -R o-rwx,g+r $BES_STORAGE_AREA
fi


/opt/glite/yaim/bin/yaim -c -d 6 -s /etc/storm-bes/siteinfo/storm.def -n se_storm_backend -n se_storm_frontend -n se_storm_gridftp 2>&1

if [ $? -ne 0 ]; then
    exit $?
fi


httpd_groups=`groups apache | cut -f 2 -d ":"`

if [[ ! $httpd_groups =~ "bes" ]]; then
    echo "User 'apache' isn't in 'bes' group, adding it there."
    usermod -a -G bes apache
fi

if [[ ! $httpd_groups =~ "storm" ]]; then
    echo "User 'apache' isn't in 'storm' group, adding it there."
    usermod -a -G storm apache
fi

echo "Writing httpd configs for WebDAV"

cp -af $STORM_HTTPD_CONF_DIR/* -t $HTTPD_CONF_DIR

echo "Restarting httpd server to enable WebDAV access"

chkconfig httpd on
service httpd restart

echo
echo "Configuration is done, now you could check the service itself."
echo
