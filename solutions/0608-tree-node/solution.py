import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:

    tree['type'] = 'Inner'
    tree.loc[tree['p_id'].isna(), 'type'] = 'Root'

    tree.loc[~tree['id'].isin(tree['p_id'].dropna()), 'type'] = 'Leaf'
    if len(tree) == 1:
        tree.loc[0, 'type'] = 'Root'
    
    return tree[['id', 'type']]

