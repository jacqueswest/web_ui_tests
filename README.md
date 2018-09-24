# Setup Guide

## Install Python 3:
Select the latest version from:
    
    
    https://www.python.org/downloads/release/python-370
For Windows select _Windows x86 executable installer_

For MAC OS, click on the _download button_
        
**NB:** For Windows ensure you tick set python path during installation.

## Upgrade PIP(Python package manager)
From _cmd_ or _bash prompt_, execute:

    python -m pip install --upgrade pip

## Install GIT(If not installed)
For Windows:
    
    https://git-scm.com/download/win
    
For MAC OS following the guide under _Installing for MAC_:
    
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    

## Clone API Test GIT Repository:
    git clone https://github.com/jacqueswest/web_ui_tests.git
    
## Download Chrome driver:
Download chrome driver and unzip in the root of the repository:
    
    https://chromedriver.storage.googleapis.com/index.html?path=2.42/    

## Set the chrome path in user_data.json:
This is the path to the chrome browser installed.

Windows possible chrome path: 

Mac OS possible chrome path: /Applications/Google Chrome.app

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
  
  Example of API HTML test report:
  
    Result	Test	Duration	Links
    Passed	tests/test_add_users.py::test_verify_landing_on_user_list_table	0.03	
    Passed	tests/test_add_users.py::test_can_add_user_one	2.18	
    Passed	tests/test_add_users.py::test_can_add_user_two	1.94
        
