# pip install selenium 
# brew install chromedriver
# pip install webdriver-manager

from selenium import webdriver #webdriverをimport
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep  #sleepをimport 処理を止めることができる(3秒待って実行など、、)

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.awseducate.com/signin/SiteLogin?ec=302&startURL=%2Fstudent%2Fs%2F"
browser.get(url)
elem_username = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:username') 
elem_username.send_keys("hirano.kentaro.infratop@gmail.com")
elem_password = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:password') 
elem_password.send_keys("yakyuken2024!")
sleep(1)
elem_login_btn = browser.find_element_by_class_name('loginText')
elem_login_btn.click()
sleep(7)
elem_aws_account_btn = browser.find_element_by_css_selector("a[href='/student/s/awssite")
elem_aws_account_btn.click()
sleep(4)
elem_start_account_btn = browser.find_element_by_class_name('btn')
elem_start_account_btn.click()
sleep(7)
browser.switch_to.window(browser.window_handles[-1])
elem_aws_console_btn = browser.find_element_by_id('awsbtn')
elem_aws_console_btn.click()
sleep(5)
browser.switch_to.window(browser.window_handles[-1])
cloud9_url = "https://console.aws.amazon.com/cloud9/home?region=us-east-1#"
browser.get(cloud9_url)