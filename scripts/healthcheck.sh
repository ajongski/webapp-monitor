#!/bin/bash

sleep 5

while true
do 
    start=`date +%s`
    cmd=$(curl web:5000/healthcheck)
    end=`date +%s`

    runtime=$((end-start))

    echo $runtime

    if [ $cmd == "healthy" ]
    then
        echo "healthy"
    elif [ $runtime > 10]
    then
        python /scripts/smtp.py
    else
        python /scripts/smtp.py
    fi
    sleep 60
done
