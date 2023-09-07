#!/bin/bash
confirm(){
	echo "Do you want to uninstall Emacs?"
	read answ 
	if [[ $answ == "N" || $answ == "n" ]]; then
		return 1
	else
		return 0
	fi
}
rpm -q emacs
if [[ $? == 1 ]]; then
	sudo dnf install -y emacs
	answ=$(confirm)
	echo $answ
	if [[ $answ == 0 ]]; then
		sudo dnf erase -y emacs
	fi
else
	sudo dnf erase -y emacs
fi

