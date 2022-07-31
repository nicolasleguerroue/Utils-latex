#!/bin/bash


function WaitingNetwork() {
	while [[ -z `hostname -I` ]]; do
	echo "Waiting for network"
	sleep 2
	done
}

function NetworkIsAvailable() {
	if [[ -z `hostname -I` ]]; then
		#echo -e "déconnecté"
		echo 1
	else
		#echo -e "connecté"
		echo 0
	fi
}

function GetIp() {
	echo -e $(hostname -I)
}

