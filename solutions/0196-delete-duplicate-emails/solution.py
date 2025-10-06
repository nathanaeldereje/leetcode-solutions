import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Keep first occurrence of each duplicated email, and all non-duplicated emails
    # max_ids = person.groupby('email')['id'].transform('min')
    # mask = person['id'] == max_ids
    # person.drop(person.index[~mask], inplace=True)
    person.sort_values('id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


