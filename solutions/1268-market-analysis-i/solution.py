import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[
        (orders['order_date'] >= '2019-01-01') &
        (orders['order_date'] < '2020-01-01')
    ]
    orders_count = orders_2019.groupby('buyer_id')['order_id'].count()
    users['orders_in_2019'] = users['user_id'].map(orders_count).fillna(0)
    result = users.rename(columns={'user_id': 'buyer_id'})[
        ['buyer_id', 'join_date', 'orders_in_2019']
    ]
    
    return result
