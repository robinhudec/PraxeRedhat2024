#!/bin/bash
if [[ $1 == "" ]]; then 
	exit 1
fi

rpm -q $1
if [[ $? == 1 ]]; then
	sudo dnf install -y $1
	if [[ $? == 1 ]]; then
		sudo dnf erase -y $1
	fi
else
	sudo dnf erase -y $1
fi

