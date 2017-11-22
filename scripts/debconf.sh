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
	dpkg-scanpackages ${FULL_DIR} | gzip -9c > ${FULL_DIR}/Packages.gz
	if [[ $? != 1 ]]; then
		echo -e "\n\033[32mSuccess...\033[0m\n"
	else
		echo -e "\n\033[31m[-]\033[0m\033[32m Could not scan packages in \"${ARCH}/${OS_TYPE}\"...\033[0m\n"
		exit 1
	fi

	# Write to s1.list
	echo -e "\033[34m[*]\033[0m\033[32m Writing to /etc/apt/sources.list.d/s1.list...\033[0m"
	if [[ -f "/etc/apt/sources.list.d/s1.list" ]]; then
		echo -e "\n\033[32mApt file: s1.list exists...\033[0m"
		if [[ `grep "deb http://127.0.0.1/debs amd64/debian/" /etc/apt/sources.list` ]]; then
			echo -e "\033[32mRepository URL exists in /etc/apt/sources.list...\033[0m\n"
		else
			# Prompt the user
			echo -e "\n"
			read -p "Add the s1 repo to /etc/apt/sources.list? [Y|y|N|n]: " choice
			if [[ ${choice} == "Y" ]] || [[ ${choice} == "y" ]]; then
				echo "deb http://127.0.0.1/debs amd64/debian/" >> /etc/apt/sources.list
			elif [[ ${choice} == "N" ]] || [[ ${choice} == "n" ]]; then
				echo -e "\n\033[32mNot adding s1 repo to /etc/apt/sources.list...\033[0m\n"
			else
				echo ""
			fi
		fi
	else
		# echo "deb http://127.0.0.1/debs amd64/debian/" > /etc/apt/sources.list.d/s1.list
		if [[ `grep "deb http://127.0.0.1/debs amd64/debian/" /etc/apt/sources.list` ]]; then
			echo -e "\033[32mRepository URL exists in /etc/apt/sources.list...\033[0m\n"
		else
			echo "deb http://127.0.0.1/debs amd64/debian/" >> /etc/apt/sources.list
		fi
	fi

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
