from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Edge()

# TC01 - Open student registration page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# TC02 - Locate username / Text input
driver.find_element(By.NAME, "my-text").send_keys("NK")
time.sleep(2)

# TC03 - Enter password
driver.find_element(By.NAME, "my-password").send_keys("viji@123")
time.sleep(2)

# TC04 - Locate Submit using text()
driver.find_element(By.XPATH, "//button[text()='Submit']")
time.sleep(2)

# TC05 - Locate textbox dynamically using contains()
driver.find_element(
    By.XPATH,
    "//input[contains(@name,'my-text')]"
)
time.sleep(2)

# TC06 - Locate element with prefix using starts-with()
driver.find_element(
    By.XPATH,
    "//input[starts-with(@name,'my-')]"
)
time.sleep(2)

# TC07 - Find input using two attributes - and
driver.find_element(
    By.XPATH,
    "//input[@name='my-text' and @type='text']"
)
time.sleep(2)

# TC08 - Find element using alternatives - or
driver.find_element(
    By.XPATH,
    "//input[@name='my-text' or @name='my-password']"
)
time.sleep(2)

# TC09 - Find parent form
driver.find_element(
    By.XPATH,
    "//input[@name='my-text']/ancestor::form"
)
time.sleep(2)

# TC10 - Find form from input - ancestor
driver.find_element(
    By.XPATH,
    "//input[@name='my-text']/ancestor::form"
)
time.sleep(2)

# TC11 - Find child inputs
driver.find_elements(
    By.XPATH,
    "//form/child::input"
)
time.sleep(2)

# TC12 - Find next element
driver.find_element(
    By.XPATH,
    "//input[@name='my-text']/following::input[1]"
)
time.sleep(2)

# TC13 - Find checkbox
driver.find_element(
    By.XPATH,
    "//input[@type='checkbox']"
).click()
time.sleep(2)

# TC14 - Find radio button
driver.find_element(
    By.XPATH,
    "//input[@type='radio']"
).click()
time.sleep(2)

# TC15 - Select dropdown
dropdown = driver.find_element(
    By.XPATH,
    "//select"
)

Select(dropdown).select_by_visible_text("Two")
time.sleep(2)

# TC16 - Find second textbox
driver.find_element(
    By.XPATH,
    "(//input[@type='text'])[2]"
)
time.sleep(2)

# TC17 - Verify submitted message
driver.find_element(
    By.XPATH,
    "//button[text()='Submit']"
).click()
time.sleep(2)

# Reload the form before TC18
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# TC18 - Find all input fields

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

inputs = driver.find_elements(By.XPATH, "//input")

print("Number of input fields:", len(inputs))
time.sleep(2)


# TC19 - Locate textbox dynamically using contains()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

element = driver.find_element(
    By.XPATH,
    "//input[contains(@name,'my-text')]"
)


time.sleep(2)

# TC20 - Complete registration automation

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(
    By.NAME,
    "my-text"
).send_keys("Student")
time.sleep(2)

driver.find_element(
    By.NAME,
    "my-password"
).send_keys("Password123")
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//input[@type='checkbox']"
).click()
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//input[@type='radio']"
).click()
time.sleep(2)

Select(
    driver.find_element(By.TAG_NAME, "select")
).select_by_visible_text("Two")
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//button[text()='Submit']"
).click()
time.sleep(2)

print("Registration completed!")
time.sleep(20)