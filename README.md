
# These are the instructions to run this test application.

1. Clone the jukin_pytest project from Github to your machine.
2. Ensure that Python is installed on your machine and that python environment variable is set correctly in path.
3. Ensure that grails application server is running.
4. Goto the project folder and run command 'venv\scripts\activate.bat' in order to activate the virtual environment (for windows machines) and for linux or mac use (source venv/bin/activate)
5. Now the vertualenv is activated. Run command (pytest --browser chrome --url "http://localhost:8080/WhatChaMaCallIt/login"  --html=./report/report.html)
6. my framework currently support three browser connfiguration namely chrome, firefox and iexplorer (just replace the chrome with other options)
7. After test execution, please navigate to report directory and open the report.html
8. this report contains all the details related to this execution that is number of testcases passed and failed with detailed explaination.
