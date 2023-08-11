import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Add a new series to tweets df containing len of each value in "content" series 
    tweets["char_len"] = tweets["content"].str.len()
    
    # Determine which tweet content > 15 chars
    answr = tweets[(tweets["char_len"] > 15)]

    # Return a df of invalid tweet_ids 
    return answr[["tweet_id"]]
