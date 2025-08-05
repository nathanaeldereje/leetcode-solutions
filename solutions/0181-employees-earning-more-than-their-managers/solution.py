import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee, how='inner', left_on='managerId', right_on='id', suffixes=('_emp', '_mgr'))
    result = merged[merged['salary_emp'] > merged['salary_mgr']][['name_emp']]
    result.columns = ['Employee']

    return(result)
