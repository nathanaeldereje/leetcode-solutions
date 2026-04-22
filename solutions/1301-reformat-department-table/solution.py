import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    result = department.pivot_table(
        index='id',
        columns='month',
        values='revenue',
        aggfunc='sum'
    ).rename(columns=lambda x: f"{x}_Revenue").reset_index()
    months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

    result = result.reindex(columns=['id'] + [f"{m}_Revenue" for m in months])
    return result
