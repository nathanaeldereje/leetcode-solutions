import pandas as pd
import numpy as np

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    banned_ids = users[users['banned'] == 'Yes']['users_id']
    trips_filtered = trips[
        (trips['request_at'].between("2013-10-01", "2013-10-03")) & 
        (~trips['client_id'].isin(banned_ids)) & 
        (~trips['driver_id'].isin(banned_ids))
    ]
    trips_filtered['is_cancelled']=np.where(trips_filtered['status']=='completed', False, True)
    df = trips_filtered.groupby('request_at', as_index=False).agg(
        Day=('request_at', 'first'),
        # total_trips=('status', 'count'),
        cancelled=('is_cancelled','mean')
    )
    df['Cancellation Rate']=(df['cancelled']).round(2)
    return df[['Day','Cancellation Rate']]
    
