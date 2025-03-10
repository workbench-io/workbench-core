from pathlib import Path

from workbench_components.workbench_logging.logging_configs import setup_logging
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger
from workbench_optimize.optimize_factory import factory_optimize
from workbench_process.process_factory import factory_process
from workbench_train.train_factory import factory_train
from workbench_utils.enums import WorkbenchSteps

DIR_SETTINGS = Path(__file__).parent.joinpath("settings")


def run_all_logic(
    filepath_settings_process: Path,
    filepath_settings_train: Path,
    filepath_settings_optimize: Path,
) -> None:
    """
    Run all the logic to:
    - load and process data
    - train, validates and selects the best predictive model among a set of models
    - Use the best model to create a solution that optimizes a given metric given a set of constraints

    Args:
        filepath_settings_process (Path): The file path to the process settings file.
        filepath_settings_train (Path): The file path to the model training settings file.
        filepath_settings_optimize (Path): The file path to the solution optimization settings file.

    Returns:
        None
    """
    process_logic, process_data, process_settings = factory_process.create_instance(name=WorkbenchSteps.PROCESS)
    process_settings.load_settings_from_file(filepath_settings_process)
    process_logic.run(process_data, process_settings)

    train_logic, train_data, train_settings = factory_train.create_instance(name=WorkbenchSteps.TRAIN)
    train_settings.load_settings_from_file(filepath_settings_train)
    train_data.from_process_data(process_data)
    train_logic.run(train_data, train_settings)

    optimize_logic, optimize_data, optimize_settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)
    optimize_settings.load_settings_from_file(filepath_settings_optimize)
    optimize_logic.run(optimize_data, optimize_settings)


def main() -> None:

    setup_logging()

    logger = WorkbenchLogger()
    logger.create_logger()
    logger.log_info(method=main, message="Starting running all logic.")

    run_all_logic(
        filepath_settings_process=Path(DIR_SETTINGS.joinpath("process_settings.json")),
        filepath_settings_train=Path(DIR_SETTINGS.joinpath("train_settings.json")),
        filepath_settings_optimize=Path(DIR_SETTINGS.joinpath("optimize_settings.json")),
    )

    logger.log_info(method=main, message="Finished running all logic.")


if __name__ == "__main__":
    main()
