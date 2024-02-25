 
''' IMPORTS '''

# requests allows you to send HTTP requests
import requests 
# beautifulsoup pulls and organizes data from HTML file
from bs4 import BeautifulSoup 

''' DATA RETRIEVING AND PARSING '''

# Making a GET request 
r = requests.get('https://www.veganpeace.com/ingredients/ingredients.htm') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

# finds the data needed
s = soup.find('div', class_='main-wrap') 

lines = s.find_all('span') 

''' INITIALIZING VARIABLES '''

# user input
UserIngredient = input("Enter your ingredient: ").upper()

# bool to see if user input exists in data
isthere = False
  
''' LOOKING FOR USER INPUT IN DATA FROM WEBSITE '''

for i in lines: 

    # organizes data into ingredient and category
    line = i.text
    line = line.split("(")
    DataIngredient = ((line[0])[:-1:]).upper()
    DataCategory = (line[-1])[:-2:]

    # test
    print(DataIngredient)
    print(DataCategory)

    # compares ingredients
    if(UserIngredient == DataIngredient):
        isthere = True

''' CHECKS CATEGORY '''

# if data and user input match, check category
if(isthere):

    # A means animal product
    if(DataCategory == 'A'):

        print("Your ingredient is an animal product")

    # V means vegan
    elif(DataCategory == 'V'):

        print("Your ingredient is vegan")

    # B means can be animal or vegan product
    else:

        print("Your ingredient exists in both animal and vegan versions") 

# execute if ingredient was not found in data
else:
   
   print("Your ingredient is not found")
   
