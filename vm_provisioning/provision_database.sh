#!/usr/bin/env bash
echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== PROVISION DATABASE ============================="
echo "==============================================================="
echo -e "\n\n\n\n\n"

# Prepare database
echo "============== Prepare Postgresql database ===================="
sudo -u postgres -i psql postgres -c "CREATE DATABASE magazin_online WITH ENCODING='UTF8' TEMPLATE=template0 LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8';"
sudo -u postgres -i psql postgres -c "CREATE USER iteamdev WITH PASSWORD 'dragos';"
sudo -u postgres -i psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE magazin_online TO iteamdev;"
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

sudo -u postgres -i service postgresql restart
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== FINISHED PROVISIONING DATABASE ================="
echo "==============================================================="
echo -e "\n\n\n\n\n"
