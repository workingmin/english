#!/usr/bin/bash

TEMP=`getopt -o f: --long file:,not -- "$@"`
eval set -- "$TEMP"

not=0
while true ; do
    case "$1" in
        -f|--file)
            file=$2 ; shift 2 ;;
        --not)
            not=1 ; shift ;;
        --) shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done

while read line
do
    s=`eval echo "$line"`
    if [[ $s =~ ^[a-zA-Z]+$ ]]; then
        if [ $not -eq 0 ]; then
            echo $s
        fi
    elif [ $not -eq 1 ]; then
        echo $s
    fi
done < $file