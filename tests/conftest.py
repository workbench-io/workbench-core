import pytest

from workbench_core.workbench_config.workbench_config import WorkbenchConfig
from workbench_core.workbench_config.workbench_config_factory import WorkbenchConfigFactory
from workbench_core.workbench_data.workbench_data import WorkbenchData
from workbench_core.workbench_data.workbench_data_factory import WorkbenchDataFactory
from workbench_core.workbench_factory import WorkbenchFactory
from workbench_core.workbench_process.workbench_process import WorkbenchProcess
from workbench_core.workbench_process.workbench_process_factory import WorkbenchProcessFactory
from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_core.workbench_transformer.workbench_transformer_factory import WorkbenchTransformerFactory


class WorkbenchObject:
    pass


class ConcreteWorkbenchTransfomer(WorkbenchTransformer):

    def transform(self, data: WorkbenchData) -> bool:  # pylint: disable=unused-argument
        return True


class ConcreteWorkbenchProcess(WorkbenchProcess):
    def run(self, data: WorkbenchData, config: WorkbenchConfig) -> bool:  # pylint: disable=unused-argument
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
    return ConcreteWorkbenchTransfomer


@pytest.fixture
def data_transformer_factory() -> WorkbenchTransformerFactory:
    return WorkbenchTransformerFactory()


@pytest.fixture
def workbench_config() -> WorkbenchConfig:
    return WorkbenchConfig


@pytest.fixture
def workbench_config_factory() -> WorkbenchConfigFactory:
    return WorkbenchConfigFactory()


@pytest.fixture
def workbench_process() -> WorkbenchProcess:
    return ConcreteWorkbenchProcess


@pytest.fixture
def workbench_process_factory() -> WorkbenchProcessFactory:
    return WorkbenchProcessFactory()
