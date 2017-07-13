#!/bin/bash
a ='pwd'

PATH= a:$PATH

export PATH

echo -e '\n#### Create Virtual Environment ####\n'

virtualenv -p /usr/bin/python2.7 --no-site-packages ~/.gamingtec_env


VIRTUAL_ENV_NAME='.gamingtec_env

virtualenv $VIRTUAL_ENV_NAME


echo -e '\n#### Activate Virtual Environment ####\n'
source $VIRTUAL_ENV_NAME/bin/activate


echo -e '\n#### Install requirements ####\n'
pip install -r requirements.txt


echo -e '#### Run tests ####\n'

python start.py

#nosetests --with-html --html-report=nose_report_test.html

echo ### deactivate virtual environment ###
deactivate