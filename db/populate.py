import pandas
import requests
from sqlalchemy import create_engine
from urls import urls


class Populate:
    def __init__(self):
        self.engine = create_engine('postgresql://root:root@localhost:5432/nba')

    def populate(self):
        # gets players and writes to sql, replacing if table exists
        players = get_dataframe_from_response(urls[0])
        players.to_sql('players', con=self.engine, if_exists='replace', index=False)

        # gets teams and writes to sql, replace if table exists (if you want to append to the table, use if_exists='append')
        teams = get_dataframe_from_response(urls[1])
        # I only want to store certain columns
        teams = teams.loc[:, ['TEAM_ID', 'TEAM_NAME']]
        teams.to_sql('teams', con=self.engine, if_exists='replace', index=False)

def get_dataframe_from_response(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    # any response other than 200 is an error
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pandas.DataFrame(data, columns=headers)

    return frame

populate = Populate()
populate.populate()
