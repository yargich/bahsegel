#!/bin/bash
#PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
#if [ ! -d "venv" ]; then
#        virtualenv venv
#fi
#. venv/bin/activate
#virtualenv -p /usr/bin/python2.7 gt_env

#a ='pwd'
#PATH= a:$PATH
#export $PATH
#echo -e '\n#### Create Virtual Environment ####\n'
#VIRTUAL_ENV_NAME='/gt_env'
#virtualenv -p /usr/bin/python2.7 --no-site-packages $VIRTUAL_ENV_NAME
#virtualenv $VIRTUAL_ENV_NAME
#echo -e '\n#### Activate Virtual Environment ####\n'

#alias activate =" . gt_env/bin/activate"
#activate
#echo -e '\n#### Install requirements ####\n'
#pip install -r requirements.txt
#echo -e '#### Run tests ####\n'
python start_bahsegel_chrome.py
#open -a "Google Chrome" nosetests.html
#echo -e '\n#### deactivate virtual environment ####\n'
#deactivate
