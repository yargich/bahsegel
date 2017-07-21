#!/bin/bash
a ='pwd'

PATH= a:$PATH

export PATH

echo -e '\n#### Create Virtual Environment ####\n'

virtualenv -p /usr/bin/python2.7 --no-site-packages ~/.gamingtec_env


VIRTUAL_ENV_NAME='gt_env

virtualenv $VIRTUAL_ENV_NAME


echo -e '\n#### Activate Virtual Environment ####\n'
source $VIRTUAL_ENV_NAME/bin/activate


echo -e '\n#### Install requirements ####\n'
pip install -r requirements.txt


echo -e '#### Run tests ####\n'

python start.py

nosetests start_bahsegel.py --with-html
python -m webbrowser nosetests.html

echo ### deactivate virtual environment ###
deactivate