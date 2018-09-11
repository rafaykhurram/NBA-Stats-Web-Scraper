import pandas as pd
import FetchData as fd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# fetches current snapshot of player stat totals for an NBA season for chosen team
loop = 1;

print("NBA Player Individual Total Statistics by Team")
while(loop==1):
    print()
    teams = input('Team Mascot?: ')

    year = input('NBA Season?(2014,2015,2016,2017,2018): ')
    if year == '2018':
        year = "2017-18"
    elif year == '2017':
        year = "2016-17"
    elif year == '2016':
        year = "2015-16"
    elif year == '2015':
        year = "2014-15"
    elif year == '2014':
        year = "2013-14"
    teams = teams.lower()
    if teams == 'wolves':
        teams = 'timberwolves'
        print("Minnesota Timberwolves:")
    elif teams == 'timberwolves':
        print("Minnesota Timberwolves:")
    elif teams == 'cavs':
        teams = 'cavaliers'
        print("Cleveland Cavaliers:")
    elif teams == 'cavaliers':
        print("Cleveland Cavaliers:")
    elif teams == 'celtics':
        print("Boston Celtics:")
    elif teams == 'hawks':
        print("Atlanta Hawks:")
    elif teams == 'nets':
        print("Brooklyn Nets:")
    elif teams == 'hornets':
        print("Charlotte Hornets:")
    elif teams == 'bulls':
        print("Chicago Bulls:")
    elif teams == 'cavaliers':
        print("Cleveland Cavaliers:")
    elif teams == 'nuggets':
        print("Denver Nuggets:")
    elif teams == 'spurs':
        print("San Antonio Spurs:")
    elif teams == 'blazers':
        print("Portland Trail Blazers:")
    elif teams == 'warriors':
        print("Golden State Warriors:")
    elif teams == 'thunder':
        print("Oklahoma City Thunder:")
    elif teams == 'clippers':
        print("Los Angeles Clippers:")
    elif teams == 'lakers':
        print("Los Angeles Lakers:")
    elif teams == 'pistons':
        print("Detroit Pistons:")
    elif teams == 'rockets':
        print("Houston Rockets:")
    elif teams == 'pacers':
        print("Indiana Pacers:")
    elif teams == 'grizzlies':
        print("Memphis Grizzlies:")
    elif teams == 'heat':
        print("Miami Heat:")
    elif teams == 'bucks':
        print("Milwaukee Bucks:")
    elif teams == 'pelicans':
        print("New Orleans Pelicans:")
    elif teams == 'knicks':
        print("New York Knicks:")
    elif teams == 'magic':
        print("Orlando Magic:")
    elif teams == '76ers':
        print("Philadelphia 76ers:")
        teams = 'sixers'
    elif teams == 'sixers':
        print("Philadelphia 76ers:")
    elif teams == 'suns':
        print("Phoenix Suns:")
    elif teams == 'kings':
        print("Sacramento Kings:")
    elif teams == 'raptors':
        print("Toronto Raptors:")
    elif teams == 'jazz':
        print("Utah Jazz")
    elif teams == 'wizards':
        print("Washington Wizards:")
    print()
    teams = [teams]
    # initializing data frame
    plyrDataFrame = pd.DataFrame()

    # running nbaTeamStats func & iterating through teams
    for i in teams:
        plyrDataFrame = plyrDataFrame.append(fd.nbaTeamStats(i, year))

    # writing .csv for external analysis
        plyrDataFrame.to_csv("NBA_Player_Stats.csv")

    # printing df for quick n' dirty view of pulled data
    print(plyrDataFrame)
    print();
    rerun=input("Run Again?(Y/N): ")

    rerun=rerun.lower()
    if rerun =='y':
        loop=1;
    elif rerun =='n':
        loop=0;