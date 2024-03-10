from pathlib import Path

from workbench_components.workbench_logging.logging_configs import setup_logging
from workbench_optimize.optimize_factory import factory_optimize
from workbench_process.process_factory import factory_process
from workbench_train.train_factory import factory_train
from workbench_utils.common import WorkbenchSteps


def run_all_logic(
    filepath_settings_process: Path,
    filepath_settings_train: Path,
    filepath_settings_optimize: Path,
) -> None:
    """Run all the logic"""

    process_logic, process_data, process_settings = factory_process.create_instance(name=WorkbenchSteps.PROCESS)
    process_settings.load_settings_from_file(filepath_settings_process)
    process_logic.run(process_data, process_settings)

    train_logic, train_data, train_settings = factory_train.create_instance(name=WorkbenchSteps.TRAIN)
    train_settings.load_settings_from_file(filepath_settings_train)
    train_data.from_process_data(process_data)
    train_logic.run(train_data, train_settings)

    optimize_logic, optimize_data, optimize_settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)
    optimize_settings.load_settings_from_file(filepath_settings_optimize)
    optimize_data.from_process_data(process_data)
    optimize_logic.run(train_data, train_settings)


def main() -> None:

    setup_logging()
    run_all_logic(
        filepath_settings_process=Path("./output/process_settings.json"),
        filepath_settings_train=Path("./output/train_settings.json"),
        filepath_settings_optimize=Path("./output/optimize_settings.json"),
    )


if __name__ == "__main__":
    main()
