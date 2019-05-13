# -*- coding: utf-8 -*- 

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import sys, os
import urllib

driver = webdriver.Chrome('/Users/jjayd/Desktop/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://everytime.kr/login')

user_id = "ID"
user_pw = "PASSWORD"
driver.find_element_by_name('userid').send_keys(user_id)
driver.find_element_by_name('password').send_keys(user_pw)

driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

course=['유비쿼터스사회와소통능력', '문제해결기법', '컴퓨터공학세미나', '인간컴퓨터상호작용', '인포메이션디자인', '통합디자인스튜디오', '융합캡스톤디자인', '컴퓨터비전', '심화융합캡스톤디자인', '교육과창조경영', '감성지능과인포메틱스', '신호및시스템', '디지털통신', '제어공학기초', '동역학', 'Computer Aided Engineering', '창의적공학설계', '기술경영개론', '기술사업화캡스톤디자인', '생산관리', 'CAD/제품정보관리및실습', 'Forecasting and Time Series Analysis Utilizing Big Data', '논리회로', '논리회로설계실험', '마이크로프로세서', '디지털시스템', '데이터통신', '마이크로프로세서실험', '종합설계프로젝트', '스마트카공학개론', '기계학습개론', '기계학습종합설계', '스마트팩토리캡스톤디자인1', '시스템프로그램', '자료구조개론', ' 알고리즘개론', '컴퓨터개론', '오픈소스소프트웨어실습', '프로그래밍입문', 'JAVA프로그래밍실습', '소프트웨어공학개론', '데이터베이스개론', '운영체제', '컴퓨터구조개론', '프로그래밍언어', '컴퓨터그래픽스개론', '인공지능개론', '컴퓨터네트웍개론', '소프트웨어특강1', '임베디드소프트웨어개론', '네트워크프로젝트', '인공지능프로젝트', '소프트웨어현장실습1', '소프트웨어현장실습2', '모바일앱프로그래밍실습', '빅데이터분석방법론', '기계학습원론']
for c in course:
	driver.get('https://everytime.kr/lecture')
	elem=driver.find_element_by_name("keyword")
	elem.send_keys(c)
	elem.submit()
	
	ncourse=1
	while True:
		try:
			driver.find_element_by_xpath('//*[@id="container"]/div/a['+str(ncourse)+']').click()
		except:
			break

		professor = driver.find_element_by_xpath('//*[@id="container"]/div[2]/p[1]/span').text
		star = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[1]/span/span[1]').text
		assignment = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[1]/span').text
		teamproj = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[2]/span').text
		percentage = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[3]/span').text
		attendance = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[4]/span').text
		testnum = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[5]/span').text

		print("course: ",c)
		print("professor: ",professor)
		print("star: ",star)
		print("assignment: ",assignment)
		print("teamproject: ",teamproj)
		print("percentage: ",percentage)
		print("attendance: ",attendance)
		print("testnum: ",testnum)
		narticle=1
		while True:
			try:
				arti=driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[2]/article['+str(narticle)+']/p[3]').text
				semester = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[2]/article['+str(narticle)+']/p[2]/span').text
				if(semester==""):
					semester = driver.find_element_by_xpath('//*[@id="container"]/div[4]/div[2]/article/p[2]/span').text
				print("semester: ",semester)
				print("article: ",arti)
				narticle=narticle+1
			except:
				break

		ncourse=ncourse+1
		print()
