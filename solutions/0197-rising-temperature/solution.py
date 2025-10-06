import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',inplace=True)
    
    # Create boolean mask
    mask = (
        (weather['temperature'].shift(1) < weather['temperature']) &
        ((weather['recordDate'] - weather['recordDate'].shift(1)).dt.days == 1)
    )
    
    # Create filtered DataFrame with only Id
    return weather.loc[mask, ['id']].rename(columns={'id':'Id'})

