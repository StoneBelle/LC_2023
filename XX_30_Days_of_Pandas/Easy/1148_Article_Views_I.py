import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    # Given a df of containing data on articles, authors, viewer, & dates viewed
    # Df may contain duplicate rows
    # If author_id == viewer id that indicates it's the same person 
    # Return df with single series called "id" of author who viewed their work

    # Remove duplicates from orginal/current df
    views.drop_duplicates(inplace=True)

    # Check for author_ids & view_ids that match, and store in df
    answr = views[(views['author_id'] == views['viewer_id'])]



    # Renames the "author_idn" col to "id"
    answr.rename(columns={"author_id": "id"}, inplace=True)

    # Sorts asnwr df in ascending order based on it values in series "id"
    answr = answr.sort_values(by=['id'])

    # Account for duplicatted author ids 
    # (i.e. authors who viewed their work but on different articles/dates)
    answr.drop_duplicates(subset=['id'], inplace=True)

    return answr[["id"]]
