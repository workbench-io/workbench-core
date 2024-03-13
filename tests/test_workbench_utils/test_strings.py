import pytest

from workbench_utils.strings import clean_text


@pytest.mark.parametrize(
    ["input_text", "expected"],
    [
        ("hello_world  ", "Hello World"),
        ("  hello___world__", "Hello World"),
        ("hello-world", "Hello World"),
        ("  hello---world--", "Hello World"),
        ("hEllo_wORLD  ", "Hello World"),
        ("  hEllo___wORLD__", "Hello World"),
        ("hEllo-wORLD", "Hello World"),
        ("  hEllo---wORLD--", "Hello World"),
    ],
)
def test_clean_text(input_text: str, expected: str):

    result = clean_text(input_text)
    assert result == expected
