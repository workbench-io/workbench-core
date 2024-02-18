"""Test the WorkbenchFactory class."""

import pytest

from tests.conftest import WorkbenchObject
from workbench_core.workbench_factory import WorkbenchFactory, WorkbenchFactoryError


class TestWorkbenchFactory:
    """Test the WorkbenchFactory class."""

    def test_register(self, workbench_factory: WorkbenchFactory, workbench_object: WorkbenchObject):

        workbench_factory = WorkbenchFactory()
        workbench_factory.register(name="name", item=workbench_object)

        assert workbench_factory._items["name"] == workbench_object  # pylint: disable=protected-access

    def test_create(self, workbench_factory: WorkbenchFactory, workbench_object: WorkbenchObject):

        workbench_factory = WorkbenchFactory()
        workbench_factory.register(name="name", item=workbench_object)
        result = workbench_factory.create(name="name")

        assert result == workbench_object

    def test_create_instance(self, workbench_factory: WorkbenchFactory, workbench_object: WorkbenchObject):

        workbench_factory = WorkbenchFactory()
        workbench_factory.register(name="name", item=workbench_object)
        result = workbench_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_object.__qualname__
        assert isinstance(result, WorkbenchObject)

    def test_create_instance_not_registered(self, workbench_factory: WorkbenchFactory):

        object_name = "name"
        workbench_factory = WorkbenchFactory()

        with pytest.raises(WorkbenchFactoryError, match=f"Item {object_name} not found in factory."):
            workbench_factory.create_instance(name=object_name)

    @pytest.mark.parametrize(
        ["name", "expected"],
        [
            ("name", True),
            ("other_name", True),
            ("non_existing_name", False),
        ],
        ids=["single", "multiple", "non_existing"],
    )
    def test_contains(
        self,
        workbench_factory: WorkbenchFactory,
        workbench_object: WorkbenchObject,
        name: str,
        expected: bool,
    ):

        workbench_factory = WorkbenchFactory()
        workbench_factory.register(name="name", item=workbench_object)
        workbench_factory.register(name="other_name", item=workbench_object)

        result = workbench_factory.contains(name=name)
        assert result is expected

    @pytest.mark.parametrize(
        ["names", "items"],
        [
            ([], {}),
            (["name"], {"name": "item"}),
            (["name", "other_name"], {"name": "item", "other_name": "other_item"}),
        ],
        ids=["empty", "single", "multiple"],
    )
    def test_list_items(self, workbench_factory: WorkbenchFactory, names: list, items: dict):

        for name in names:
            workbench_factory.register(name=name, item=items[name])

        result = workbench_factory.list_items()
        assert result == names
