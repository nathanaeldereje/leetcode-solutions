import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # Boolean masks (avoid creating multiple DataFrames)
    has_dup_tiv = insurance.duplicated('tiv_2015', keep=False)
    has_dup_loc = insurance.duplicated(['lat', 'lon'], keep=False)
    
    # Apply both conditions directly
    filtered = insurance[has_dup_tiv & ~has_dup_loc]
    
    # Compute rounded sum
    total = round(filtered['tiv_2016'].sum(), 2)
    
    return pd.DataFrame({'tiv_2016': [total]})

