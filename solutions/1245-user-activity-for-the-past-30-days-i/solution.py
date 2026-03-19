import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    start = "2019-06-28"
    end = "2019-07-27"

    df = activity[(activity["activity_date"] >= start) & 
                  (activity["activity_date"] <= end)]

    result = (
        df.groupby("activity_date",as_index=False)["user_id"]
        .nunique()
        # .reset_index()
        .rename(columns={
            "activity_date": "day",
            "user_id": "active_users"
        })
    )

    return result
    
