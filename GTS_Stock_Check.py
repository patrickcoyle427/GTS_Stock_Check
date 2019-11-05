#!/bin/usr/python3

'''
GTS_stock_check.py

NOTE: Will only work if the user is currently logged into GTS Distribution
        www.gtsdistribution.com

Loads a CSV file of products that need to be reordered, generated through lightspeed retail.

Searches GTS Distribution, a hobby and collectible distributor, to check if the product is in stock.
Output is a CSV file with the UPC, Name, and quanity to Order if the product is in stock.

'''

# TO DO:
# -Load the CSV File
# -Read the CSV File and pull out the desired info
# -Run a search of GTS: search URL is: https://www.gtsdistribution.com/pc_combined_results.asp?search_keyword=
#  -After the '=' put the upc of the item needed

import bs4, csv, requests, os.path

# requests - Used to GET the GTS Distribution search
# bs4 - Beautiful Soup to read the webpage received from the requests GET request
# csv - Used to read the Lightspeed retail generated CSV of products needed and to export a CSV of what
#       the user needs to order
# os.path - Used for finding the .csv files needed for the search

def start_search():

    pass

if __name__ == '__main__':

    start_search()
