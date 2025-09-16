import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(bonus, on="empId", how="left")
    return merged.loc[(merged["bonus"].lt(1000)) | merged["bonus"].isnull(), ["name", "bonus"]]


