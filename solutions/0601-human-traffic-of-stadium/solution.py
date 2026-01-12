import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    mask = stadium['people'] >= 100
    
    group_id = (mask != mask.shift(fill_value=False)).cumsum()
    print(group_id)
    group_counts = group_id.groupby(group_id).transform('count')

    return (
        stadium[mask & (group_counts >= 3)]
        [['id', 'visit_date', 'people']]
        .sort_values('visit_date')
    )

