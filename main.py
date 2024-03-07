from workbench_components.workbench_logging.logging_configs import setup_logging
from workbench_process.process_factory import factory_process
from workbench_train.train_factory import factory_train
from workbench_utils.common import WorkbenchSteps


def run_all_logic() -> None:
    """Run all the logic"""

    process_logic, process_data, process_settings = factory_process.create_instance(name=WorkbenchSteps.PROCESS)
    process_settings.load_settings_from_file("tests/test_workbench_process/resources/workbench_settings.json")
    process_logic.run(process_data, process_settings)

    train_logic, train_data, train_settings = factory_train.create_instance(name=WorkbenchSteps.TRAIN)
    train_settings.load_settings_from_file("tests/test_workbench_train/resources/workbench_settings.json")
    train_data.from_process_data(process_data)
    train_logic.run(train_data, train_settings)


def main() -> None:

    setup_logging()
    run_all_logic()


if __name__ == "__main__":
    main()
