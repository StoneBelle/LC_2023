import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    # Check if any vals in "conditions" contains "DIAB1"
    # r indicates a raw str, and allows the use of regex
    # \b checks for word boundaries (i.e. space, period, tab)
    return patients[patients["conditions"].str.contains(r"\bDIAB1")]
