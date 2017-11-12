#!/bin/bash

## Setup script - Version: 1 ##

# Variables:System
ID="$(awk -F '=' '/^ID=/ {print $2}' /etc/os-release)"
ID_LIKE="$(awk -F '=' '/^ID_LIKE=/ {print $2}' /etc/os-release)"
# -> Colors
gs="\033[01;32m"
rs="\033[01;31m"
ys="\033[01;33m"
blue="\033[01;34m"
ce="\033[00m"
# -> Colors:Pattern
plus="${gs}[+]${ce} "
minus="${rs}[-]${ce} "
astk="${blue}[*]${blue} "


# Variables:Directories
opt_conf_main_dir="/opt/chat/config"


# Variables:Files
opt_conf_main_file="${opt_conf_main_dir}/dir_main.txt"


# Check if the user is in root
if [ "$(id -u)" != "0" ]; then
	echo -e "\n\033[01;31m[-]\033[00m\033[01;32m Please run this script as root...\033[00m\n" 2>&1
	exit 1
fi

# **********************************************************************************************
# Functions:Files
function writeConfigFile()
{
	if [ -f "$1" ]; then
		echo "$2" >> $1
	fi
}

# Generate the main ffiles and directories in the /opt directory
# -> /opt/chat
# -> /opt/chat/config
# -> /opt/chat/notes
# -> /opt/chat/config/dir_main.txt
function genMainDirectories()
{
	if [ -d ${opt_conf_main_dir} ]; then
		echo -e "${blue}=>${ce}${gs} Directory: \"${opt_conf_main_dir}\" exists..."
		if [[ -f ${opt_conf_main_file} ]]; then
			echo -e "${blue}=>${ce}${gs} File: \"${opt_conf_main_file}\" exists..."
			if [[ `grep ${HOME} ${opt_conf_main_file}` ]]; then
				echo "Variable \${HOME} exists in ${opt_conf_main_file}..."
			else
				echo "${HOME}" > ${opt_conf_main_file}
			fi
		else
			echo -e "${astk}${gs}Generating file: \"${opt_conf_main_file}\"..."
			if [[ -d ${opt_conf_main_dir} ]]; then
				touch ${opt_conf_main_file}
				echo "${HOME}" > ${opt_conf_main_file}
				if [[ "$?" != 1 ]]; then
					echo -e "${plus}${ys}Successfully generated file: \"${opt_conf_main_file}\"..."
				else
					echo -e "${minus}${gs}Could not generate file: \"${opt_conf_main_file}\"..."
					exit 1
				fi
			else
				mkdir ${opt_conf_main_dir}
				if [[ "$?" != 1 ]]; then
					touch ${opt_conf_main_file}
					echo "${HOME}" > ${opt_conf_main_file}
					if [[ "$?" != 1 ]]; then
						echo -e "${gs}Success...${ce}\n"
					else
						echo -e "\n${minus}${gs}Could not generate file: ${opt_conf_main_file}...${ce}\n"
					fi
				else
					echo -e "\n${minus}${gs}Could not create directory: ${opt_conf_main_dir}...${ce}\n"
				fi
			fi
		fi
	else
		echo -e "${astk}${gs}Creating directory: \"${opt_conf_main_dir}\"..."
		mkdir ${opt_conf_main_dir}
		if [[ "$?" != 1 ]]; then
			echo -e "${gs}=>${ce}${ys} Successfully created directory: \"${opt_conf_main_dir}\"...\n"
		else
			echo -e "\n${minus}${gs}Could not create directory: ${opt_conf_main_dir}...${ce}\n"
			exit 1
		fi
		echo -e "${astk}${gs}Creating file: \"${opt_conf_main_file}\"..."
		touch ${opt_conf_main_file}
		if [[ "$?" != 1 ]]; then
			echo -e "${gs}=>${ce}${ys} Successfully created file: \"${opt_conf_main_file}\"..."
			echo "${HOME}" > ${opt_conf_main_file}
		else
			echo -e "${minus}${gs}Could not create file: ${opt_conf_main_file}...\n"
			exit 1
		fi
	fi
}

# Get system information
function getSysInfo()
{
	
}

genMainDirectories
