import pandas as pd

class PandasDataframeComparison:
    """
    Class that compare 2 dataframes and returns a report.

    Args:
        df_left: first dataframe to execute the comparison
        df_right: second dataframe to execute the comparison
    """
    def __init__(self,df_left: pd.DataFrame, df_right:pd.DataFrame):
        self.df_left = df_left
        self.df_right = df_right

    def df_are_equals(self):
        """
        Method that check if 2 dataframes are equal
        """
        return self.df_left.equals(self.df_right)