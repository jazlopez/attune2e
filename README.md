# Selenium e2e AttuneNxt

e2e test suite for AttuneNxt

## Getting Started


### Prerequisites

* Verify you have Python 2.7 and PIP installed before proceed to installation step.

```
which python

which pip
```

If you receive python/pip not found see the links below to install missing pre-requisites.

* [Python](https://www.python.org/downloads/)
* [PIP](https://pip.pypa.io/en/stable/installing/)  


```
pip install -r requirements.txt
```

### Installing

1. Install required packages (Selenium, Colorama) via PIP.

    See the below.
    ```
    pip install -r requirements.txt
    ```

2. Copy config.py.dist to config.py and replace configuration values as required.

    ```
    "url": {
        "login": "",    # where to login
        "homepage": "", # landing page (after login)
        "webdriver": "" # e.g, http://localhost:4444/wd/hub
        },
        "username": "", # login name
        "password": ""  # login password
    }
    ```
    
## Running the tests

Launch a terminal and execute test suite.

    python e2e.py

### Test Cases
---


1. Levey-Jennings-User-Login

2. Levey-Jennings-Default-Landing-Page

3. Levey-Jennings- Instrument-Collapse-Panel

4. Levey-Jennings-Baseline-Selection

5. Levey-Jennings-Plotting-Option-Selection

6. Levey-Jennings-Channel-Laser-Selection

7. Levey-Jennings-Double-Chart-View

8. Levey-Jennings-Multiple-Chart-View

9. Levey-Jennings-Pagination-Support

10. Levey-Jennings-Date-Picker-Filter-Support

11. Levey-Jennings-Toggle-Average

12. Levey-Jennings-Toggle-Standard-Deviation

13. Levey-Jennings-Generate-Pdf-Support

14. Levey-Jennings-Printable-Pdf-Document

## Contributing

* Teresa Camarena, teresa.camarena@thermofisher.com

* Jaziel Lopez, jaziel.lopez@thermofisher.com 

## License

THIS SOFTWARE AND RELATED DOCUMENTATION CONTAINS PROPRIETARY MATERIALS OF THERMO FISHER SCIENTIFIC PROTECTED BY VARIOUS INTELLECTUAL PROPERTY RIGHTS. 
YOUR USE OF THE SOFTWARE AND DOCUMENTATION IS LIMITED
