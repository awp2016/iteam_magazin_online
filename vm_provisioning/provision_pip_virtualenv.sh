#!/usr/bin/env bash

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== PROVISION PIP AND VIRTUAL ENVIRONMENT =========="
echo "==============================================================="
echo -e "\n\n\n\n\n"

# Install pip
echo "============== Installing Python PIP =========================="
sudo apt-get install -y python-pip
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Install virtual environment
echo "============== Installing Virtual Environment ================="
cd ~
sudo pip install virtualenv virtualenvwrapper
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Add required configs to user's .profile
echo "============== Update current user profile ===================="
if ! grep -Fq "WORKON_HOME" ~/.profile; then
  echo export WORKON_HOME=~/virtualenvs/ >> ~/.profile
  echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.profile
  echo export PIP_VIRTUALENV_BASE=~/virtualenvs >> ~/.profile
  echo export ITEAM_PLATFORM=LOCAL >> ~/.profile

  source ~/.profile
fi
echo -e "\n\n\n Done update current user profile"
echo -e "\n\n\n\n\n"

# Set environment params
echo "============== Set environment parameters ====================="
export WORKON_HOME=~/virtualenvs/
source /usr/local/bin/virtualenvwrapper.sh
export PIP_VIRTUALENV_BASE=~/virtualenvs
export ITEAM_PLATFORM=LOCAL
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Create virtual environemnt and work on it
echo "============== Create Virtual environment and Work on it ======"
cd ~
mkvirtualenv --python=/usr/bin/python3 iteam
workon iteam
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Symlink /var/www -> vagrant sync folder
echo "============== Symlink /var/www -> vagrant ===================="
sudo rm -rf /var/www/iteam_magazin_online
sudo rm -rf /var/www
sudo mkdir /var/www
sudo ln -fs /vagrant/ /var/www/iteam_magazin_online
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Mark manage.py as executable
echo "============== Mark file manage.py as executable =============="
sudo chmod +x /var/www/iteam_magazin_online/src/manage.py
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== FINISHED PROVISIONING PIP-VIRTUAL ENVIRONMENT =="
echo "==============================================================="
echo -e "\n\n\n\n\n"
