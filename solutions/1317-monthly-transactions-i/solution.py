import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.copy()
    transactions['month'] = transactions['trans_date'].dt.to_period('M').astype(str)
    transactions['is_approved'] = transactions['state'] == 'approved'
    transactions['approved_amount'] = transactions['amount'] * transactions['is_approved']
    df=transactions.groupby(['month', 'country'], as_index=False, dropna=False).agg(
        trans_count=('id', 'count'),
        approved_count=('is_approved', 'sum'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('approved_amount', 'sum')
    )
    return df
