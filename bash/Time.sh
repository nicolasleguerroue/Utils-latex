#!/bin/bash

GetTime() {
	echo -e "$(date +%H):$(date +%M):$(date +%S) $(date +%d)/$(date +%m)/$(date +%y)"
}

GetYear() {
	echo -e $(date +%y)
}

GetMonth() {
	echo -e $(date +%m)
}

GetDay() {
	echo -e $(date +%d)
}

GetHour() {
	echo -e $(date +%H)
}

GetMinute() {
	echo -e $(date +%M)
}

GetSeconde() {
	echo -e $(date +%S)
}