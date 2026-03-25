import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales_small = sales[['product_id', 'year', 'price']].set_index('product_id')
    product_small = product[['product_id', 'product_name']].set_index('product_id')
    
    return sales_small.join(product_small)
