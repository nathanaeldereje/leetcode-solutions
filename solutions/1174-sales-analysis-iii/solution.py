import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    outside_q1 = sales[(sales['sale_date'] < '2019-01-01') | 
                        (sales['sale_date'] > '2019-03-31')]
    outside_ids = outside_q1['product_id'].unique()  
    inside_q1 = sales[sales['sale_date'].between('2019-01-01', '2019-03-31')]
    inside_ids = inside_q1['product_id'].unique()
    only_q1_ids = [pid for pid in inside_ids if pid not in outside_ids]
    result = product[product['product_id'].isin(only_q1_ids)]
    return result[['product_id','product_name']]
