import os
import json
test_str1 = "$200.00 to $400.00"
test_str2 = "$300"

test_list = [test_str1, test_str2, "$99.99 to $100.99"]

def getNums(num_str):
    try:
        if "to" in num_str:
            new_item = item.replace(" to ", "")
            prices = new_item.split('$')
            prices.remove("")
            prices = [float(i) for i in prices]
            raw_price = float(prices/2) # return the average price
        else:
            return float(num_str.replace("$", "")) # just return the float
    except:
        print("No price detected\n")
        return

def main():
    f = open("JSON\phone-2021-06-14_22-17-37.json", "r")
    item_dict = json.load(f)
    #print(item_dict)
    dict_list = []
    for item in item_dict:
        dict_list.append(item_dict[item])
    
    print(dict_list)
    
main()