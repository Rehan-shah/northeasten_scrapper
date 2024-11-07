

import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def grade_click(webdriver: WebDriver, grade: int):

    dropdown = Select(webdriver.find_element(By.ID,'form_6d343b98-1791-4946-a37d-db3752ce3c49'))


    dropdown.select_by_visible_text(f"{grade}th Grade")

    date_m = Select(webdriver.find_element(By.ID,'form_76ed993f-fa70-4d47-9c70-f0816807be5f_m'))


    date_m.select_by_visible_text("June")
    
    date_y = Select(webdriver.find_element(By.ID, "form_76ed993f-fa70-4d47-9c70-f0816807be5f_y"))

    date_y.select_by_visible_text(f"{grade+2012}")

def sub_area_click(webdriver: WebDriver, sub_area: str):

    dropdown = Select(webdriver.find_element(By.ID,'form_624246fd-3add-4b77-9576-c7093ee36fe4'))


    dropdown.select_by_visible_text(f"{sub_area}")

def cou_level(webdriver: WebDriver, cou_level: str):

    dropdown = Select(webdriver.find_element(By.ID,'form_624246fd-3add-4b77-9576-c7093ee36fe4'))

    dropdown.select_by_visible_text(f"{cou_level}")

def level_sc(webdriver: WebDriver, level: str):

    dropdown = Select(webdriver.find_element(By.ID,'form_7375809c-9f5a-45ca-a025-c9e4ecfdc293'))

    dropdown.select_by_visible_text(f"{level}")

def grade_sc(webdriver: WebDriver, grade: str):

    
    dropdown = Select(webdriver.find_element(By.ID,'form_7375809c-9f5a-45ca-a025-c9e4ecfdc293'))


    dropdown.select_by_visible_text("Letter")

    dropdown = Select(webdriver.find_element(By.ID, "form_acdb7194-1273-459e-9d61-22b12f1782d0"))

    dropdown.select_by_visible_text(f"{grade}")

    webdriver.find_element(By.ID,'form_fc8e4be9-b8ef-4b00-ae13-ce4e072c4e15').send_keys("4")

    webdriver.find_element(By.XPATH,'//*[@id="form_7cf24d6d-a569-483f-bcce-19c5e886d8b0_container"]/div[4]/button').click() #course

