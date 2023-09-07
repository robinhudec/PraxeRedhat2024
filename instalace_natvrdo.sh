#!/bin/bash
rpm -q emacs
if [[ $? == 1 ]]; then
	sudo dnf install -y emacs
	sudo dnf erase -y emacs
else
	sudo dnf erase -y emacs
fi

