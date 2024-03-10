from workbench_utils.warning import filter_warnings


def test_filter_warnings():

    result = filter_warnings()  # pylint: disable=assignment-from-no-return

    assert result is None
