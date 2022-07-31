#!/bin/bash


function createDirectory {
	directory="$1"
	if [ -z "$directory" ]; then
		echo -e "$red"
 		echo -e "Please, give a folder name in argument of createDirectory function !"
		echo -e "$default"
	else
		if [ ! -d "$directory" ];then
			echo -e "$green>>> Directory '${directory}' has been created !$default"
			mkdir $directory 
        else 
            echo -e ">>> Directory '${directory}' exists !"
		fi
	fi
}
#$1 = filename, $2=default content, $1=boolean on escape char
function createFile 
{
	file=$1
	defaultContent=$2
	escapeChar=$3
	ignoreEscapeChar=0
	if [ -z "$escapeChar" ]; then
		ignoreEscapeChar=0
	else
		ignoreEscapeChar=1
	fi
	if [ -z "$file" ]; then
		echo -e "$red"
 		echo -e "Please, give a filename in argument of createFile function !"
		echo -e "$default"
		exit
	fi

	if [ -z "$defaultContent" ]; then
		echo -e "$red"
 		echo -e "Please, give a default content in argument of createFile function !"
		echo -e "$default"
		exit
	fi

	if [[ ! -f $file ]];then
		touch $file
		echo -e "$green >>> File '${file}' has been created ! $default"
		if [[ $ignoreEscapeChar == "0" ]];then
			echo -e "$defaultContent" > $file
		else
			echo "$defaultContent" > $file
		fi
	else
		echo -e ">>> File '${file}' exists"
	fi
}