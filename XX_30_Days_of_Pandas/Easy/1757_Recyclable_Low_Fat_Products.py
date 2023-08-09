import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

  # Return df of the product ids that are both low fat & recyclable
  # Checks multiple cols for specific vals
  answr = products.query('low_fats.str.contains("Y") and recyclable.str.contains("Y")', engine='python')

  # Return df with only the product_id columns
  return answr[["product_id"]]  
   
