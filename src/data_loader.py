import requests
import pandas as pd

def load_fpl_data():
    """
    Loads current FPL player data from the official FPL API.
    Returns a pandas DataFrame.
    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()
    players_df = pd.DataFrame(data['elements'])
    return players_df

if __name__ == "__main__":
    df = load_fpl_data()
    print(df[['first_name', 'second_name', 'form', 'total_points']].head())
