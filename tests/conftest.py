import pytest

from workbench_core.data_object.data_object import DataObject
from workbench_core.data_object.data_object_factory import DataObjectFactory
from workbench_core.data_transformer.data_transfomer import DataTransformer
from workbench_core.data_transformer.data_transformer_factory import DataTransformerFactory
from workbench_core.workbench_factory import WorkbenchFactory


class WorkbenchObject:
    pass


class ConcreteDataTransfomer(DataTransformer):

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
def data_transformer() -> DataTransformer:
    return ConcreteDataTransfomer


@pytest.fixture
def data_transformer_factory() -> DataTransformerFactory:
    return DataTransformerFactory()
