#!/bin/bash

DIR_=`dirname $0`/..
BASE_DIR=`readlink -f $DIR_`

SCRIPT_DIR="${BASE_DIR}/scripts"
CONFIG_DIR="${BASE_DIR}/siteinfo"
MAIN_CONFIG="$CONFIG_DIR/storm.def"
USERS_CONF="$CONFIG_DIR/storm-users.conf"
GROUPS_CONF="$CONFIG_DIR/storm-groups.conf"

# Default values
DEF_NTP_HOSTS_IP="202.112.31.197 218.75.4.130 114.113.198.166 202.112.10.36"
DEF_SRM_PORT=8444
DEF_WEBDAV_PORT=2880

SITE_NAME=`hostname -f`

# WebDAV configuration files
WEBDAV_CONF_DIR="${BASE_DIR}/httpd/conf.d"
WEBDAV_HTTPD_CONF="${WEBDAV_CONF_DIR}/bes-webdav.conf"
WEBDAV_SECURED_CONF="${WEBDAV_CONF_DIR}/bes-webdav/secured.include"
WEBDAV_ANON_CONF="${WEBDAV_CONF_DIR}/bes-webdav/anonymous.include"

WEBDAV_TMPL_DIR="${BASE_DIR}/httpd/templates"
WEBDAV_HTTPD_TMPL="$WEBDAV_TMPL_DIR/bes-webdav.conf"
WEBDAV_SECURED_TMPL="$WEBDAV_TMPL_DIR/bes-webdav/secured.include"
WEBDAV_ANON_TMPL="$WEBDAV_TMPL_DIR/bes-webdav/anonymous.include"



# Replace one substring with another in stdin
myreplace() {
    a=`echo $1 | sed -r 's/\//\\\\\//g'`
    b=`echo $2 | sed -r 's/\//\\\\\//g'`
    cat | sed "s/$a/$b/g"
}

cond_replace() {
    if $1; then
        myreplace $2 $3
    fi
}

# Read parameter value from configuration file (main one by default)
get_config_value() {
    local config=${2:-$MAIN_CONFIG}
    local val=`grep "$1=" "$config" | cut -f 2 -d '=' | tr -d '\n"' `
    read  -rd '' val <<< "$val" # trimming leading and trailing spaces
    echo $val
}

####################################################################################################

# Try to get settings from previous installation if any
if [ -f "$MAIN_CONFIG" ]; then
    NTP_HOSTS_IP_=`get_config_value NTP_HOSTS_IP`
    MYSQL_PASSWORD=`get_config_value MYSQL_PASSWORD`
    STORM_DB_PWD=`get_config_value STORM_DB_PWD`
    STORM_BES_ONLINE_SIZE_=`get_config_value STORM_BES_ONLINE_SIZE`
    STORM_BE_XMLRPC_TOKEN=`get_config_value STORM_BE_XMLRPC_TOKEN`
    STORM_FRONTEND_PORT_=`get_config_value STORM_FRONTEND_PORT`
fi

if [ -f $WEBDAV_HTTPD_CONF ]; then
    grep -e "^\s*Include .*/secured.include" $WEBDAV_HTTPD_CONF >/dev/null 2>&1
    [ $? -ne 0 ] && WEBDAV_HTTPS_PORT_=0

    grep -e "^\s*Include .*/anonymous.include" $WEBDAV_HTTPD_CONF >/dev/null 2>&1
    [ $? -ne 0 ] && WEBDAV_HTTP_PORT_=0
fi

if [[ ("$WEBDAV_HTTPS_PORT_" != "0") && -f "$WEBDAV_SECURED_CONF" ]]; then
    WEBDAV_HTTPS_PORT_=`grep "<VirtualHost " "$WEBDAV_SECURED_CONF" | cut -f2 -d ":" | cut -f1 -d ">" `
fi

if [[ ("$WEBDAV_HTTP_PORT_" != "0") && -f "$WEBDAV_ANON_CONF" ]]; then
    WEBDAV_HTTP_PORT_=`grep "<VirtualHost " "$WEBDAV_ANON_CONF" | cut -f2 -d ":" | cut -f1 -d ">" `
fi


# Setting default values for non-initialized parameters

[ -z "$NTP_HOSTS_IP_" ] && NTP_HOSTS_IP_="$DEF_NTP_HOSTS_IP"
[ -z "$MYSQL_PASSWORD" ] && MYSQL_PASSWORD=`mkpasswd -s 0 -l 12`
[ -z "$STORM_DB_PWD" ] && STORM_DB_PWD=`mkpasswd -s 0 -l 12`

if [ -z "$STORM_BES_ONLINE_SIZE_" ]; then
    bes_storage_area=`get_config_value STORM_DEFAULT_ROOT $MAIN_CONFIG.template`
    if [ -d $bes_storage_area ]; then
        sa_size_gb=`df -BG $bes_storage_area | tail -1 | awk '{print $2}' | tr -d "G"`
    fi
    STORM_BES_ONLINE_SIZE_=${sa_size_gb:-"1"}
fi

