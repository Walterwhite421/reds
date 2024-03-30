from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import standings
def main():
    # Call playerid_lookup function for Clayton Kershaw
    player_info_kershaw = playerid_lookup(last='kershaw', first='clayton')
    player_id_kershaw = player_info_kershaw['key_mlbam'].iloc[0]

    # Call statcast_pitcher function for Clayton Kershaw
    statcast_info_kershaw = statcast_pitcher(start_dt='2023-04-20', end_dt='2023-09-28', player_id=player_id_kershaw)

    # Print the statcast information for Clayton Kershaw
    print("Statcast information for Clayton Kershaw:")
    print(statcast_info_kershaw)
    print()

    # Call playerid_lookup function for Hunter Greene
    player_info_greene = playerid_lookup(last='greene', first='hunter')
    player_id_greene = player_info_greene['key_mlbam'].iloc[0]

    # Call statcast_pitcher function for Hunter Greene
    statcast_info_greene = statcast_pitcher(start_dt='2023-04-20', end_dt='2023-09-28', player_id=player_id_greene)

    # Print the statcast information for Hunter Greene
    print("Statcast information for Hunter Greene:")
    print(statcast_info_greene)

    # Fetch standings for the Reds division in a specific season
    standings_data = standings(2024)  # Change the year accordingly
    reds_standings = standings_data[4]  # Assuming the Reds are in the fifth division
    print("\nStandings for the Reds division:")
    print(reds_standings)

if __name__ == "__main__":
    main()


