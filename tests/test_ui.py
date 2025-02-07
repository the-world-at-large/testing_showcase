import time

from selenium import webdriver


def test_ui():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    time.sleep(2)
    title = driver.title
    driver.quit()
    assert "Example Domain" in title
