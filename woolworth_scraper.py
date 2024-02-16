# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = "https://www.woolworths.com.au/shop/search/products?searchTerm=spam"
#URL = "https://www.woolworths.com.au/"
#URL = str(input("Enter link: "))
# PATH = "/usr/bin/geckodriver"
# I don't reference PATH inside Firefox() is because i already put the Geckodriver in /usr/bin/
driver = webdriver.Firefox()


#def extract_source(url):
#    # you need to specify allowable user-agent or permission will be denied
#    agent = {"User-Agent":"Mozilla/5.0"}
#    page = requests.get(url, headers=agent).text
#    return page

#print(extract_source(URL))

driver.get(URL)


print(driver.title)

#search = driver.find_element(By.ID, "wx-headerSearch")
#search.send_keys("spam")
#search.send_keys(Keys.RETURN)

# price frame (Class)
try: 
    main = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ng-tns-c106-3:nth-child(3)"))
    )

    #print(main)

    for element in main.text:
        print(element)
finally:
    driver.quit()


