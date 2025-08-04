import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if logs.empty:
        return pd.DataFrame({'ConsecutiveNums': []})

    logs['change'] = logs['num'] != logs['num'].shift()
    logs['change'][0]=True
    logs['group_id'] = logs['change'].cumsum()
    group_sizes = logs.groupby('group_id').size()
    large_groups = group_sizes[group_sizes >= 3].index
    result = logs[logs['group_id'].isin(large_groups)].groupby('group_id').first()['num'].unique()
    # unique_nums = result.unique()

    # return pd.DataFrame({'ConsecutiveNums': logs['']})
    return pd.DataFrame({'ConsecutiveNums': result})

