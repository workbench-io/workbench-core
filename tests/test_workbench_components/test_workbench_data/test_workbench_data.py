import pytest

from workbench_components.workbench_data.workbench_data import WorkbenchData, WorkbenchDataException


class TestWorkbenchData:

    def test___init__(self):
        workbench_data = WorkbenchData()
        assert workbench_data is not None

    def test_get_data_returns_data_when_present(self):
        workbench_data = WorkbenchData()
        workbench_data.data1 = [1, 2, 3]

        result = workbench_data.get_data("data1")

        assert result is not None
        assert result == [1, 2, 3]

    def test_get_data_raises_exception_when_data_is_absent(self):
        workbench_data = WorkbenchData()

        name = "does_not_exist"
        with pytest.raises(WorkbenchDataException):
            workbench_data.get_data(name)
