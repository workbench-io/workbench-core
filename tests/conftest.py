import pytest

from workbench_core.data_objects.data_object import DataObject
from workbench_core.data_objects.data_object_factory import DataObjectFactory
from workbench_core.workbench_factory import WorkbenchFactory


class WorkbenchObject:
    pass


@pytest.fixture
def workbench_factory() -> WorkbenchFactory:
    return WorkbenchFactory()


@pytest.fixture
def workbench_object() -> WorkbenchObject:
    return WorkbenchObject


@pytest.fixture
def data_object() -> DataObject:
    return DataObject


@pytest.fixture
def data_object_factory() -> DataObjectFactory:
    return DataObjectFactory()
