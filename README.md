# NBA_Stats
Python Webscraper - www.stats.nba.com
Utilizing Python 3.6, panda, numpy, request, and bs4 to scrape www.stats.nba.com data for all active roster players of preferred team, 
__V.0.1 - Current features:__
- Can compile dataframe of (almost) all active roster players in NBA, including player total stats to .csv file.
__File Descriptions:__
- FetchData.py:
  * Function that takes team name ('spurs', 'blazers', etc. in this format) as input, and returns a
    pandas data frame for that team's player statistics.
- FetchAllTeams.py:
  * Utilizes the function in FetchData.py, iterating through an array of all 30 team names.(*ahem*, 29 actually. Thanks Dallas..)
  * Compiles a single dataframe containing all player information for the following statistics: 
    - Games Played
    - Points (total)
    - Feild Goals (total)
    - Feild Goal %
    - 3 Point %
    - Free-throw %
    - Offensive Rebounds
    - Defensive Rebounds
    - Rebounds (total)
    - Assists
    - Steals
    - Turnovers
    - Personal Fouls
