import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
     manager_ids = employee['managerId'].value_counts().loc[lambda x: x >= 5].index
     return employee.loc[employee['id'].isin(manager_ids), ['name']]

    
