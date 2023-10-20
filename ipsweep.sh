#!/usr/bin/bash

if [ "$1" == "" ]
then
	echo "You forgot an IP address!"
	echo "Syntax: ./ipsweep.sh 192.168.1"

else
	for range in `seq 1 254`; do
		ping $1.$range -c 1 | grep "64 bytes" | cut -f 4 -d " " | tr -d ":" &
	done

fi
