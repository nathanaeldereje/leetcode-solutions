import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    cutoff = '2019-08-16'
    valid = products[products['change_date'] <= cutoff]
    last_prices = valid.sort_values('change_date').groupby('product_id').tail(1)
    all_products = products[['product_id']].drop_duplicates()

    df = all_products.merge(
        last_prices[['product_id', 'new_price']],
        on='product_id',
        how='left'
    )
    df['price'] = df['new_price'].fillna(10)
    return df[['product_id','price']]
