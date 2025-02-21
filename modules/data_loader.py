import pandas as pd

def load_data(filepath="assets/titanic.csv"):
    """Loads and preprocesses the Titanic dataset."""
    return pd.read_csv(filepath)