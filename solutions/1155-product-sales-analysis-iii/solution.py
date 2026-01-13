import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales['first_year'] = sales.groupby('product_id')['year'].transform('min')
    result = sales[sales['year'] == sales['first_year']]
    return result[['product_id', 'first_year', 'quantity', 'price']]
