import shutil
import os
import webbrowser
import time
from selenium import webdriver

# print(shutil.move('C:\\z_test\\src\\The.Vampire.Diaries.S04E01.HDTV.x264-LOL.srt',
#            'C:\\z_test\\dist\\'))

# print(shutil.move('C:\\z_test\\src\\The.Vampire.Diaries.S04E01.HDTV.x264-LOL.srt',
#                 'C:\\z_test\\src\\test.txt'))


# for f, s, file in os.walk('C:\\z_test'):
#     print ('the current folder is: ',f)
#
# webbrowser.open('http://eca.gov.sa/cs')
# print(time.sleep(1))

#fbrowser = webdriver.Firefox(executable_path="C:/Program Files/Firefox Developer Edition/firefox.exe")
#fbrowser.get('http://www.google.com')

related_case = str(input('Enter Case ID: '))
browser = webdriver.Chrome(executable_path='C:/Users/ibrahim/Downloads/chromedriver_win32/chromedriver.exe')
browser.switch_to.window('')
browser.maximize_window()
browser.get('https://goo.gl/LFbRHC')
#time.sleep(1)
#time.sleep(1)
user_id = browser.find_element_by_name('userid')
user_id.send_keys('ecmadmin')
pass_word = browser.find_element_by_name('password')
#pass_word.send_keys('')
time.sleep(1)
pass_word.submit()
#browser.get('http://eca.gov.sa/cs/groups/secure/logs/IdcLnLog.htm')
#time.sleep(1)
#browser.back()

search = browser.get('http://eca.gov.sa/cs/idcplg?IdcService='
                     'GET_SEARCH_RESULTS&'
                     'QueryText=xsiebelCase<matches>`'+related_case+'`'
                     '&ResultCount=500&'
                     'ftx=&'
                     'SortField=xAttachmentCode&'
                     'SortOrder=Asc')

#log_out = browser.find_element_by_link_text('Logout')
#log_out.click()
#time.sleep(2)
#browser.quit()
