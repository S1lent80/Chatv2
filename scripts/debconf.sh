#!/bin/bash

MAIN_DIR="/var/www/html/debs"
ARCH="amd64"
OS_TYPE="debian"
FULL_DIR="${MAIN_DIR}/${ARCH}/${OS_TYPE}"

# Check if the user is running in root
if [ "$(id -u)" != "0" ]; then
	echo -e "\n\033[31m[-]\033[0m\033[32m Please run this script in root...\033[0m\n" 2>&1
	exit 1
fi 

if [ -d "${FULL_DIR}" ]; then
	# Scan the package directories
	echo -e "\n\033[34m[*]\033[0m\033[32m Scanning packages in \"${ARCH}/${OS_TYPE}\"...\033[0m\n"
	dpkg-scanpackages ${FULL_DIR} | gzip -9c > "${FULL_DIR}/Packages.gz"
	if [[ $? != 1 ]]; then
		echo -e "\n\033[32mSuccess...\033[0m"
	else
		echo -e "\n\033[31m[-]\033[0m\033[32m Could not scan packages in \"${ARCH}/${OS_TYPE}\"...\033[0m\n"
		exit 1
	fi

	# Write to s1.list
	echo -e "\033[34m[*]\033[0m\033[32m Writing to /etc/apt/sources.list.d/s1.list...\033[0m"
	echo "deb http://127.0.0.1/debs amd64/debian/" > /etc/apt/sources.list.d/s1.list

	# Update the system
	apt-get update 
	if [[ $? != 1 ]]; then
		echo -e "\n\033[32mSuccess...\033[0m\n"
	else
		echo -e "\n\033[31m[-]\033[0m\033[32m Unable to update the system...\033[0m\n"
		exit 1
	fi
else
	echo -e "\n\033[31m[-]\033[0m\033[32m Could not find directory: ${FULL_DIR}...\033[0m\n"
	exit 1
fi
