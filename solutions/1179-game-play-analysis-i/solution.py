import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    groupped = activity.groupby('player_id', as_index=False)['event_date'].min()
    groupped.rename(columns={'event_date': 'first_login'}, inplace=True)
    return groupped

