from workbench_components.workbench_logging.logging_configs import setup_logging
from workbench_process.common import STEP_PROCESS
from workbench_process.process_factory import factory_process


def run_process() -> None:
    """Run the loading and processing of the data."""
    process_logic, process_data, process_settings = factory_process.create_instance(name=STEP_PROCESS)

    process_settings.load_settings_from_file("tests/test_workbench_process/resources/workbench_settings.json")

    process_logic.run(process_data, process_settings)


def main() -> None:

    setup_logging()
    run_process()


if __name__ == "__main__":
    main()
