* Create a virtual environment
py -m venv env

* Exit from the virtual environment
deactivate

* Activate virtual environment
./env/Scripts/activate.ps1

* Test virtual enviroment
Test-Path env:VIRTUAL_ENV

* Install packages
pip install pytest requests lxml

* Run tests
py -m pytest

* The book to learn automation with pytest
https://blog.testproject.io/2019/07/16/python-test-automation-project-using-pytest/