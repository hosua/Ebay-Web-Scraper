from selenium import webdriver
from datetime import datetime
from colorama import Fore, Back, Style
import json
import time


fg_prompt = Fore.LIGHTCYAN_EX
fg_page = Fore.LIGHTMAGENTA_EX
fg_num = Fore.GREEN
fg_opts = Fore.YELLOW
fg_quit = Fore.RED



def scrape():
    
    def dumpJson(file, item_dict):
        with open(file, "w+") as f:
            json.dump(item_dict, f)
            print(fg_prompt + "Saved data to " + file.__str__())

    chrome_opts = webdriver.ChromeOptions()
    chrome_opts.add_argument("-headless")   # You can run the scraper without opening a window
    driver = webdriver.Chrome(options=chrome_opts)
    ebay_home = "https://www.ebay.com/"
    driver.get(ebay_home)
    textBox = driver.find_element_by_id("gh-ac")

    item = input(fg_prompt + "Enter an item to search for\n" + Fore.RESET)
    textBox.send_keys(item + "\n")
    
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file = item.replace(" ", "-") + "-" + str(now) + ".json"

    item_dict = {}
    num_pages = int(input(fg_prompt + "How many pages?\n" + Fore.RESET))
    print("\n\n")

    fg_money = Fore.GREEN
    fg_title = Fore.LIGHTCYAN_EX
    fg_link = Fore.LIGHTBLACK_EX

    k = 0   # Make this global to continue page count between pages
    for i in range(num_pages):
        items = driver.find_elements_by_class_name("s-item__info")
        print(fg_page + "==================Page " + str(i+1) + "====================" + Fore.RESET)
        try:
            next_page = driver.find_element_by_class_name("pagination__next")
        except:
            print(fg_quit + "Could not find next page! Finishing...\n" + Fore.RESET)
            dumpJson(file, item_dict)
        for j in range(len(items)):
            try:
                k += 1  
                link = items[j].find_element_by_class_name("s-item__link").get_attribute("href")
                title = items[j].find_element_by_class_name("s-item__title").text.replace("NEW LISTING", "")
                details = items[j].find_element_by_class_name("s-item__details")
                detail = details.find_element_by_class_name("s-item__detail")
                price = detail.find_element_by_class_name("s-item__price").text
                if "to" in price:
                    new_item = price.replace(" to ", "").replace("$", " ")[1:]
                    #print("new_item: " + new_item)
                    prices = new_item.split()
                    sum = 0
                    for thing in prices:
                        sum += float(thing)
                    raw_price = sum/2 # get the average price
                else:
                    raw_price = float(price.replace("$", "")) # just return the float
                item_dict[title] = {"title": title, "price": price, "link": link, "raw_price": raw_price}
                #print(raw_price)
                print(str(k-1) + ". " + fg_money + price + fg_title +" - " + title + Fore.RESET)
                print(fg_link + link + Fore.RESET) 
            except:
                pass
            print("============================================================")
        try:
            next_page.click()
        except: # It kinda seems dumb to do it this way but this throws weird errors.
            break

    dumpJson(file, item_dict)

    
