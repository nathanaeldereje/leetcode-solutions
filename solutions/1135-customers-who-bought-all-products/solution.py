def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = len(product)
    counts = customer.groupby('customer_id')['product_key'].nunique()
    return counts[counts == total_products].reset_index()[['customer_id']]

