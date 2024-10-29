from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
## Enter parameters
soup = BeautifulSoup(page.text, 'lxml')
## Find the right table and extract titles
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

### Create a data frame to save the data 
df = pd.DataFrame(columns = world_table_titles)

## Find the values of the columns using a loop
column_data = table.find_all('tr')

## [1:0] eliminates the top row if needed
for row in column_data[1:]:
    row_data = row.find_all('td')
    Individual_row_data = [data.text.strip() for data in row_data]
    print(Individual_row_data)
## The below part appends the values to the existing data frame with tittles
    lenght = len(df)
    df.loc[lenght] = Individual_row_data

## df.to_csv created a csv file and then youc an specify the location to save the file, index=false deletes the added index column
    df.to_csv(r'C:\Users\jespinoza\Desktop\Python\Wikipedia\Wikipedia.csv', index = False)

   



