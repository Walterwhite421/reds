from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

def main():
    # Call playerid_lookup function for Clayton Kershaw
    player_info = playerid_lookup(last='kershaw', first='clayton')


    # Extract the MLBAM ID (key_mlbam) from the player_info DataFrame
    player_id = player_info['key_mlbam'].iloc[0]

    # Call statcast_pitcher function for Clayton Kershaw
    statcast_info = statcast_pitcher(start_dt='2023-04-20', end_dt='2023-09-28', player_id=player_id)

    # Print the statcast information
    print(statcast_info)

if __name__ == "__main__":
    main()
