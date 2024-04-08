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
  apt update >> $logfile  	#Update repositories cache
  apt upgrade -y >> $logfile  	#Upgrade packages
  apt install apt-utils -y >> $logfile
  apt install nano -y >> $logfile
}

#Installation of Docker if using Baremetal
function install_enable_docker() {
  ##Docker
  apt install docker -y >> $logfile			#Install Docker
  systemctl start docker.service >> $logfile	#Start Docker service
  systemctl enable docker.service >> $logfile	#Enable Docker service
  docker_version=$(sudo docker version)
  echo "Docker version isntalled: $docker_version " >> $logfile
}

#Installation of I2C tools. 
function install_i2c_tools() {
  apt install i2c-tools -y >> $logfile
  apt install libi2c-dev -y >> $logfile
}

#Installation of Python tools
function install_python_tools() {
  apt install python3 -y >> $logfile
  apt install python3-smbus -y >> $logfile
}


pushd /tests/logs/
update_upgrade
install_i2c_tools
install_python_tools

#Appending date to logfile name
mv $logfile ${logfile}_${formatdate}
popd
