#!/bin/bash
set -x

##Script to prepare Manjaro for PinePhone to use with the PineEye
##Installation log file "log_file" gets created in logs/

mkdir -p /tests/logs/				#Directory to save logs
logfile="log_file"		#File to be used to log installation process

pushd /tests/logs/
formatdate=$(date +"%m_%d_%Y_%R")
date -u > $logfile
popd

#Update and upgrade system packages
function update_upgrade() { 	
  sudo pacman -Syy >> $logfile  	#Update repositories cache
#  sudo pacman -Syu -y >> $logfile  	#Upgrade packages
}

#Installation of Docker if using Baremetal
function install_enable_docker() {
  ##Docker
  sudo pacman -S docker -y >> $logfile			#Install Docker
  sudo systemctl start docker.service >> $logfile	#Start Docker service
  sudo systemctl enable docker.service >> $logfile	#Enable Docker service
  docker_version=$(sudo docker version)
  echo "Docker version isntalled: $docker_version " >> $logfile
}

#Installation of I2C tools. 
function install_i2c_tools() {
  sudo pacman -S i2c-tools -y >> $logfile
}

#Installation of Python tools
function isntall_python_tools() {
  sudo pacman -S python-smbus -y >> $logfile
}


pushd /tests/logs/
update_upgrade

#Appending date to logfile name
mv $logfile ${logfile}_${formatdate}
popd
