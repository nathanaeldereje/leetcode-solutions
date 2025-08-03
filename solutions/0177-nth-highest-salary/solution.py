import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = sorted(employee['salary'].unique(), reverse=True)
    col_name = f'getNthHighestSalary({N})'  # dynamic column name
    if N <= len(unique_salaries) and N>0:
        return pd.DataFrame({col_name: [unique_salaries[N - 1]]})
    else:
        return pd.DataFrame({col_name: [None]})

