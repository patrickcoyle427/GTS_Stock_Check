#!/bin/usr/python3

'''
GTS_stock_check.py

NOTE: Will only work if the user is currently logged into GTS Distribution
        www.gtsdistribution.com

Loads a CSV file of products that need to be reordered, generated through lightspeed retail.

Searches GTS Distribution, a hobby and collectible distributor, to check if the product is in stock.
Output is a CSV file with the UPC, Name, and quantity to Order if the product is in stock.

'''

# TO DO:
# Do I need to log requests in? If so find out how:
#   For research: https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module
#   Check answer by tigerFinch
# If needed, create a function for the user to log in with
# Read the page found from the search and find the in stock quantity
# If in stock, write the upc, item name, # to order and GTS in stock quantity to
#   a new csv file.

import bs4, csv, os, os.path, requests

# bs4 - Beautiful Soup to read the webpage received from the requests GET request
# csv - Used to read the Lightspeed retail generated CSV of products needed and to
#       export a CSV of what the user needs to order
# os - Used for listing the .csv files found in a folder.
# os.path - Used for finding the .csv files needed for the search.
# requests - Used to GET the GTS Distribution search.


def start_search():

    # Runs each function of the search

    file_results = find_file()

    to_find = open_csv(file_results)

    found = find_products(to_find)

def find_file():

    # finds all .csv files in the folder and asks the user which file
    # to load.

    # Returns the name of that file

    csv_files = [file for file in os.listdir() if file.endswith('.csv')]
    # Builds a list of every .csv file in the same folder as this script.

    to_load = ''

    csv_len = len(csv_files)

    if csv_len > 1:

        for i in range(csv_len):

            print('{}. - {}'.format(i, csv_files[i]))

        while True:

            try:

                print('Please choose which file you would like to use')
                choice = int(input('> '))

                if choice > csv_len:

                    print('Choice greater than number of options')

                    continue

                else:

                    print('You have chosen {}'.format(csv_files[choice]))

                    to_load = csv_files[choice]

                    break

            except ValueError:

                print('Choice must be a number!')

                continue

    else:

        to_load = csv_files[0]

    print('{} has been loaded.'.format(csv_files[0]))

    return to_load

def open_csv(file):

    # Open's the csv file to be used in the search

    # file - the name of the csv file to be read

    # Returns a list of tuples that contain the UPC, Item Names, and Quantity
    #   needed to be searched on GTS's website.

    with open(file, newline='') as search_csv:

        reader = csv.reader(search_csv, delimiter=',',quotechar='|')
        
        to_search = [(row[1], row[5], row[9]) for row in reader]
        # creates a list of tuples that correspond to rows of the csv file read
    
        # row[1] = UPC
        # row[5] = Item Name
        # row[9] = Quantity Needed

    return to_search

def find_products(item_info):

    # Takes the info from the loaded CSV and searches for in stock items

    # item_info - a list of tuples that contain the UPC, Item Name, and
    #               Quantity Needed, in that order
    #               [0] = UPC, [1] = Name, [2] = Quantity Needed

    # Returns...

    for item in item_info:

        upc = item[0]

        print(upc)
        
        res = requests.get('https://www.gtsdistribution.com/pc_combined_results.asp?search_keyword={}'.format(upc))

        try:

            res.raise_for_status()

        except Exception as exc:

            print('There was a promlem: {}'.format(exc))

if __name__ == '__main__':

    start_search()
