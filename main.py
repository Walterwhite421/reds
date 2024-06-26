#!/usr/bin/env python3

from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_batter
from pybaseball import standings
from pybaseball import schedule_and_record
from pybaseball.team_pitching import team_pitching_bref  # Importing the team_pitching_bref function
from pybaseball.team_batting import team_batting_bref # Importing the team_batting_bref function

def get_player_statistics(pitcher_last_name, batter_last_name):
    try:
        # Call playerid_lookup function for pitcher
        pitcher_info = playerid_lookup(last=pitcher_last_name)
        pitcher_id = pitcher_info['key_mlbam'].iloc[0]

        # Call statcast_pitcher function for pitcher
        pitcher_statcast_info = statcast_pitcher(start_dt='2024-03-28', end_dt='2024-11-02', player_id=pitcher_id)

        # Print the statcast information for pitcher
        print(f"\nStatcast information for {pitcher_last_name}:")
        print(pitcher_statcast_info)
        print()
    except Exception as e:
        print(f"Error fetching data for {pitcher_last_name}: {e}")

    try:
        # Call playerid_lookup function for batter
        batter_info = playerid_lookup(last=batter_last_name)
        batter_id = batter_info['key_mlbam'].iloc[0]

        # Call statcast_batter function for batter
        batter_statcast_info = statcast_batter(start_dt='2024-03-28', end_dt='2024-11-02', player_id=batter_id)

        # Print the statcast information for batter
        print(f"\nStatcast information for {batter_last_name}:")
        print(batter_statcast_info)
    except Exception as e:
        print(f"Error fetching data for {batter_last_name}: {e}")

def main():
    # Fetch standings for the Reds division in a specific season
    standings_data = standings(2024)  # Change the year accordingly
    reds_standings = standings_data[4]  # Assuming the Reds are in the fifth division
    print("\nStandings for the Reds division:")
    print(reds_standings)

    pitcher_last_name = input("Enter pitcher's last name: ")
    batter_last_name = input("Enter batter's last name: ")
    get_player_statistics(pitcher_last_name, batter_last_name)

    try:
        # Call playerid_lookup function for batter
        batter_info = playerid_lookup(last=batter_last_name)
        batter_id = batter_info['key_mlbam'].iloc[0]

        # Call statcast_batter function for batter
        batter_statcast_info = statcast_batter(start_dt='2024-03-28', end_dt='2024-11-02', player_id=batter_id)

        # Print the statcast information for batter
        print(f"\nStatcast information for {batter_last_name}:")
        print(batter_statcast_info)
    except Exception as e:
        print(f"Error fetching data for {batter_last_name}: {e}")




    try:
        # Get team batting data for the Reds
        reds_batting_data = team_batting_bref(team='CIN', start_season=2024, end_season=2024)
        print("\nTeam batting data for the Reds:")
        print(reds_batting_data)

    except Exception as e:
        print(f"Error fetching team batting data for the Reds: {e}")
    try:
         # Get team pitching data for the Reds
         reds_pitching_data = team_pitching_bref(team='CIN', start_season=2024, end_season=2024)
         print("\nTeam pitching data for the Reds:")
         print(reds_pitching_data)

    except Exception as e:
         print(f"Error fetching team pitching data for the Reds: {e}")


    try:
        # Call playerid_lookup function for Frankie Montas
        player_info_montas = playerid_lookup(last='montas', first='frankie')
        player_id_montas = player_info_montas['key_mlbam'].iloc[0]

        # Call statcast_pitcher function for Frankie Montas
        statcast_info_montas = statcast_pitcher(start_dt='2024-03-28', end_dt='2024-11-02', player_id=player_id_montas)

        # Print the statcast information for Frankie Montas
        print("Statcast information for Frankie Montas:")
        print(statcast_info_montas)
        print()
    except Exception as e:
        print(f"Error fetching data for Frankie Montas: {e}")

    try:
        # Call playerid_lookup function for Graham Ashcraft
        player_info_ashcraft = playerid_lookup(last='ashcraft', first='graham')
        player_id_ashcraft = player_info_ashcraft['key_mlbam'].iloc[0]

        # Call statcast_pitcher function for Graham Ashcraft
        statcast_info_ashcraft = statcast_pitcher(start_dt='2023-04-20', end_dt='2023-09-28', player_id=player_id_ashcraft)

        # Print the statcast information for Graham Ashcraft
        print("Statcast information for Graham Ashcraft:")
        print(statcast_info_ashcraft)
        print()
    except Exception as e:
        print(f"Error fetching data for Graham Ashcraft: {e}")

    try:
        # Call playerid_lookup function for Hunter Greene
        player_info_greene = playerid_lookup(last='greene', first='hunter')
        player_id_greene = player_info_greene['key_mlbam'].iloc[0]

        # Call statcast_pitcher function for Hunter Greene
        statcast_info_greene = statcast_pitcher(start_dt='2024-03-28', end_dt='2024-11-02', player_id=player_id_greene)

        # Print the statcast information for Hunter Greene
        print("Statcast information for Hunter Greene:")
        print(statcast_info_greene)

    except Exception as e:
        print(f"Error fetching data for Hunter Greene: {e}")



    try:
        # Call playerid_lookup function for Jake Fraley
        player_info_fraley = playerid_lookup(last='fraley', first='jake')
        player_id_fraley = player_info_fraley['key_mlbam'].iloc[0]

        # Call statcast_batter function for Jake Fraley
        statcast_info_fraley = statcast_batter(start_dt='2024-03-28', end_dt='2024-11-02', player_id=player_id_fraley)

        # Print the statcast information for Jake Fraley
        print("Statcast information for Jake Fraley:")
        print(statcast_info_fraley)

    except Exception as e:
        print(f"Error fetching data for Jake Fraley: {e}")


    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
