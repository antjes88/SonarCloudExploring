import pytest
import os


def delete_file_if_exists(file_path):
    """Deletes a file if it exists.

    Args:
        file_path: A string containing the path to the file
    Returns:
        None
    Raises:
        OSError: If the file cannot be deleted
    """
    if os.path.exists(file_path):
        os.remove(file_path)


@pytest.fixture(scope='function')
def reboot_file_path():
    """
    Fixture that yields a file path and deletes the file before and after the test function is run.

    Yields:
        A string containing the file path.
    """
    reboot_file_path = 'tests/output/result.txt'
    delete_file_if_exists(reboot_file_path)

    yield reboot_file_path

    delete_file_if_exists(reboot_file_path)
