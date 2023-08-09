import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Change values in 'users["name"]' to ensure they follow standard capitalization

    names = users["name"].tolist()

    for name in names:
        # Check for names with improper capitalization 
        if name != name.capitalize():
            # Fix capitalization of name inside OG df
            users = users.replace(to_replace=name, value=name.capitalize())


    return users.sort_values("user_id")
