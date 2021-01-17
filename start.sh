#!/usr/bin/env bash
flask db upgrade
service nginx start
uwsgi --ini uwsgi.ini