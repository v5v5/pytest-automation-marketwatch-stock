* Install package virtualenv
py -m pip install virtualenv

* Creating a virtual environment
py -m venv env

* Exiting from the virtual environment
deactivate

* Activate virtual environment
./env/Scripts/activate.ps1

* Test virtual enviroment
Test-Path env:VIRTUAL_ENV

* Install used packages
pip install requests
pip install lxml

* Run tests
python -m pytest

* The book to learn automation with pytest
https://blog.testproject.io/2019/07/16/python-test-automation-project-using-pytest/