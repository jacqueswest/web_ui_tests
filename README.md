# Setup Guide

## Install Python 3:
Select the latest version from:
    
    
    https://www.python.org/downloads/release/python-370
For Windows select _Windows x86 executable installer_

For MAC OS, click on the _download button_
        
**NB:** For Windows ensure you tick **_Add Python 3.7 to PATH_** during installation

## Verify Python and pip installation
From _cmd_ or _bash prompt_, execute:

    python --version
        Output example: Python 3.7
    pip --version
        Output example: /Users/mac/project/lib/python3.7/site-packages/pip (python 3.7)

If you experience any problems see section _Python and pip path tips for windows_


## NB: Python and pip path tips for windows
If you have issues executing python and/or pip in git bash prompt then use windows native cmd.

If pip application can't still not be found, add pip path to the environment variables.

Find python 3 installation folder and under it you should find the scripts folder, add this scripts path to environment variables, see below possible path:

    C:\Users\{UserAccountName}\AppData\Local\Programs\Python\Python37-32\Scripts
    

## Upgrade PIP(_Python package manager_)
From _cmd_ or _bash prompt_, execute:

    python -m pip install --upgrade pip

## Install GIT(_If not installed_)
For Windows:
    
    https://git-scm.com/download/win
    
For MAC OS following the guide under _Installing for MAC_:
    
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    

## Clone WEB UI Test GIT Repository:
    git clone https://github.com/jacqueswest/web_ui_tests.git
    
## Download Chrome driver:
Download chrome driver and unzip in the root of the repository:
    
    https://chromedriver.storage.googleapis.com/index.html?path=2.42/    

## Set the chrome path in user_data.json:
This is the path to the chrome browser installed.

**NB:** For windows paths use double backslashes(\\\\) in the path

Windows possible chrome path: _C:\\\Program Files (x86)\\\Google\\\Chrome\\\Application\\\chrome.exe_

Mac OS possible chrome path: _/Applications/Google Chrome.app_

Edit **_/test_data_lib/user_data.json_** with the chrome path:

    {
    "locator_data": {
        "chrome_path": "PASTE CHROME PATH",
    
    
## Install Required Python Packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
## Executing Tests:
From the root of the repository, run:

    pytest

## Output Example:
    tests/test_add_users.py::test_verify_landing_on_user_list_table PASSED                                               [ 33%]
    tests/test_add_users.py::test_can_add_user_one PASSED                                                                [ 66%]
    tests/test_add_users.py::test_can_add_user_two PASSED                                                                [100%]


## Viewing Test Report:            
  A report called **_web_ui_tests_report.html_** will be created in the root of the repository after test execution.
  
  Copy the full path of the report and open it in a browser or in a HTML viewer to view the report.
  
  Example of WEB UI HTML test report:
  
    Result	Test	Duration	Links
    Passed	tests/test_add_users.py::test_verify_landing_on_user_list_table	0.03	
    Passed	tests/test_add_users.py::test_can_add_user_one	2.18	
    Passed	tests/test_add_users.py::test_can_add_user_two	1.94
        
