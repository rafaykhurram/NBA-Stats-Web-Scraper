import requests
import pandas as pd
from bs4 import BeautifulSoup

def nbaTeamStats(team, time):

    # requesting current statistics for SAS players
    ''' Note about the following link: any stat link on NBA.com can be interfaced
        with using this script. This includes all 29 other teams, as well as historical
        and playoff information, assuming previous team data is available through NBA.com'''

    url = requests.get("http://www.nba.com/" + team + "/stats/stats?season="+time+"&season_type=regular%20season")
    soup = BeautifulSoup(url.content, "html.parser")

    # list of column headers, these will be used to iterate through html tags
    # to find each player's statistics
    stat = ['gp', 'pts', 'fgm', 'fg_pct', 'fg3_pct',
            'ft_pct', 'oreb', 'dreb', 'reb', 'ast',
            'stl', 'tov', 'pf', 'team']

    # getting all player names
    playerName = []
    playerData = soup.find_all("td")
    for i in range(0, len(playerData)//2, 14): # every 14th "td" tag in playerData contains player name
        player = str(playerData[i])
        idx_s = player.find('ank">') + 5
        idx_e = player.find('</a')
        playerName.append(player[idx_s:idx_e])

    # initializing data frame, filling with NaN's
    # dataFrame index = player name, columns = stat names
    dataFrame = pd.DataFrame(index=playerName, columns=stat)
    dataFrame.fillna(1)

    # parsing html document and assigning statistics to data frame
    # by row (player index). Finding player statistics via columns (statistic) was
    # not possible without information loss, due to the lack of html class attributed with 'td'
    # tags containing information for statistics with null values. For example, David Lee's lack of 3pt %
    # causes each data point for 3pt % to be shifted, because Lee's lack of data isn't recorded.
    playerIndex = 0
    for i in playerName:
        playerIndex += 1
        playerRow = soup.find_all('tr')[playerIndex]

        for j in stat:
            temp = playerRow.find('td',j)
            dataFrame.set_value(i,j,temp) # setting dataFrame value to html slice

            # handling missing values for stats.
            if dataFrame.get_value(i,j) == None:
                dataFrame.set_value(i,j,'-') # '-' used to signify lack of data, this will be coerced to NaN
            else:
                dataFrame.set_value(i,j,str(temp.contents[0])) # parse html slice to pull relevant statistic
                # removing %'s from pct stats
                if '%' in dataFrame.get_value(i,j):
                    dataFrame.set_value(i,j,dataFrame.get_value(i,j).strip('%'))

    # converting data type to numeric
    dataFrame = dataFrame.apply(pd.to_numeric, errors='coerce')

    # converting percentages to decimals in columns 3, 4, and 5
    dataFrame.iloc[:, 3] = round((dataFrame.iloc[:,3] / 100), 3)
    dataFrame.iloc[:, 4] = round((dataFrame.iloc[:,4] / 100), 3)
    dataFrame.iloc[:, 5] = round((dataFrame.iloc[:,5] / 100), 3)

    # adding team name to dataframe
    dataFrame.loc[:,'team'] = team

    # displaying data frame and ensuring all columns are visible
    pd.set_option('display.width', 1000)



    return(dataFrame)
