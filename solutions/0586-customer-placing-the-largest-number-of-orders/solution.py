import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=orders.groupby('customer_number',as_index=False).size()
    max=df['size'].max()
    # print(df)
    return df[df['size']==max][['customer_number']]
