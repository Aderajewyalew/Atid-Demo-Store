from time import sleep
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium import webdriver
from selenium.webdriver.common.by import By
from Atid_Store.Bases_Test.location import *


#

def test_store_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()
    driver.find_element(By.XPATH,
                        f"{store_button}").click()

    sleep(2)
    driver.find_element(By.XPATH,
                        f"{abchor_bracelet}").click()
    sleep(2)
    driver.find_element(By.XPATH, f"{add_to_chart}").click()
    sleep(2)
    driver.find_element(By.XPATH,
                        f"{view_prduct_chart}").click()
    sleep(2)
    coupon_filed = driver.find_element(By.XPATH, f"{coupon_box}")
    sleep(2)
    coupon_filed.clear()
    coupon_filed.send_keys("1234vdbdsb")
    sleep(2)
    driver.find_element(By.XPATH, f"{apply_copuon}").click()
    sleep(2)
    productname = driver.find_element(By.XPATH, f"{name_product}").text
    assert productname == "Anchor Bracelet"

    productprice = driver.find_element(By.XPATH, f"{product_price}").text
    assert productprice == "250.00 ₪"


def test_men_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()
    driver.find_element(By.XPATH,
                        f"{men_button}").click()
    sleep(1)
    driver.find_element(By.XPATH,
                        f"{page_two}").click()
    sleep(1)
    driver.find_element(By.XPATH,
                        f"{product_red_hoodies}").click()
    sleep(1)
    driver.find_element(By.XPATH, f"{quantity}").click()
    sleep(1)
    driver.find_element(By.XPATH, f"{add_to_chart_men}").click()
    sleep(1)

    driver.find_element(By.XPATH,
                        f"{view_chart}").click()
    sleep(1)
    name = driver.find_element(By.XPATH, f"{product_name}").text
    assert name == "Red Hoodie"
    coupon_filed = driver.find_element(By.XPATH, f"{coupon_field}")
    sleep(2)
    coupon_filed.clear()
    coupon_filed.send_keys("1234vdbdsb")
    sleep(2)
    driver.find_element(By.XPATH, f"{aplly_cupon}").click()
    product_price = driver.find_element(By.XPATH, f"{price}").text
    assert product_price == "150.00 ₪"
    sleep(3)


def test_women_buy_product():
    women_driver = webdriver.Chrome()
    women_driver.get("https://atid.store/")
    women_driver.maximize_window()
    women_driver.find_element(By.XPATH,
                              f"{women_button}").click()
    sleep(1)
    women_driver.find_element(By.XPATH,
                              f"{click_shoulder_handbag}").click()
    sleep(1)
    women_driver.find_element(By.XPATH, f"{increase_quantity}").click()
    sleep(1)
    women_driver.find_element(By.XPATH, f"{added_to_chart}").click()
    sleep(1)
    women_driver.find_element(By.XPATH, f"{view_to_chart}").click()
    sleep(1)

    product_name = women_driver.find_element(By.XPATH, f"{products_name}").text
    assert product_name == "Black Over-the-shoulder Handbag"

    product_price1 = women_driver.find_element(By.XPATH, f"{products_price1}").text
    assert product_price1 == "85.00 ₪"
    copun_box = women_driver.find_element(By.XPATH, f"{coupon_boxw}")
    sleep(2)
    copun_box.clear()
    copun_box.send_keys("123321wed")
    sleep(2)
    women_driver.find_element(By.XPATH, f"{click_copun}")
    sleep(2)

def accesserios_product():

    accessrios = webdriver.Chrome()
    accessrios.get("https://atid.store/")
    accessrios.maximize_window()
    accessrios.find_element(By.XPATH,
                            f"{accesserios}").click()
    sleep(1)
    accessrios.find_element(By.XPATH,
                            f"{click_products}").click()
    sleep(1)
    accessrios.find_element(By.XPATH, f"{click_quantity}").click()
    sleep(1)
    accessrios.find_element(By.XPATH, f"{click_add_product}").click()
    sleep(1)
    accessrios.find_element(By.XPATH, f"{view_chart_acc}").click()
    sleep(1)

    product_name = accessrios.find_element(By.XPATH, f"{productName}").text
    assert product_name == "Boho Bangle Bracelet"

    product_price1 = accessrios.find_element(By.XPATH, f"{productPrice}").text
    assert product_price1 == "45.00 ₪"
    copun_box = accessrios.find_element(By.XPATH, f"{copupn_box}")
    sleep(2)
    copun_box.clear()
    copun_box.send_keys("123321wed")
    sleep(2)
    accessrios.find_element(By.XPATH, f"{click_copun}")
    sleep(2)


accesserios_product()

