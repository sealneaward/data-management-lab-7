-- Table: players

-- DROP TABLE players;


CREATE TABLE `nba`.`players` (
	        BLK int,
          DEF_RIM_FGA float,
          DEF_RIM_FGM int,
          DEF_RIM_FG_PCT float,
          DREB int,
          GP int,
          L int,
          MIN int,
          PLAYER_ID int,
          PLAYER_NAME varchar(255),
          STL int,
          TEAM_ABBREVIATION varchar(50),
          TEAM_ID int,
          W int,
	PRIMARY KEY(PLAYER_ID)
);
