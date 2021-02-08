from selenium import webdriver 
#search_string = input("Input the URL or string you want to search for:")  
def google_search(search_string):
    search_string = search_string.replace(' ', '+')   
    browser = webdriver.Chrome('chromedriver') 
    for i in range(1): 
        matched_elements = browser.get("https://www.google.com/search?q=" +
                                        search_string + "&start=" + str(i))