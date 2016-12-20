#!/usr/bin/env bash

echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== RUN SERVER ====================================="
echo "==============================================================="
echo -e "\n\n\n\n\n"

# Set environment params
echo "============== Set environment parameters ====================="
export WORKON_HOME=~/virtualenvs/
source /usr/local/bin/virtualenvwrapper.sh
export PIP_VIRTUALENV_BASE=~/virtualenvs
export ITEAM_PLATFORM=LOCAL
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Go to the sources folder
echo "============== Change folder to /var/www/new_XPC_ITO/src ======"
workon iteam
cd /var/www/iteam_magazin_online/src
pwd
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Install requirements for running the application
echo "============== Install project requirements ==================="
pip install -r requirements/local.txt
echo -e "\n\n\n Done..."
echo -e "\n\n\n\n\n"

# Collect static
echo "============== Collect static files ==========================="
./manage.py collectstatic --noinput
./manage.py compress --force
echo -e "\n\n\nDone..."
echo -e "\n\n\n\n\n"


echo "============== Restora database ==========================="
echo -e "\n\n\nDone..."
echo -e "\n\n\n\n\n"

# Run server
echo "============== Start server ==================================="
echo "Use \"vagrant ssh\" to login to the VM"
echo "Run the following commands to start server"
echo ""
echo "1. cd /var/www/iteam_magazin_online/src"
echo "2. workon iteam"
echo "3. ./manage.py runserver 0.0.0.0:8000"
echo "3. open browser on your PC and access URL 192.168.33.12:8000"
echo "4. compress file css and js ./manage.py compress"
echo -e "\n\n\n\n\n"
echo "==============================================================="
echo "============== SERVER STARTED ================================="
echo "==============================================================="
echo -e "\n\n\n\n\n"
