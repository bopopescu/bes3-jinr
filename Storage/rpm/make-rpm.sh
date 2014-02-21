#!/bin/sh

CONFIG_DIR=`dirname $0`
SPEC_FILE=storm-bes.spec

PACKAGE_NAME=`grep "%global packagename" ${CONFIG_DIR}/${SPEC_FILE} | cut -d ' ' -f 3`
VERSION=`cat ${CONFIG_DIR}/VERSION`
RELEASE=`cat ${CONFIG_DIR}/RELEASE`

TMP_DIR=`mktemp -d`

PACKAGE_DIRNAME=${PACKAGE_NAME}-${VERSION}
PAC_TMPDIR=${TMP_DIR}/${PACKAGE_DIRNAME}

mkdir ${PAC_TMPDIR}
cp -r ${CONFIG_DIR}/* ${PAC_TMPDIR}
find ${PAC_TMPDIR} -regex '/(\.svn|\.git)' | xargs rm -rf
tar -C ${TMP_DIR} -cz ${PACKAGE_DIRNAME} > $TMP_DIR/${PACKAGE_DIRNAME}.tar.gz

rpmbuild --define="VERSION ${VERSION}" --define="RELEASE ${RELEASE}" -ta $TMP_DIR/${PACKAGE_DIRNAME}.tar.gz

rm -rf ${TMP_DIR}

