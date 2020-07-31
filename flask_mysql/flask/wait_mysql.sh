#!/bin/sh

mysql_host=$1
mysql_port=$2
shift 2
cmd="$@"

# wait for the postgres docker to be running
while ! nc $mysql_host $mysql_port; do
  >&2 echo "Database is unavailable - sleeping"
  sleep 1
done

>&2 echo "Database is up"

# run the command
exec $cmd

