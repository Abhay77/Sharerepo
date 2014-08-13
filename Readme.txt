1) Current code works with firefox.
For chrome: driver = webdriver.Chrome('/path/to/chromedriver') 

2) Model wikiaweb.py is library which has WikiaGUI class with login, uploadvideo, quit functions. It has also logging enabled.

3) Logfile named logging.txt will be created inside the same directory.

4) wikiaconf.ini can contain config parameters where one can store username, password, xpaths or other identifiers. I have currently read user and password however function conftodict is already written.

5) Testcases are named "Wikiatest1.py and Wikiatest2.py. I have used python unittest module.


