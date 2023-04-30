import filecmp
import pandas as pd
import pytest
from compare import PandasDataframeComparison


@pytest.mark.parametrize(
    "df_left, df_right, expected_result",
    [
        (
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                True
        ),
        (
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                pd.DataFrame.from_dict({'col_1': [4, 5, 6], 'col_2': ['d', 'e', 'f']}),
                False
        ),
    ]
)
def test_df_are_equals(df_left, df_right, expected_result):
    """
    GIVEN a couple of dataframes that can or cannot be equals
    WHEN they are processed by PandasDataframeComparison.df_are_equals()
    THEN the value results should evaluate if they are or not equals (as given on parameter expected_result value)
    """
    comparison = PandasDataframeComparison(df_left, df_right)

    assert comparison.df_are_equals() == expected_result


@pytest.mark.parametrize(
    "df_left, df_right, report_file_path_to_compare",
    [
        (
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                'tests/data/report_equal.txt'
        ),
        (
                pd.DataFrame.from_dict({'col_1': [1, 2, 3], 'col_2': ['a', 'b', 'c']}),
                pd.DataFrame.from_dict({'col_1': [4, 5, 6], 'col_2': ['d', 'e', 'f']}),
                'tests/data/report_not_equal.txt'
        ),
    ]
)
def test_write_report(df_left, df_right, report_file_path_to_compare, reboot_file_path):
    """
    GIVEN a couple of dataframes that can or cannot be equals
    WHEN they are processed by PandasDataframeComparison.write_report()
    THEN the report files should be created and the evaluation should be the expected
    """
    comparison = PandasDataframeComparison(df_left, df_right)
    comparison.write_report(reboot_file_path)

    assert filecmp.cmp(report_file_path_to_compare, reboot_file_path)


def test_fails():
    assert False