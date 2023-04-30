import pandas as pd


class PandasDataframeComparison:
    """
    Class that compare 2 dataframes and returns a report.

    Args:
        df_left: first dataframe to execute the comparison
        df_right: second dataframe to execute the comparison
    """
    def __init__(self, df_left: pd.DataFrame, df_right: pd.DataFrame):
        self.df_left = df_left
        self.df_right = df_right

    def df_are_equals(self):
        """
        Method that check if 2 dataframes are equal
        """
        return self.df_left.equals(self.df_right)

    def write_report(self, report_file_path):
        """
        Method that creates a report file with the result of the analysis

        Args:
            report_file_path: path to file where report has to be written
        """
        with open(report_file_path, 'w+') as f:
            if self.df_are_equals():
                f.write("Dataframes are equal")
            else:
                f.write("Dataframes are not equal")

    def get_missing_columns(self):
        """
        Method that returns as list the columns from left df that are not present on right df and vice-versa.

        Returns:
            - list of columns from left df that are not present on right df
            - list of columns from right df that are not present on left df
        """
        left_missing_columns = set(self.df_left.columns) - set(self.df_right.columns)
        right_missing_columns = set(self.df_right.columns) - set(self.df_left.columns)

        return list(left_missing_columns), list(right_missing_columns)
