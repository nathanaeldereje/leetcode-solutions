import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['poor_query_percentage'] = queries['rating'] < 3
    queries['quality']=(queries['rating']/queries['position'])
    df = queries.groupby('query_name', as_index=False)[
        ['quality', 'poor_query_percentage']
    ].mean()

    df['poor_query_percentage'] = (df['poor_query_percentage'] * 100).round(2)
    df['quality'] = (df['quality'] + 1e-9).round(2)
    return df

