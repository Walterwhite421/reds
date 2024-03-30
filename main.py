from pybaseball import playerid_lookup, statcast_pitcher, standings, schedule_and_record
import pandas as pd

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
        statcast_info_montas = statcast_pitcher(start_dt='2024-03-28', end_dt='2024-09-28', player_id=player_id_montas)

        # Print the statcast information for Frankie Montas
        print("Statcast information for Frankie Montas:")
        print(statcast_info_montas)
        print()

        # Filter columns related to 'spin' and 'spin rate'
        spin_columns = statcast_info_montas.filter(like='spin').columns

        # Select only the columns related to 'spin' and 'spin rate'
        spin_data = statcast_info_montas[spin_columns]

        # Print the DataFrame with spin-related columns
        print("Spin-related data for Frankie Montas:")
        print(spin_data)
        print()
    except Exception as e:
        print(f"Error fetching data for Frankie Montas: {e}")

    # Similarly, you can add code to fetch spin-related data for other pitchers

if __name__ == "__main__":
    main()
