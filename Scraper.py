from bs4 import BeautifulSoup
import requests

account_name=str(input('Enter your account name: '))
account_tag=str(input('Enter your account tag: '))

if account_name=='':
    account_name='Aatricks'
if account_tag=='':
    account_tag='EUW'

column1 = ['Iron 1', 'Iron 2', 'Iron 3', 'Bronze 1', 'Bronze 2', 'Bronze 3', 'Silver 1', 'Silver 2', 'Silver 3', 'Gold 1', 'Gold 2', 'Gold 3', 'Platinum 1', 'Platinum 2', 'Platinum 3', 'Diamond 1', 'Diamond 2', 'Diamond 2', 'Ascendant 1', 'Ascendant 2', 'Ascendant 3', 'Immortal 1', 'Immortal 2', 'Immortal 3', 'Radiant']
column2 = [99.7, 99.3, 97.6, 93.1, 88, 81.6, 75, 66.9, 59.3, 51.6, 44.1, 37.4, 31.3, 25.5, 20.6, 16.2, 12.2, 8.9, 6.3, 4.2, 2.7, 1.6, 0.6, 0.2, 0.04]

def percentage(rank,column1,column2):
    for i in range(25):
        if rank==column1[i]:
            print('You are in the top '+str(column2[i])+'% of players')
        else:
            pass

url='https://tracker.gg/valorant/profile/riot/'+account_name+'%23'+account_tag+'/overview?playlist=competitive&season=all'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

# Get the peak rating
peak_rating=soup.find_all('div',class_='rating-summary__content rating-summary__content--secondary')

for i in peak_rating:
    #img=i.find('img')
    #print(img['src'])
    rank=i.find('div',class_='value')
    season=i.find('div',class_='subtext')
    print('\n')
    print(account_name+'#'+account_tag + ' peak rating : ' + '\n')
    print(rank.text)
    print(season.text+'\n')


soup2=BeautifulSoup('<span data-v-263291e0="" class="heading__players"> 9 755 519 Players </span>','lxml')
percentage(rank.text,column1,column2)
print('in a spectre of'+soup2.text)

def table(column1, column2):
    print("|    Ranks     |  percentage  |")
    print("|--------------|--------------|")
    for i in range(25):
        print("| {:12} | {:12} |".format(column1[i], column2[i]))

t=input('Do you want to see the rank percentage table? (y/n) : ')
if t=='y':
    table(column1,column2)
else:
    pass