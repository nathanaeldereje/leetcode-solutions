import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of each number
    counts = my_numbers['num'].value_counts()

    # Filter numbers that appear only once
    single_numbers = counts[counts == 1].index

    # Find the maximum of those numbers (if any)
    if len(single_numbers) == 0:
        return pd.DataFrame({'num': [None]})
    else:
        return pd.DataFrame({'num': [single_numbers.max()]})

