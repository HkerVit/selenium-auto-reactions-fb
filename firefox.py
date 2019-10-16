 # – coding: utf-8 –
from selenium import webdriver
import time
import random

driver = webdriver.Firefox()
driver.get('https://mbasic.facebook.com')

reaction_link = []
accout_list = []
def set_cookie(cookie = ''):
	ck_split = cookie.split('; ')
	for x in ck_split:
		ck = x.split('=')
		cookie = {
			'name': ck[0],
			'value' : ck[1]
		}
		driver.add_cookie(cookie)
	driver.refresh()
def find_posts_link():
	element = driver.find_elements_by_xpath("//a[contains(text(),'Bày tỏ cảm xúc')]")
	for x in element:
		reaction_link.append(x.get_attribute('href'))
def reaction_post(reac = 1):
	reac = int(reac)
	print(reac)
	for x in reaction_link:
		driver.get(x)
		elm = driver.find_elements_by_xpath("//a")
		elm[reac].click()
		print(str(reac) + ' posts \n')
		time.sleep(5)

def get_reactions_account(limit = 5):
	f = open("account.txt", "r")
	acc_list = f.read().split('\n')
	for x in acc_list:
		now_acc = x.split('|')
		if int(now_acc[3]) < time.time():
			break
		set_cookie(now_acc[0])
		find_posts_link()
		string = now_acc[2];

		reaction_post(string[random.randint(0, len(string))])
		#accout_list.append(acc_info)
		print('run done account \n')
	#print('get total '+str(len(accout_list)) + ' account avaiable !')
# set_cookie('sb=eJuMXSopE9t9x7FSekKoM3HX; datr=eJuMXeBdtsHpKgZnG_QzJ8tK; xs=32%3Atgyed4byBzAehQ%3A2%3A1570168865%3A8397%3A6313; c_user=100016029917976; ')
# find_posts_link()
# reaction_post('', '')
#reaction_post('', '')
get_reactions_account()

