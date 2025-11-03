import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    sent_counts = request_accepted['requester_id'].value_counts()
    received_counts = request_accepted['accepter_id'].value_counts()
    friend_counts = sent_counts.add(received_counts, fill_value=0)
    friend_counts = friend_counts.reset_index()
    friend_counts.columns = ['id', 'num']
    

    max_num = friend_counts['num'].max()
    return friend_counts[friend_counts['num'] == max_num]

