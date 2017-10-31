import psycopg2

class Connection:
    def __init__(self):
        con = psycopg2.connect(database='nba', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_players(self,team_id):
        self.cur.execute('select "PLAYER_ID","PLAYER_NAME" from players where "TEAM_ID" = %s', [team_id])
        return self.cur.fetchall()

    def get_stats(self,player_id):
        self.cur.execute('select * from players where "PLAYER_ID" = %s', [player_id])
        return self.cur.fetchall()

    def get_teams(self):
        self.cur.execute('select "TEAM_ID","TEAM_NAME" from teams')
        return self.cur.fetchall()
