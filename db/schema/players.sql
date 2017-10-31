-- Table: players

-- DROP TABLE players;

CREATE TABLE players
(
  "PLAYER_ID" bigint NOT NULL,
  "PLAYER_NAME" text,
  "TEAM_ID" bigint,
  "TEAM_ABBREVIATION" text,
  "GP" bigint,
  "W" bigint,
  "L" bigint,
  "MIN" double precision,
  "STL" bigint,
  "BLK" bigint,
  "DREB" bigint,
  "DEF_RIM_FGM" bigint,
  "DEF_RIM_FGA" bigint,
  "DEF_RIM_FG_PCT" double precision,
  CONSTRAINT hustle_overall_pkey PRIMARY KEY ("PLAYER_ID")
)
WITH (
  OIDS=FALSE
);
