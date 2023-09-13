#!/bin/bash
for i in {1..100}; do
	sudo useradd $1$i
	echo -e "heslo\nheslo" | passwd $1$i &> /dev/null
done

for i in {1..100}; do
	id $1$i &> /dev/null
	if [[ $? == 1  ]]; then
		echo "uzivatel $1$i neexistuje"
	else
		echo "uzivatel $1$i existuje"
	fi

done

grep -e "alice[[:alnum:]]*[2]" /etc/passwd


for i in {1..100}; do
	sudo userdel $1$i
done

for i in {1..100}; do
        id $1$i &> /dev/null
        if [[ $? == 1  ]]; then
                echo "uzivatel $1$i neexistuje"
        else
                echo "uzivatel $1$i existuje"
        fi

done

