from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_batter
from pybaseball import standings
from pybaseball import schedule_and_record
from team_batting import team_batting_bref

def main():
    # Fetch standings for the Reds division in a specific season
    standings_data = standings(2024)  # Change the year accordingly
    reds_standings = standings_data[4]  # Assuming the Reds are in the fifth division
    print("\nStandings for the Reds division:")
    print(reds_standings)

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
        statcast_info_greene = statcast_pitcher(start_dt='2023-04-20', end_dt='2023-09-28', player_id=player_id_greene)

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

def main():
    # Fetch standings for the Reds division in a specific season
    standings_data = standings(2024)  # Change the year accordingly
    reds_standings = standings_data[4]  # Assuming the Reds are in the fifth division
    print("\nStandings for the Reds division:")
    print(reds_standings)

    try:
        # Call team_batting function for the Reds for a specific season
        reds_batting_stats = team_batting_bref('CIN', 2024)

        # Print the batting statistics for the Reds
        print("\nBatting statistics for the Reds:")
        print(reds_batting_stats)
        print()
    except Exception as e:
        print(f"Error fetching data for Reds batting statistics: {e}")

    # Other parts of your main function



if __name__ == "__main__":
    main()
