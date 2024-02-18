import pytest

from workbench_core.workbench_config.workbench_config import WorkbenchConfig
from workbench_core.workbench_config.workbench_config_factory import WorkbenchConfigFactory
from workbench_core.workbench_data.workbench_data import WorkbenchData
from workbench_core.workbench_data.workbench_data_factory import WorkbenchDataFactory
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
def workbench_data() -> WorkbenchData:
    return WorkbenchData


@pytest.fixture
def workbench_data_factory() -> WorkbenchDataFactory:
    return WorkbenchDataFactory()


@pytest.fixture
def data_transformer() -> WorkbenchTransformer:
    return ConcreteDataTransfomer


@pytest.fixture
def data_transformer_factory() -> WorkbenchTransformerFactory:
    return WorkbenchTransformerFactory()


@pytest.fixture
def workbench_config() -> WorkbenchConfig:
    return ConcreteDataTransfomer


@pytest.fixture
def workbench_config_factory() -> WorkbenchConfigFactory:
    return WorkbenchConfigFactory()
