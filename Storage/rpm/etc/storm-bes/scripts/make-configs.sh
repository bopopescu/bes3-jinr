#!/bin/bash

cd `dirname $0`/..

SCRIPT_DIR=`pwd`/scripts
CONFIG_DIR=`pwd`/siteinfo
MAIN_CONFIG="$CONFIG_DIR/storm.def"
USERS_CONF="$CONFIG_DIR/storm-users.conf"
GROUPS_CONF="$CONFIG_DIR/storm-groups.conf"
SITE_NAME=`hostname -f`


# Replace one substring with another in stdin
myreplace() {
    a=`echo $1 | sed 's/\//\\\\\//g'`
    b=`echo $2 | sed 's/\//\\\\\//g'`
    cat | sed "s/$a/$b/g"
}

# Read parameter value from main configuration file
get_config_value() {
    local val=`grep "$1=" "$MAIN_CONFIG" | cut -f 2 -d '=' | tr -d '\n"' `
    read  -rd '' val <<< "$val" # trimming leading and trailing spaces
    echo $val
}



# Try to get settings from previous installation if any
if [ -f "$MAIN_CONFIG" ]; then
    NTP_HOSTS_IP_=`get_config_value NTP_HOSTS_IP`
    MYSQL_PASSWORD=`get_config_value MYSQL_PASSWORD`
    STORM_DB_PWD=`get_config_value STORM_DB_PWD`
    STORM_BES_ONLINE_SIZE_=`get_config_value STORM_BES_ONLINE_SIZE`
    STORM_BE_XMLRPC_TOKEN=`get_config_value STORM_BE_XMLRPC_TOKEN`
fi

# Setting default values for non-initialized parameters

if [ -z "$NTP_HOSTS_IP_" ]; then
    NTP_HOSTS_IP_="202.112.31.197 218.75.4.130 114.113.198.166 202.112.10.36"
fi 

if [ -z "$MYSQL_PASSWORD" ]; then
    MYSQL_PASSWORD=`mkpasswd -s 0 -l 12`
fi

if [ -z "$STORM_DB_PWD" ]; then
    STORM_DB_PWD=`mkpasswd -s 0 -l 12`
fi

if [ -z "$STORM_BES_ONLINE_SIZE_" ]; then
    STORM_BES_ONLINE_SIZE_="1"
fi

if [ -z "$STORM_BE_XMLRPC_TOKEN" ]; then
    STORM_BE_XMLRPC_TOKEN=`mkpasswd -s 0 -l 15`
fi


# Propmt admin to enter or confirm configuration parameters

echo -n "Please specify domain name [`hostname -d`]: "
read MY_DOMAIN
if [ -z "$MY_DOMAIN" ]; then
    MY_DOMAIN=`hostname -d`
fi

echo -n "Please specify current host name [`hostname -f`]: "
read STORM_BACKEND_HOST
if [ -z "$STORM_BACKEND_HOST" ]; then
    STORM_BACKEND_HOST=`hostname -f`
fi

echo -n "Please specify NTP hosts IP addresses (divided by spaces) ['$NTP_HOSTS_IP_']: "
read NTP_HOSTS_IP
if [ -z "$NTP_HOSTS_IP" ]; then
    NTP_HOSTS_IP="$NTP_HOSTS_IP_"
fi

echo -n "Size of /besfs storage (in GB, integer) [$STORM_BES_ONLINE_SIZE_]: "
read STORM_BES_ONLINE_SIZE
if [ -z "$STORM_BES_ONLINE_SIZE" ]; then
    STORM_BES_ONLINE_SIZE="$STORM_BES_ONLINE_SIZE_"
fi


# Confirm configuration

OK="n"
echo -n "Is this information correct (y/n)? [$OK]: "
read OK


if [ ! "$OK" == "y" ]; then
    echo "If you've entered incorrect information, you should run setup again"
    exit 1
fi


if [ -f "$MAIN_CONFIG" ]; then
    cp "$MAIN_CONFIG" "$MAIN_CONFIG.backup_`date +%Y%m%d_%H%M%S`"
fi

echo
echo "Writing main configuration file $MAIN_CONFIG"
echo

cat "$MAIN_CONFIG.template" | \
    myreplace "SITE_NAME=\"???\"" "SITE_NAME=\"$SITE_NAME\"" | \
    myreplace "MY_DOMAIN=\"???\"" "MY_DOMAIN=\"$MY_DOMAIN\"" | \
    myreplace "STORM_BACKEND_HOST=\"???\"" "STORM_BACKEND_HOST=\"$STORM_BACKEND_HOST\"" | \
    myreplace "NTP_HOSTS_IP=\"???\"" "NTP_HOSTS_IP=\"$NTP_HOSTS_IP\"" | \
    myreplace "USERS_CONF=\"???\"" "USERS_CONF=\"$USERS_CONF\"" | \
    myreplace "GROUPS_CONF=\"???\"" "GROUPS_CONF=\"$GROUPS_CONF\"" | \
    myreplace "MYSQL_PASSWORD=\"???\"" "MYSQL_PASSWORD=\"$MYSQL_PASSWORD\"" | \
    myreplace "STORM_DB_PWD=\"???\"" "STORM_DB_PWD=\"$STORM_DB_PWD\"" | \
    myreplace "STORM_BES_ONLINE_SIZE=\"???\"" "STORM_BES_ONLINE_SIZE=$STORM_BES_ONLINE_SIZE" | \
    myreplace "STORM_BE_XMLRPC_TOKEN=\"???\"" "STORM_BE_XMLRPC_TOKEN=$STORM_BE_XMLRPC_TOKEN" \
  > "$MAIN_CONFIG"


chmod 750 $MAIN_CONFIG

echo
echo "To configure service, please run 'bash $SCRIPT_DIR/configure-service.sh'"
echo

