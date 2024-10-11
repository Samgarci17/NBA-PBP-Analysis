'''
def: Script that scrapes the largest lead and largest comeback(lead change) of every playoff game from 1997-2024 by using bs4 to parse the html of bbal-ref and pandas to store the data as a dataframe and then csv
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re

years = list(range(1997,2025))
playoffComebacks = pd.DataFrame(index=range(105), columns=years)
playoffLeads = pd.DataFrame(index=range(105), columns=years) 
'''
def: Obtain the links to every playoff series from 1997 to 2024 by reading 'https://www.basketball-reference.com/playoffs/series.html' using bs4. 

in: None

out: List of strings, strings are hrefs leading to playoff series from 1997-2024
'''
def getPlayoffSeries():
    playoff_series = []

    url = 'https://www.basketball-reference.com/playoffs/series.html'

    # Send a GET request to the URL
    response = requests.get(url)
    time.sleep(7)

    # Check if the request was successful 
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all(id="playoffs_series")
        rows = table[0].find_all('tr')
        rows.pop(0)
        rows.pop(0)
        rows = rows[:447]
        for row in rows:
            cells = row.find_all('td', attrs={"data-stat": "series"})
            for cell in cells:
                a = cell.find_all('a')
                playoff_series.append(a[0].get('href'))
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

    return playoff_series

'''
def: Using bs4 to find the play-by-play table, getBoxscore tracks the largest comeback and largest lead of the game.

in: string

out: two tuples, the largest lead and largest comeback of the game with their corresponding bball-reference game id. ex largestLead = (14, '201804220WAS')
'''
def getBoxscore(url):
    #current score
    lead = 0
    #the largest lead since the last lead change
    prev_lead = 0 
    largest_lead = 0 
    largest_comeback = 0 
    
    response = requests.get(url)
    time.sleep(7)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find_all(id='pbp')
    table = table[0].find_all('tr')
    for row in table[1:]:  # Skip the header row
        if row.find('td', class_='bbr-play-score'):
            if row.find('td', class_='center'):
                score = row.find('td', class_='center')
                pattern = re.compile(r'(\d+)([-])(\d+)')
                match = pattern.match(score.text)
                num1 = int(match.group(1))
                num2 = int(match.group(3))
                lead = num1 - num2

        if abs(lead) > largest_lead:
            largest_lead = abs(lead)
        
        if abs(lead) > abs(prev_lead):
            prev_lead = lead

        #if a lead is erased or a lead change occurs, save the lead if it was larger than the current largest comeback
        if (lead == 0) or ((lead * prev_lead) < 0):
            if largest_comeback < abs(prev_lead):
                largest_comeback = abs(prev_lead)
                prev_lead = lead


    return largest_comeback, largest_lead

'''
def: Uses bs4 to create a list containing hrefs leading to the correspoding games of each playoff series. getBoxscore is then called to obtain the largest lead and comeback for each playoff game. They are then stored in the two lists lead_per_playoffs and comeback_per_playoffs. The lists are stored as columns in the playoffLeads and playoffComebacks dataframes with their labels as the corresponding playoff year. 

in: list of strings containing hrefs to bball-reference playoff series

out: None
'''
def getSeries(playoff_urls):
    lead_per_playoffs = []
    comeback_per_playoffs = []
    i = 0
    year = 2024
    for series_url in playoff_urls:
        i += 1
        url = 'https://www.basketball-reference.com'+series_url
        response = requests.get(url)
        time.sleep(7)
        if response.status_code != 200:
            print('Failed to retrieve the webpage. Status code:', response.status_code, response)
            
        soup = BeautifulSoup(response.content, 'html.parser')

        #game_list contains the list of games in the playoff series obtained from url in playoff_urls
        game_list = soup.find_all(class_='gamelink')
        for game in game_list:
            a = game.find_all('a')
            link = a[0].get('href')
            link = link[11:]
            gameurl = 'https://www.basketball-reference.com/boxscores/pbp/'+link
            comeback, lead = getBoxscore(gameurl)
            
            game_name = link[:-5]
            comeback_per_playoffs.append(int(comeback))
            lead_per_playoffs.append(int(lead))

        if i%15 == 0:
            while len(comeback_per_playoffs) < 105:
                comeback_per_playoffs.append(None)
            while len(lead_per_playoffs) < 105:
                lead_per_playoffs.append(None)  
            playoffLeads[year] = lead_per_playoffs
            playoffComebacks[year] = comeback_per_playoffs
            year -= 1
            lead_per_playoffs.clear()
            comeback_per_playoffs.clear()
        print('finished playoff series')
            

getSeries(getPlayoffSeries())
playoffComebacks.to_csv('playoffComebacks.csv', index=False)
playoffLeads.to_csv('playoffLeads.csv', index=False)
