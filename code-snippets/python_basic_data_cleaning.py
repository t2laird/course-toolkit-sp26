# Basic Data Cleaning Tool: Handle missing values + remove duplicates + reset index
import pandas as pd

def basic_data_cleaning(df: pd.DataFrame, fillna_value: any = 0) -> pd.DataFrame:
    """
    Perform basic cleaning on a pandas DataFrame
    :param df: The DataFrame to be cleaned
    :param fillna_value: Default value to fill missing values (0 by default)
    :return: Cleaned DataFrame
    """
    # 1. Remove completely duplicate rows
    df_clean = df.drop_duplicates()
    # 2. Fill in missing values with the specified value
    df_clean = df_clean.fillna(fillna_value)
    # 3. Reset index (delete original index, generate new continuous index)
    df_clean = df_clean.reset_index(drop=True)
    # 4. Print summary of cleaning results
    print(f"Cleaning completed: Original rows {len(df)} → Cleaned rows {len(df_clean)}")
    return df_clean

# Test example (can be retained or deleted, does not affect core functionality)
if __name__ == "__main__":
    test_df = pd.DataFrame({"A": [1, 2, 2, None], "B": [4, None, 5, 5]})
    cleaned_df = basic_data_cleaning(test_df)
    print(cleaned_df)