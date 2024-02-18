import pytest

from workbench_core.workbench_factory import WorkbenchFactory


class WorkbenchObject:
    pass


@pytest.fixture
def workbench_factory() -> WorkbenchFactory:
    return WorkbenchFactory()


@pytest.fixture
def workbench_object() -> object:

    return WorkbenchObject
