import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # Given 2 dataframes: customers & orders
    # customers contains customers' IDs & names 
    # orders contains customers' IDs of purchasing customers 
    # Determine which customers never purchased 

    # Retrieve ids of customers who ordered and store in list
    purchasers = orders["customerId"].tolist()

    # Removes the rows of customers who purchased, from the OG df
    # (i.e. leaves the customers who did NOT purchase in the df)
    customers = customers[customers.id.isin(purchasers) == False]

    # Renames the "name" col to "Customers"
    customers.rename(columns={"name": "Customers"}, inplace=True)

    # Returns only the "Customers" col, but still remains as a df 
    return customers[["Customers"]]
    

