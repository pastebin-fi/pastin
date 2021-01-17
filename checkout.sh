#!/bin/bash

if git checkout "$1" ; then
    if [ "$1" == "master" ]; then
        sed "s/DB = pastin\(.*\)/DB = pastin/" config.ini > config.ini.new
    else
        sed "s/DB = pastin\(.*\)/DB = pastin_$1/" config.ini > config.ini.new
    fi
    mv config.ini.new config.ini
fi
