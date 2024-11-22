from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://barbora.lt/produktai/grikiai-well-done-800-g")
# driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()

# a = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/div/meta[1]")
# print(driver.title)
# print(a)

# # bandau kaina - printina stulpeliu
# a = driver.find_element(By.ID, "fti-product-price--0").text
# print(a)

# # VEIKIA PUSIAU
# elements = driver.find_elements(By.CLASS_NAME, "b-product-info--price-and-quantity")
# texts = [element.text for element in elements]
# print(texts, sep="\n")
# print(texts, sep="\n\n ") # spaudina paskutini dalyka (kartais)

a = driver.find_element(By.CLASS_NAME, "tw-pb-1").text
# print(a[0])
print(a)
# print(type(a))
# type(a)
driver.close()