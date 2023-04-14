from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

class MyWebDriver:

    def get_driver(self):
        webdrivers = [
            GeckoDriverManager,
            ChromeDriverManager,
            EdgeChromiumDriverManager,
            IEDriverManager,
        ]
        for webdriver_manager in webdrivers:
            try:
                if webdriver_manager== GeckoDriverManager:
                    print("trying Firefox")
                    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
                    driver.get('https://www.google.com')
                    print(f"Current URL: {driver.current_url}")
                elif webdriver_manager==ChromeDriverManager:
                    print("trying Chrome")
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                    driver.get('https://www.google.com')
                    print(f"Current URL: {driver.current_url}")
                elif webdriver_manager == EdgeChromiumDriverManager:
                    print("trying Edge")
                    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
                    driver.get('https://www.google.com')
                    print(f"Current URL: {driver.current_url}")
                elif webdriver_manager ==IEDriverManager:
                    print("trying IE")
                    driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
                    driver.get('https://www.google.com')
                    print(f"Current URL: {driver.current_url}")
                else:
                    raise Exception("all attempts failed")
                return driver
            except Exception as e:
                print(f"{webdriver_manager.__name__} failed: {str(e)}")
                continue
        raise Exception("Could not find a compatible webdriver")


if __name__ == '__main__':
    driver = MyWebDriver().get_driver()
    driver.close()
