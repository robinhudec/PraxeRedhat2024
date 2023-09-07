#!/bin/bash
text="passwd"
while read -r line; do 
	user=$(echo "$line"|cut -d":" -f3)
	bash=$(echo "$line"|cut -d":" -f7)
	name=$(echo "$line"|cut -d":" -f1)
	echo $name" "$bash" "$user
done < $text
