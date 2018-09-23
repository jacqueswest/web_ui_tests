# Setup Guide

## Install Python 3:
Select the latest version from:
    
    
    https://www.python.org/downloads/
    
    
**NB:** For Windows ensure you tick set python path during installation.

## Clone API Test GIT Repository:
    git clone https://github.com/jacqueswest/api_tests.git
    
## Install Required Python Packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
## Executing Tests:
From the root of the repository, run:

    pytest

## Output Example:
    tests/test_get_dog_breeds.py::test_get_all_breeds PASSED                                                             [ 25%]
    tests/test_get_dog_breeds.py::test_verify_retriever_breed PASSED                                                     [ 50%]
    tests/test_get_dog_breeds.py::test_get_retriever_sub_breeds PASSED                                                   [ 75%]
    tests/test_get_dog_breeds.py::test_get_random_image_golden_retriever PASSED                                          [100%]

## Viewing Test Report:            
  A report called **_api_report.html_** will be created in the root of the repository after test execution.
  
  Copy the full path of the report and open it in a browser or in a HTML viewer to view the report.
  
  Example of API HTML test report:
  
    Passed	tests/test_get_dog_breeds.py::test_get_all_breeds	0.91	
    ----------------------------- Captured stdout call -----------------------------
    {'message': {'affenpinscher': [],
                 'african': [],
                 'airedale': [],
                 'akita': [],
                 'appenzeller': [],
                 'basenji': [],
                 'beagle': [],
                 'bluetick': [],
                 'borzoi': [],
                 'bouvier': [],
                 'boxer': [],
                 'brabancon': [],
                 'briard': [],
                 'bulldog': ['boston', 'french'],
                 'bullterrier': ['staffordshire']......
        
