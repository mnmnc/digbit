#!/bin/bash
 
for i in $( ./digbit.py $1);
do
        dotcheck=$( echo "$i" | grep "\." | wc -l)
        echo -n "$i ";
        check=$(nslookup $i| grep "NXDOMAIN" | wc -l);
        if [[ $check -ne 0 && dotcheck -ne 0 ]];
        then
                echo " < available";
        else
                echo " ";
        fi;
done