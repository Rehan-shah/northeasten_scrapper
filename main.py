from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from utlis import grade_click, sub_area_click,grade_sc 

res = None

with open("grades.json","rb") as f:
    res = json.load(f)

for n in res:
    if n.get("grade_mark") == "IP":
        n.update({"grade_mark": "In-Progress (IP)"})
    if n.get("course_level") == "IGCSE" or n.get("course_level") == "regular":
        n.update({"course_level": "10df73c9-0baa-4b3a-8ce9-5fc6a465cebb"})
    if n.get("course_level") == "AS Level":
        n.update({"course_level": "GCE Advanced Subsidiary Level"})
    if n.get("course_level") == "A Level":
        n.update({"course_level": "GCE Advanced Level"})

driver = webdriver.ChromiumEdge()



driver.get("https://apply.northeastern.edu/account/login?r=https://apply.northeastern.edu/portal/app_status?utm_campaign%3DFRapplicant%26utm_content%3DASC_appacknowledge%26utm_medium%3Demail%26utm_source%3Ddeliver%26utm_term%3Dfa25")

driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("Rehanshahcollage@gmail.com")

driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Rehan!2345678")

driver.find_element(By.XPATH,'//*[@id="content"]/form/table/tbody/tr/td[1]/div/button').click()


driver.get("https://apply.northeastern.edu/portal/sr_coursework")


for n in res:
    time.sleep(3)
    try:
        add_course_btn = driver.find_element(By.XPATH, '//*[@id="part_8b5ebf1a-0507-4c57-a7aa-0eae29822a70"]/table/tbody/tr/td[2]/strong/a')
    except:
        time.sleep(3)
        add_course_btn = driver.find_element(By.XPATH, '//*[@id="part_8b5ebf1a-0507-4c57-a7aa-0eae29822a70"]/table/tbody/tr/td[2]/strong/a')
    add_course_btn.click()
    time.sleep(2)
    grade_click(driver, n.get("grade"))
    time.sleep(1)
    sub_area_click(driver, n.get("subject area"))
    time.sleep(1)
    driver.find_element(By.ID,"form_3ecf3c52-c90e-4efb-9b12-103c0704a421").send_keys(n.get("name"))
    time.sleep(5)

    grade_sc(driver, n.get("grade_mark"))

    time.sleep(3)
    

time.sleep(10000)
driver.get("https:google.com")
