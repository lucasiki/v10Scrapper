import os
import sys
import logging
import json

from pyvirtualdisplay import Display
from selenium import webdriver

from script import SCRIPT, INIT_URL

logging.getLogger().setLevel(logging.INFO)


def rundriver(running_script=None):
    
    display = Display(visible=0, size=(800, 600))
    display.start()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })

    driver = webdriver.Chrome(options=chrome_options)
    
    BASE_URL = running_script.url
    DATA = running_script.script

    driver.get(BASE_URL)
        
    value = None
    for key, value in DATA:
        value = driver.__getattribute__(key)(*value)

    driver.quit()
    display.stop()
    
    return value

if __name__ == '__main__':   

    rundriver(SCRIPT)
