"""
This is the tool that routes to multiple functions to display the appropriate chart
"""

import pandas as pd


def load_df(file_path: str) -> pd.DataFrame:
    # takes a file path, then routes to the appropriate type of file, then loads it as a df
    file_type = file_path.split(".")[-1]
    mapping = {"csv": pd.read_csv,
               "xlsx": pd.read_excel,
               "xls": pd.read_excel,
               "json": pd.read_json}
    return mapping[file_type](file_path)
