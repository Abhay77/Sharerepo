import re, os, sys, time, glob, shutil 
import __builtin__
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
#from WikiaWebComponent import *
#from GUIEvent import GUIEvent
#from WikiaErrorCode import WikiaErrorCode
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
LOG_FILENAME = 'logging.txt'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )


f = open(LOG_FILENAME, 'rt')




confpath = "F:\\tmp\Wikia\wikiaconf.ini"
hashes = {}
url = "http://testhomework.wikia.com/"
youtubeurl = "http://www.youtube.com/watch?v=h9tRIZyTXTI"
class WikiaGUI():



    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.base_url = url
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True


    def login(self):
        try:
            logging.info("Started Login")
            self.driver.get(self.base_url + "/wiki/Test-homework_Wiki")
            self.driver.find_element_by_link_text("Log in").click()
            self.driver.find_element_by_name("username").clear()
            self.driver.find_element_by_name("username").send_keys(self.username)
            self.driver.find_element_by_name("password").clear()
            self.driver.find_element_by_name("password").send_keys(self.password)
            self.driver.find_element_by_css_selector("input.login-button").click()
            print self.driver.find_element_by_xpath("//*[@id='AccountNavigation']/li/a").text, ">>>>>>>>>>>>>>>>>"
            self.driver.find_element_by_xpath("//*[@id='AccountNavigation']/li/a").text == self.username
            logging.info("Login successful")
        except:
            logging.critical("Login failed")

    def uploadvideo(self):
        try:
            logging.info("Started uploading video")                        
            self.driver.find_element_by_xpath(".//*[@id='WikiHeader']/div[2]/nav").click()     
            self.driver.find_element_by_link_text("Add a Video").click()
            self.driver.find_element_by_id("wpWikiaVideoAddUrl").clear()
            self.driver.find_element_by_id("wpWikiaVideoAddUrl").send_keys(youtubeurl)
            self.driver.find_element_by_css_selector("div.submits > input[type=\"submit\"]").click()
            self.driver.find_element_by_xpath("html/body/div[3]/div[3]/div").text == "Video page File:The Best Classical Music In The World was successfully added."
            self.driver.find_element_by_xpath("html/body/div[3]/div[3]/div/a").click()
            self.driver.find_element_by_xpath(".//*[@id='WikiaPageHeader']/h1").text == "The Best Classical Music In The World"
            logging.info("Uploaded video successfully")
        except:
            logging.critical("Upload video failed")
 

    def quit(self):
        self.driver.quit()
        try:
            body = f.read()
        finally:
            f.close()



def readconf(confpath="F:\\tmp\Wikia\wikiaconf.ini"):
        try:
            print confpath
            fo = open(confpath, "r")
            str1 = fo.readlines()
            #Close opend file
            fo.close()
        except IOError:
            print "Error: File does not appear to exist."
        return str1




def conftodict(var1):
    i = 0
    for x in range(len(var1)):
        xy = re.compile('(.*)\s=\s(.*)')
        matchxy = xy.search(var1[x])
        hashes[matchxy.group(1)] = matchxy.group(2)
        i = i + 1
    return hashes
var1 = readconf(confpath)
hashes1 = conftodict(var1)
print hashes1

