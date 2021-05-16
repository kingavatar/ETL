#!/bin/bash

cd backend
pipenv install
pipenv run python app.py &
pipenv run python ftpserver.py
cd ..
echo "Process is Running... kill python process manually."