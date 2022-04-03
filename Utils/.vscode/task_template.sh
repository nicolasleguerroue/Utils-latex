#!/bin/bash
file=$1
echo -e "Task template generation : start"
echo -e "Reading $file file"

##global settings
version="2.0.0"
defaultColor="white"
loadNpmCommands=false
reloadButton=♻️


arrayLabels=()

#Parsing
while IFS= read -r line
do
	if [[ `echo $line | grep \#\#` != "" ]]; then
		#echo -e "Header settings found"

		foundVersion=`echo $line | grep version | cut -d '=' -f2`
		foundDefaultColor=`echo $line | grep defaultColor | cut -d '=' -f2`
		foundLoadNpmCommands=`echo $line | grep loadNpmCommands | cut -d '=' -f2`
		foundReloadButton=`echo $line | grep reloadButton | cut -d '=' -f2`


		if [[ $foundVersion != "" ]];then
			version=$foundVersion
		fi
		if [[ $foundDefaultColor != "" ]];then
			defaultColor=$foundDefaultColor
		fi
		if [[ $foundLoadNpmCommands != "" ]];then
			loadNpmCommands=$foundLoadNpmCommands
		fi
		if [[ $foundReloadButton != "" ]];then
			reloadButton=$foundReloadButton
		fi

	elif [[ `echo $line | grep \#` != "" ]];then
		arrayLabels+="`echo $line | cut -d ',' -f1 | cut -d '=' -f2`"
	fi


done < $file

for i in "${arrayLabels[*]}"; do echo "$i -- \n"; done

echo -e "Version : "$version
echo -e "Default color : "$defaultColor
echo -e "Load NPM commands : "$loadNpmCommands
echo -e "Reload buttons icon : "$reloadButton

