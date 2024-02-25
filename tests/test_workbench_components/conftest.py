import logging

import pytest

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_data.workbench_data_factory import WorkbenchDataFactory
from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_components.workbench_logic.workbench_logic_factory import WorkbenchLogicFactory
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_components.workbench_settings.workbench_settings_factory import WorkbenchSettingsFactory
from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_components.workbench_source.workbench_source_factory import WorkbenchSourceFactory
from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_components.workbench_transformer.workbench_transformer_factory import WorkbenchTransformerFactory


class WorkbenchObject:
    pass


class ConcreteWorkbenchTransfomer(WorkbenchTransformer):

    def transform(self, data: WorkbenchData) -> bool:  # pylint: disable=unused-argument
        return True


class ConcreteWorkbenchLogic(WorkbenchLogic):
    def run(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
        return True


class ConcreteWorkbenchSource(WorkbenchSource):
    def load(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
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
def workbench_transformer() -> WorkbenchTransformer:
    return ConcreteWorkbenchTransfomer


@pytest.fixture
def workbench_transformer_factory() -> WorkbenchTransformerFactory:
    return WorkbenchTransformerFactory()


@pytest.fixture
def workbench_config() -> WorkbenchSettings:
    return WorkbenchSettings


@pytest.fixture
def workbench_config_factory() -> WorkbenchSettingsFactory:
    return WorkbenchSettingsFactory()


@pytest.fixture
def workbench_process() -> WorkbenchLogic:
    return ConcreteWorkbenchLogic


@pytest.fixture
def workbench_process_factory() -> WorkbenchLogicFactory:
    return WorkbenchLogicFactory()


@pytest.fixture
def workbench_source() -> WorkbenchSource:
    return ConcreteWorkbenchSource


@pytest.fixture
def workbench_source_factory() -> WorkbenchSourceFactory:
    return WorkbenchSourceFactory()


@pytest.fixture
def log_record_info() -> logging.LogRecord:
    return logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname="/path/to/file.py",
        lineno=10,
        msg="Test message",
        args=None,
        exc_info=None,
    )


@pytest.fixture
def log_record_warning() -> logging.LogRecord:
    return logging.LogRecord(
        name="test_logger",
        level=logging.WARNING,
        pathname="/path/to/file.py",
        lineno=10,
        msg="Test message",
        args=None,
        exc_info=None,
    )
