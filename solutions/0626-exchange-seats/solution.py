import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    even_idx = seat.index[::2]
    odd_idx = seat.index[1::2]

    even_idx = even_idx[:len(odd_idx)]


    # use a temporary array to swap
    temp = seat.loc[even_idx, 'student'].values.copy()
    seat.loc[even_idx, 'student'] = seat.loc[odd_idx, 'student'].values
    seat.loc[odd_idx, 'student'] = temp

    return seat

