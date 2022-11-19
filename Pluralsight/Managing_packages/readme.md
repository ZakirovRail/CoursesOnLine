To get know which version of PIP is used:
$ pip -V


To list all installed packages:
$ pip list
To list all installed packages with info about latests available versions
$ pip list -o

To remove a package:
$ pip uninstall urllib3 chardet idna

Get help documentation:
$ pip -help


To get info about package:
$ pip show six

To get info what in the PATH variable:
$ python
$ import sys
$ sys.path


Install a package for the specific Python version:
$ python2 -m pip install flask
$ python2.7 -m pip install flask


Create local virtual environment "rates" or "rates_py3" with virtualenv:
$ python -m pip install virtualenv
$  cd ../..
$ mkdir virtualenvs
$ cd virtualenvs
$ virtualenv rates   OR virtualenv -p python3 rates_py3
enable/activate virtual environment (MacOS)
$  source rates/bin/activate
deactivate env:
$ deactivate

Create local virtual environment "rates" with venv:
$ python -m venv rates
activate:
$ . rates/bin/activate



Create a list of packages required for installation:
$ python -m pip freeze > requirements.txt

Install all packages from requirements.txt file
$ python -m pip install -r requirements.txt


Install specific version of package via pip:
$ docopt == 0.6.1
$ keyring >= 4.1.1
$ coverage != 3.5
$ python -m pip install docopt==0.6.1
$ python -m pip install 'Django<2.0'

Upgrade to latest version:
$ python -m pip install -U flask

Upgrade pip itself:
$ python -m pip install -U pip


VIRTUALENVWRAPPER
Install to Linux or MAcOS:
$ sudo pip3 install virtualenvwrapper

determine where installed virtualenvwrapper:
$ which virtualenvwrapper.sh

add virtualenvwrapper to profile file
$ nano .profile
add to profile
$ source <path to virtualenvwrapper>/virtualenvwrapper.sh
reload sh (restart PC)

add to the profile file location of venv's
$ export WORKON_HOME="/home/<path_to_venv>/venv"
restart shell

to get a list of venv:
$ workon

to run a venv:
$ workon <venv_name>

to set a PROJECT_HOME into profile:
$ nano .profile
$ export PROJECT_HOME="/home/<path>/dev" 

create a new project (create a new venv):
$ mkproject new_project

if you want to bind your project location and venv, then:
1. go to project location
2. activate venv
3. run command $setvirtualenvproject



Create a virtualenv:
$ mkvirtualenv new_env

Remove a virtualenv:
$ rmvirtualenv some_env

if you cannot to find virtualenvwrapper.sh, then:
run $ pip3 uninstall virtualenvwrapper
it will show you where virtualenvwrapper.sh file is 

reload your profile file:
$ source ~/.bash_profile



for me it was like:
#settings for virtualenvwrapper
export WORKON_HOME="/Users/Rail.zakirov/.virtualenvs/"
source /Library/Frameworks/Python.framework/Versions/3.9/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_PYTHON="/usr/local/bin/python3"
export VIRTUALENVWRAPPER_VIRTUALENV="/Users/Rail.zakirov/virtualenvs"
