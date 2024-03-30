from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_batter
from pybaseball import standings
from pybaseball import schedule_and_record

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
        # Call statcast_batter function for Reds batters
        reds_batter_data = statcast_batter('2024-03-28', '2024-09-28')

        # Filter data for Reds batters against specific teams
        reds_batter_vs_team = reds_batter_data[reds_batter_data['home_team'] == 'CIN']  # Assuming CIN is the team abbreviation for the Reds
        reds_batter_vs_team = reds_batter_vs_team.append(reds_batter_data[reds_batter_data['away_team'] == 'CIN'])

        # Print the statcast information for Reds batters against specific teams
        print("Statcast information for Reds batters against specific teams:")
        print(reds_batter_vs_team)
        print()
    except Exception as e:
        print(f"Error fetching data for Reds batters against specific teams: {e}")



if __name__ == "__main__":
    main()