[ -z "$STORM_BE_XMLRPC_TOKEN" ] && STORM_BE_XMLRPC_TOKEN=`mkpasswd -s 0 -l 15`
[ -z "$STORM_FRONTEND_PORT_" ] && STORM_FRONTEND_PORT_=$DEF_SRM_PORT
[ -z "$WEBDAV_HTTPS_PORT_" ] && WEBDAV_HTTPS_PORT_=$DEF_WEBDAV_PORT
[ -z "$WEBDAV_HTTP_PORT_" ] && WEBDAV_HTTP_PORT_=0


# Propmt admin to enter or confirm configuration parameters

echo -n "Please specify domain name [`hostname -d`]: "
read MY_DOMAIN
[ -z "$MY_DOMAIN" ] && MY_DOMAIN=`hostname -d`

echo -n "Please specify current host name [`hostname -f`]: "
read STORM_BACKEND_HOST
[ -z "$STORM_BACKEND_HOST" ] && STORM_BACKEND_HOST=`hostname -f`

echo -n "Please specify NTP hosts IP addresses (divided by spaces) ['$NTP_HOSTS_IP_']: "
read NTP_HOSTS_IP
[ -z "$NTP_HOSTS_IP" ] && NTP_HOSTS_IP="$NTP_HOSTS_IP_"

echo -n "Size of /besfs storage (in GB, integer) [$STORM_BES_ONLINE_SIZE_]: "
read STORM_BES_ONLINE_SIZE
[ -z "$STORM_BES_ONLINE_SIZE" ] && STORM_BES_ONLINE_SIZE="$STORM_BES_ONLINE_SIZE_"

echo -n "SRM port [$STORM_FRONTEND_PORT_]: "
read STORM_FRONTEND_PORT
[ -z "$STORM_FRONTEND_PORT" ] && STORM_FRONTEND_PORT="$STORM_FRONTEND_PORT_"


echo -n "Port for secured authenticated WebDAV access (0 to disable) [$WEBDAV_HTTPS_PORT_]: "
read WEBDAV_HTTPS_PORT
[ -z "$WEBDAV_HTTPS_PORT" ] && WEBDAV_HTTPS_PORT="$WEBDAV_HTTPS_PORT_"

echo -n "Port for unsecured anonymous WebDAV access (0 to disable) [$WEBDAV_HTTP_PORT_]: "
read WEBDAV_HTTP_PORT
[ -z "$WEBDAV_HTTP_PORT" ] && WEBDAV_HTTP_PORT="$WEBDAV_HTTP_PORT_"



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
    myreplace "STORM_BE_XMLRPC_TOKEN=\"???\"" "STORM_BE_XMLRPC_TOKEN=$STORM_BE_XMLRPC_TOKEN" | \
    myreplace "STORM_FRONTEND_PORT=.*$" "STORM_FRONTEND_PORT=$STORM_FRONTEND_PORT" | \
    myreplace "STORM_BES_ONLINE_SIZE=\"???\"" "STORM_BES_ONLINE_SIZE=$STORM_BES_ONLINE_SIZE" \
  > "$MAIN_CONFIG"


chmod 750 $MAIN_CONFIG

echo
echo "Writing httpd configuration files for WebDAV (in $WEBDAV_CONF_DIR/)"

cp -r $WEBDAV_TMPL_DIR/* -t $WEBDAV_CONF_DIR

if [ "$WEBDAV_HTTPS_PORT" != "0" ]; then
    # Listening of port 443 is already enabled in standard mod_ssl config
    [ "$WEBDAV_HTTPS_PORT" == "443" ] && ignore443="#"

    cat "$WEBDAV_SECURED_TMPL" | \
        myreplace "<VirtualHost .*>" "<VirtualHost \*:$WEBDAV_HTTPS_PORT>" | \
        myreplace "^.*Listen .*$" "${ignore443}Listen $WEBDAV_HTTPS_PORT" | \
        myreplace "NameVirtualHost .*$" "NameVirtualHost \*:$WEBDAV_HTTPS_PORT" \
    > "$WEBDAV_SECURED_CONF"

fi

if [ "$WEBDAV_HTTP_PORT" != "0" ]; then
    cat "$WEBDAV_ANON_TMPL" | \
        myreplace "Listen .*$" "Listen $WEBDAV_HTTP_PORT" | \
        myreplace "<VirtualHost .*>" "<VirtualHost \*:$WEBDAV_HTTP_PORT>" \
    > "$WEBDAV_ANON_CONF"
fi


[ "$WEBDAV_HTTPS_PORT" == "0" ] && disable_https="#"
[ "$WEBDAV_HTTP_PORT" == "0" ]  && disable_http="#"

cat "$WEBDAV_HTTPD_TMPL" | \
    sed -r "s/^.*(Include .*\/secured.include)/$disable_https\1/" | \
    sed -r "s/^.*(Include .*\/anonymous.include)/$disable_http\1/" \
> "$WEBDAV_HTTPD_CONF"


echo
echo "To configure service, please run 'bash $SCRIPT_DIR/configure-service.sh'"
echo

