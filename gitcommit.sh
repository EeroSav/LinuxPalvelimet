#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Add commit message"
else
	git pull origin main
	git add .
	git commit -m "$1"
	git push origin main
fi
