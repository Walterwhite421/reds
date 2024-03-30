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


def fetch_statcast_info(player_name, start_date, end_date):
    try:
        # Call playerid_lookup function for the player
        player_info = playerid_lookup(last=player_name.split()[-1], first=player_name.split()[0])
        player_id = player_info['key_mlbam'].iloc[0]

        # Check if the player is a pitcher or a batter
        if player_info['mlb_pos'].iloc[0] == 'P':
            # Call statcast_pitcher function for the pitcher
            statcast_info = statcast_pitcher(start_dt=start_date, end_dt=end_date, player_id=player_id)
        else:
            # Call statcast_batter function for the batter
            statcast_info = statcast_batter(start_dt=start_date, end_dt=end_date, player_id=player_id)

        # Print the statcast information for the player
        print(f"Statcast information for {player_name}:")
        print(statcast_info)
        print()

    except Exception as e:
        print(f"Error fetching data for {player_name}: {e}")

def main():
    # List of players and their corresponding date range
    players = {
        'Jake Fraley': ('2024-03-28', '2024-11-02'),
        'Jonathan India': ('2024-03-28', '2024-11-02'),
        'Christian Encarnacion-Strand': ('2024-03-28', '2024-11-02'),
        'Tyler Stephenson': ('2024-03-28', '2024-11-02'),
        'Elly De La Cruz': ('2024-03-28', '2024-11-02'),
        'Jeimer Candelario': ('2024-03-28', '2024-11-02'),
        'Spencer Steer': ('2024-03-28', '2024-11-02'),
        'Will Benson': ('2024-03-28', '2024-11-02'),
        'Nick Martin': ('2024-03-28', '2024-11-02')
    }

    for player, date_range in players.items():
        fetch_statcast_info(player, date_range[0], date_range[1])


    




if __name__ == "__main__":
    main()
