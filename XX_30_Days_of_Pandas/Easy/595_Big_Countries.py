import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
   
    # Query returns a df whose value meets the given conditions
    answr = world.query("population >= 25000000 or area >= 3000000")

    # Return df with only the relevant columns
    return answr[["name", "population", "area"]]  
   
