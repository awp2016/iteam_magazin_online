#!/usr/bin/env bash

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== PROVISION BASIC SERVER ========================="
echo "==============================================================="
echo -e "\n\n\n\n\n"

# Update apt-get
echo "============== Update apt-get ================================="
sudo apt-get update
echo -e "\n\n\n Done update apt-get update"
echo -e "\n\n\n\n\n"

# Generate en_us.UTF-8 locale and set it default
echo "============== Generate en_US.UTF-8 locale - Set it default ==="
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
sudo update-locale LANG=en_US.UTF-8 LC_ALL=\"en_US.UTF-8\"
echo -e "\n\n\n Done set default locale to en_US.UTF-8"
echo -e "\n\n\n\n\n"

# Install pre-requirements - here more packages may be added - apache2, git, vim, mc
echo "============== Installing pre-requirements ===================="
sudo apt-get install -y libjpeg-dev python-dev python3-dev software-properties-common python-software-properties
sudo apt-get -y autoremove
echo -e "\n\n\n Done installing pre-requirements"
echo -e "\n\n\n\n\n"

# Add required configs to user's .profile
echo "============== Update current user profile ===================="
if ! grep -Fq "WORKON_HOME" ~/.profile; then
  echo export LC_ALL=en_US.UTF-8 >> ~/.profile
  echo export LANG=en_US.UTF-8 >> ~/.profile
  echo export LANGUAGE=en_US.UTF-8 >> ~/.profile
fi

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
echo -e "\n\n\n Done update current user profile"
echo -e "\n\n\n\n\n"

# Symlink /var/www -> vagrant sync folder
echo "============== Symlink /var/www -> vagrant ===================="
sudo rm -rf /var/www/iteam_magazin_online
sudo rm -rf /var/www
sudo mkdir /var/www
sudo ln -fs /vagrant/ /var/www/iteam_magazin_online
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Install Postgresql version 9.3 - will run on default port 5432 and will create automatically the user postgresql
echo "============== Installing Postgresql 9.3 ======================"
sudo apt-get install -y postgresql postgresql-server-dev-9.3
echo -e "\n\n\n Done installing Postgresql 9.3"
echo -e "\n\n\n\n\n"

# Changes in postgresql - listen to all interfaces
echo "============== Copy configuration file and restart it ========="
sudo cp /vagrant/vm_provisioning/os_files/postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
sudo -u postgres -i service postgresql restart
echo -e "\n\n\ Done..."
echo -e "\n\n\n\n\n"

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== FINISHED PROVISIONING BASIC SERVER ============="
echo "==============================================================="
echo -e "\n\n\n\n\n"
