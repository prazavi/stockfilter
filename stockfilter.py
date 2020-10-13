from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.get('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
setting=driver.find_element_by_css_selector('#id1')
setting.click()
set=driver.find_elements_by_css_selector('.awesome.tra')
for i in set:
    if i.text=='همه نمادها':
        i.click()
        break
setting2=driver.find_element_by_css_selector('#id1')
setting2.click()
set=driver.find_elements_by_css_selector('.awesome.tra')
for i in set:
    if i.text=='حقیقی و حقوقی':
        i.click()
        break
filter=driver.find_element_by_css_selector('.MwQuery')
filter.click()
new_filter=driver.find_element_by_css_selector('.black')
new_filter.click()
filter0=driver.find_element_by_css_selector('.tra')
filter0.click()
filter_text=driver.find_element_by_id('InputFilterCode')
filter_text.clear()
filter_text.send_keys(r'0<(pe)&&(pe)<8&&(ct).Buy_N_Volume>(5*(ct).Sell_N_Volume)')
filter_play=driver.find_element_by_css_selector('.awesome.blue')
filter_play.click()
result=driver.find_elements_by_css_selector('.inst')
count=0
for i in result:
    count+=1
    if count%2==1:
        print(f'سهم شماره{1+count//2}')
    # if count%2==1:
        print(i.text)