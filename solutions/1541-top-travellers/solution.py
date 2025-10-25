import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:

    rides_group = rides.groupby('user_id', as_index=False)['distance'].sum()
    merged = users.merge(rides_group, how='left', left_on='id', right_on='user_id')
    merged['distance'] = merged['distance'].fillna(0)
    merged = merged.sort_values(['distance', 'name'], ascending=[False, True])
    return merged[['name', 'distance']].rename(columns={'distance': 'travelled_distance'})

