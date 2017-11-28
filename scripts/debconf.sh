#!/bin/bash

QUIET=0

## Dir variables ##
REPO_DIR="/var/www/html/s1"
OS_TYPE="debian"
ARCH="amd64"
DIR_FULL="${REPO_DIR}/${OS_TYPE}/${ARCH}"

## Variables ##
gs="\033[32m"
rs="\033[31m"
ys="\033[33m"
blue="\033[34m"
ce="\033[0m"
# -> Patterns
plus="${gs}[+]${ce} "
minus="${rs}[-]${ce} "
astk="${blue}[*]${ce} "

# Check if the user is in root
if [ "$(id -u)" != "0" ]; then
	echo -e "\n${minus}${gs}Please run this script as root...${ce}\n" 2>&1
	exit 1
fi

## Main program ##
if [ -d ${REPO_DIR} ] && [ -d ${DIR_FULL} ]; then
	echo -e "${astk}${gs}Found directory: ${DIR_FULL}...${ce}"
	echo -e "${astk}${gs}Writing to: ${DIR_FULL}/Packages.gz...${ce}\n"
	cd ${REPO_DIR}; dpkg-scanpackages ${OS_TYPE}/${ARCH} | gzip -9c > ${OS_TYPE}/${ARCH}/Packages.gz
	# dpkg-scanpackages ${DIR_FULL} | gzip -9c > ${DIR_FULL}/Packages.gz
	if [[ $? != 1 ]]; then
		echo -e "\n${plus}${ys}Success...${ce}"
	else
		echo -e "\n${minus}${gs}Could not write to: ${DIR_FULL}/Packages.gz...${ce}\n"
		exit 1
	fi
	
	# Check if entry is already present in /etc/apt/sources.list
	if [[ -f "/etc/apt/sources.list.d/s1.list" ]]; then
		echo -e "${astk}${gs}File \"s1.list\" exists in /etc/apt/sources.list.d...${ce}"
	else
		echo -e "${astk}${gs}Adding file \"s1.list\" to /etc/apt/sources.list.d...${ce}"
		echo "deb [trusted=true] http://127.0.0.1/s1 debian/amd64/" > /etc/apt/sources.list.d/s1.list
	fi
	
	# Update the system
	echo -e "${astk}${gs}Updating the system...${ce}"
	
	# Check quiet mode boolean
	if [[ ${QUIET} == 1 ]]; then
		apt-get -qq update
	else
		apt-get update
	fi
	
	if [[ $? != 1 ]]; then
		echo -e "\n${gs}Success...${ce}\n"
	else
		echo -e "\n${minus}${gs}Could not update system...${ce}\n"
		exit 1
	fi
else
	echo -e "\n${minus}${gs}Could not find directory: ${DIR_FULL}...${ce}\n"
	exit 1
fi

