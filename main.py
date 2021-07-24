import j_handler
import ebay_scraper
from colorama import Fore, Back, Style
JH = j_handler.JSON_Handler()

fg_prompt = Fore.LIGHTCYAN_EX
fg_num = Fore.GREEN
fg_opts = Fore.YELLOW
fg_quit = Fore.RED
def main():
    print( 	 "  __  __           _        _             _   _                               \n"
	" |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n"
	" | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n"
	" | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n"
	" |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n"
	"                                  |___/                                       \n\n")
    while True:
        user_opt = int(input("\n\n" + fg_prompt + "What would you like to do?" + Fore.RESET + "\n" +
            fg_num + "1." + fg_opts + " Scrape Ebay\n" + 
            fg_num + "2." + fg_opts + " Show json\n" + 
            fg_num + "3." + fg_opts + " Search json by title\n" +
            fg_num + "4." + fg_opts + " Sort json by price ascending\n" +
            fg_num + "5." + fg_opts + " Sort json by price descending\n" +
            fg_num + "6." + fg_opts + " Quit \n" + Fore.RESET))
        if user_opt == 1:
            ES = ebay_scraper
            ES.scrape()
        if user_opt == 2:
            item_dict = JH.getDict()
            try:            
                JH.showDict(item_dict)
            except:
                print(fg_quit + "Could not parse the dict!\n" + Fore.RESET)
        if user_opt == 3:
            item_dict = JH.getDict()
            if item_dict != None:
                new_dict = JH.searchForText(item_dict)
                JH.showDict(new_dict)
        if user_opt == 4:
            item_dict = JH.getDict()
            sorted_list = JH.sortJSON(item_dict)
        if user_opt == 5:
            item_dict = JH.getDict()
            sorted_list = JH.sortJSON(item_dict, ascending=False)
        if user_opt == 6:
            print(fg_quit + "\nExiting...\n\n" + Fore.RESET)
            break
main()