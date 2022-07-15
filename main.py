#lib impoorts for selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#imports for the program
my_info = open("form.txt", "r")
codes = open("codes.txt", "r")

#pharsing information from the file to be used in the program
info = my_info.read()
info_list = info.split("\n")
info.close()

#selenium options
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")
options.add_argument("--disable-gpu")

#main code
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
driver.get("https://halo.lucozade.com")
Thread.sleep(2000)
cookies = driver.find_element_by_xpath('//button[text()="Allow all cookies"]')
Thread.sleep(3000)
fname = driver.find_element_by_name('firstName').send_keys(info_list[0])
Thread.sleep(2500)
email = driver.find_element_by_name('email').send_keys(info_list[1])
Thread.sleep(2650)
cemail = driver.find_element_by_name('confirmEmail').send_keys(info_list[1])
Thread.sleep(2819)
phone = driver.find_element_by_name('mobile').send_keys(info_list[2])
Thread.sleep(2910)
postcode = driver.find_element_by_name('postcode').send_keys(info_list[3])
Thread.sleep(2719)
pcode = driver.find_element_by_xpath('//option[@selected="-"]').select_by_visible_text('44')
Thread.sleep(2730)
country = driver.find_element_by_xpath('//option[@selected="Select country...]').select_by_visible_text('United Kingdom')
Thread.sleep(2780)
purchase = driver.find_element_by_xpath('//option[@selected="Select location..."]').select_by_visible_text('Tesco')
Thread.sleep(3201)
age = driver.find_element_by_name('age').click()
Thread.sleep(2000)
terms = driver.find_element_by_name('terms').click()
Thread.sleep(3000)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
Thread.sleep(2390)
nbutton = driver.find_element_by_xpath('//button[text()="Next"]').click()
code = input("Please enter the code sent to your email")
verification = driver.find_element_by_name('verificationCode').send_keys(code)#need to add mail api to get the code

#because there is no name element, i have to use an xpath to find the element via the text. However there is a problem as there is two elements with the same text. 
#the code below does a try catch method to select the correct answer
try:
    ans1 = driver.find_element_by_xpath('//option[@selected="Select Answer..."]').select_by_visible_text('22')
except:
    ans1 = driver.find_element_by_xpath('//option[@selected="Select Answer..."]').select_by_visible_text('19:00')
try:
    ans2 = driver.find_element_by_xpath('//option[@selected="Select Answer..."]').select_by_visible_text('19:00')
except:
    ans2 = driver.find_element_by_xpath('//option[@selected="Select Answer..."]').select_by_visible_text('22')
play = driver.find_element_by_xpath('//button[text()="Play"]').click()
explore = driver.find_element_by_xpath('//*[contains(text(), "Click to explore")]').click()
claim = driver.find_element_by_xpath('//button[text()="claim"]').click()