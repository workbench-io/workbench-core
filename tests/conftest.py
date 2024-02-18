import pytest

from workbench_core.data_object.data_object import DataObject
from workbench_core.data_object.data_object_factory import DataObjectFactory
from workbench_core.workbench_factory import WorkbenchFactory
from workbench_core.workbench_transformer.workbench_transfomer import WorkbenchTransformer
from workbench_core.workbench_transformer.workbench_transformer_factory import WorkbenchTransformerFactory


class WorkbenchObject:
    pass


class ConcreteDataTransfomer(WorkbenchTransformer):

    def transform(self, data) -> bool:  # pylint: disable=unused-argument
        return True


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


@pytest.fixture
def data_transformer() -> WorkbenchTransformer:
    return ConcreteDataTransfomer


@pytest.fixture
def data_transformer_factory() -> WorkbenchTransformerFactory:
    return WorkbenchTransformerFactory()
