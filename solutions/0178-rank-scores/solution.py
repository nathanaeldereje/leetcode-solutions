import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort by 'score' descending
    ordered = scores[['score']].sort_values('score', ascending=False)
    # Assign ranks (dense ranking, higher scores get lower rank numbers)
    ordered['rank'] = ordered['score'].rank(method='dense', ascending=False).astype(int)
    return ordered

