from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def getUrl():
    search = str(input("Please enter the domain name: "))
    url = 'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + search + '.com'
    return url

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome('chromedriver') #location of the chrome driver
    browser.get(getUrl())
    browser.delete_all_cookies()
    browser.implicitly_wait(1)
    try:
        try:
            available = browser.find_element_by_xpath(
            '//*[@id="search-app"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/span').text
            domain = browser.find_element_by_xpath(
            '//*[@id="search-app"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/p').text
            price = browser.find_element_by_xpath(
            '//*[@id="search-app"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/span[1]/div/span[3]').text
            print(f'Hurray !!! {available} available')
            print(f'Domain: {domain}\nPrice: {price}')
        except:
            available = browser.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div/div[1]').text
            domain = browser.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div/p/span').text
            price = browser.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div/div[2]/span[1]').text
            print(f'Hurray !!! {available}')
            print(f'Domain: {domain}\nPrice: {price}')
    except NoSuchElementException:
        print('Sorry !!!, Domain is already taken. Please search other domains.')
    browser.close()


