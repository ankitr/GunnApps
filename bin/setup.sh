#!/usr/bin/bash

echo "Setting up the GunnApps environment."
echo "Assumes you are in the GunnApps root directory."

echo "sudo pip install virtualenv"
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
echo "pip install -r requirements.txt"
echo "Setup complete."
