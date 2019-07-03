import re
import requests
from bs4 import BeautifulSoup
import csv
from more_itertools import unique_everseen

poet_list = []
number_of_poems_list = []
#poet_dictionary = {'poet':[poet_list], 'number_of_poems':[number_of_poems_list]}
#poet_list = [poet]
#number_of_poems_list =[str(len(poem_urls))]

# URLS = [
#     'https://www.poetryfoundation.org/poets/browse#page=224&sort_by=last_name&preview=0',
# ]
# for url in URLS:

url_base = 'https://www.poetryfoundation.org/poets/browse#page='
url_end = '&sort_by=last_name'

for page_number in range(1):
    page_number = str(page_number)
    url = url_base + page_number + url_end
    #print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    umbrella_dictionary = {}
    poet_dictionary = {}
    for link in links:
        link_url = link.get('href')
        # print(link_url)
        link_url_base_good = 'https://www.poetryfoundation.org/poets/'
        if link_url.startswith(link_url_base_good):
            poet = link_url.replace(link_url_base_good, '')
            # print(poet)
            poem_urls = []
            response = requests.get(link_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            # print(links)
            for link in links:
                poem_url = link.get('href')
                digits_in_url = re.findall(r'\d+', poem_url)
                is_a_browse_url = 'poems/browse' in poem_url
                if '/poems/' in poem_url and not is_a_browse_url and digits_in_url != []:
                    poem_urls.append(poem_url)
                    # print(poem_url)
                    # print(digits_in_url)
                #print(link.href)
            #print(len(poem_urls))
            #print(poet + ' - ' + str(len(poem_urls)))
            poet_list.append(poet)
            number_of_poems_list.append(len(poem_urls))

            umbrella_dictionary[poet] = poet_dictionary
            poet_dictionary['number_of_poems'] = (len(poem_urls))
print(umbrella_dictionary)

            #poet_dictionary['poet_attributes'] = {}
            #poet_dictionary['poet_attributes']['number_of_poems'] = [number_of_poems_list]
            #poet_dictionary['poet'] = [poet_list]

            #poet_dictionary = {'poet':[poet_list], 'attributes':{poet_attributes} }
            #poet_attributes = {'number_of_poems':[number_of_poems_list], 'text_of_poems':''}
            
#print(poet_dictionary)

            #>>> d = {}
            #>>> d['dict1'] = {}
            #>>> d['dict1']['innerkey'] = 'value'
            #>>> d
            #{'dict1': {'innerkey': 'value'}}

            #filename = 'Top_Poets' + '.csv'
            #with open(filename, 'a') as file:

                #f = open(filename, "a", newline="") leave this hashed

                #c = csv.writer(file)
                #poet_list = poet
                #number_of_poems_list = (len(poem_urls))
                #c.writerow([poet_list, number_of_poems_list])

                #print('Wrote file to ' + filename) leave this hashed
                #from more_itertools import unique_everseen leave this hashed 

                #with open('Top_Poets.csv','r') as f, open('Top_Poets_No_Duplicates.csv','w') as out_file:
                    #out_file.writelines(unique_everseen(f))



#for url in URLS:
   # why is this a syntax error
   #response = requests.get(url)
   #filename = url.replace('https://', '') + '.csv'
   #with open(filename, 'w') as f:
     #   f.write(response.text)
    #    print('Wrote file to ' + filename)
    
    # GOAL: print all links from each url

    # TODO: learn how to create a function
    #links_to_poet_profiles = find_links_to_poet_profiles(links)

# TODO 
#do the URL
#get all the poets' names
    #use beautiful soup to find links in the html
    # you can always at a later point discern what links you want and what links you don't want
#fill in the poets' poems' list url with the poets' names: - [https://www.poetryfoundation.org/poets/FIRSTNAME-LASTNAME#tab-poems]
# write csv with one poet per row and number of poems (links) by poet from poets' poems' list url

    
