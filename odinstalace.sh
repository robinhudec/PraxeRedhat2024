#!/bin/bash
echo "Do you want to uninstall $? ?"
read answer

if [[ $answer == "Y" || $answer == "y" ]]; then
	sudo dnf erase $?
elif [[ $answer == "n" || $answer == "N" ]]; then 
	echo "$? was not removed"

fi
