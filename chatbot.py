from selenium import webdriver

import PyPDF2

driver = webdriver.Chrome("/Users/ankityadav/Desktop/DMbot/chromedriver")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter Name of person or group you want to spam:")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//* [@id='main']/footer/div[1]/div[2]/div/div[2]")

pdfFileObj = open('the-lion-king.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for index in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    print(text)
    msg_box.send_keys(text)
    driver.find_element_by_xpath("//* [@id='main']/footer/div[1]/div[3]/button") .click()

print("Success")
