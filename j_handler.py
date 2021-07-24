import json
import os
from colorama import Fore, Back, Style
import unicodedata
root = os.getcwd()

if not os.path.exists("JSON"):
    os.makedirs("JSON")
os.chdir("JSON")

fg_money = Fore.GREEN
fg_title = Fore.LIGHTCYAN_EX
fg_link = Fore.LIGHTBLACK_EX
fg_prompt = Fore.LIGHTCYAN_EX


class JSON_Handler:
    def getDict(self):
        dir = os.listdir()
        print("\nYour JSON directory contains the following files:\n")
        for i in range(len(dir)):
            split = os.path.splitext(dir[i])
            fileIndex, fileExt = split[0], split[1]
            if fileExt == ".json":
                print(str(i+1) + ") " + dir[i])
        print('\n')

        fileIndex = int(input("Enter the number of the file you want to open:\n"))
        try:
            f = open(dir[fileIndex-1], "r")
        except IndexError:
            print(Fore.RED + "That file does not exist!\n" + Fore.RESET)
            return
        try:
            item_dict = json.load(f)
        except json.JSONDecodeError:
            print(Fore.RED + "ERROR: The file you tried to open was either not a json file, or contains data that " + 
            "I can't read for some reason." + Fore.RESET)
            return


        return item_dict
    def showDict(self, item_dict):
        i = 0
        for item in item_dict:
            i += 1
            curr_item = item_dict[item]
            print('=========================================================')
            print(str(i) + ". "+ fg_money + curr_item["price"] + Fore.RESET + " - " + fg_title + item + Fore.RESET)
            print(fg_link + curr_item["link"] + Fore.RESET)
        print('=========================================================')
    def showList(self, dict_list):  # dict list will be a list of dicts
        for i in range(len(dict_list)):
            curr_item = dict_list[i]
            print('=========================================================')
            print(str(i+1) + ". "+ fg_money + curr_item["price"] + Fore.RESET + " - " + fg_title + curr_item["title"] + Fore.RESET)
            print(fg_link + curr_item["link"] + Fore.RESET)
        print('=========================================================')        
    #def sort
    def searchForText(self, item_dict):
        subStr = input("Enter the text to search for:\n")
        new_dict = {}
        for item in item_dict:
            curr_item = item_dict[item]
            if subStr.lower() in item.lower():  # ignore case sensitivity
                new_dict[item] = curr_item
        return new_dict
    def sortJSON(self, item_dict, ascending=True):
        """ # This will save a readable list if i want to do this
        def saveSortedList(file, lst):
            with open(file, "w+") as f:
                for i in range(len(lst)):
                    curr_item = lst[i]
                    f.write('=========================================================\n')
                    text = unicodedata.normalize(u'NFKD', str(i) + ". "+  curr_item["price"] + " - " + curr_item["title"] + "\n").encode('ascii', 'ignore').decode('utf8')
                    # This ignores unicode characters that otherwise could not be written to a txt file. (Basically anything above utf8)
                    # I have no fucking idea how this works but source: https://stackoverflow.com/questions/51710082/what-does-unicodedata-normalize-do-in-python
                    # keep note of this for the future
                    #print("text: ", text)
                    f.write(text)
                    f.write(curr_item["link"] + "\n")
                print(fg_prompt + "Saved data to " + file.__str__())
        """
        def saveSortedList(file, lst):
            with open(file, "w+") as f:
                json.dump(lst, f)   # Dump that list
                print(fg_prompt + "Saved data to " + file.__str__())
        dict_list = []
        for item in item_dict:
            dict_list.append(item_dict[item])
        sorted_list = sorted(dict_list, key = lambda i: i['raw_price']) # now we have sorted list, make a function that displays a list of dicts cleanly.
        if ascending:
            self.showList(sorted_list)
        if not ascending:
            sorted_list.reverse()   # reverse doesn't return anything, it mutates the list.
            self.showList(sorted_list)
        
        file = "sorted.json"
        saveSortedList(file, sorted_list)


        #print(sorted_list)
        #return sorted_list



            


