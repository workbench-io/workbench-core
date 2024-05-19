# workbench-core

This repository contains the code for the `workbench_core` package.

This is a package that is used for:
- **Data processing**: it loads data of concrete compressive strength and processes it prior to training. The code for this is in the `workbench_process` module.
- **Model training and selection**: it trains a model to predict concrete compressive strength and selects and exports the best model. The code for this is in the `workbench_train` module.
- **Solution optimization**: it creates a mixture of concrete that maximizes compressive strength given a set of constraints. The code for this is in the `workbench_optimize` module.
- **API**: it provides an API to interact with the package. The API can be used to predict the compressive strength of concrete mixtures and also to optimize the mixture of concrete to maximize compressive strength. The code for this is in the `workbench_api` module.
---

## Structure

The package is structured into the following modules:
- `workbench_components`
- `workbench_process`
- `workbench_train`
- `workbench_optimize`
- `workbench_utils`
- `workbench_api`
- `workbench_db`

---

### `workbench_components`

`workbench_components` contains core components of the `workbench_core` package that are used throughout other modules.

It contains concept classes such as:
- `WorkbenchData`: base class for data objects. These objects are used to store data and metadata and are used by `WorbenchLogic` objects.
- `WorkbenchSettings`: base class for settings objects. These objects are used to store settings used by `WorbenchLogic` objects.
- `WorkbenchLogic`:  base class for logic objects. These objects are used to process data in the provided `WorkbenchData` object according to the settings in the provided `WorkbenchSettings` object.
- `WorkbenchSource`: base class used to connect to data sources and retrieve data.
- `WorkbenchTransformer`: base class used to transform data. Each `WorkbenchTransformer` object is used to apply a specific transformation to the provided `WorkbenchData` object.
- `WorkbenchLogger`: Logger class for the workbench project. Used for logging messages and errors.
- `WorkbenchRepository`: base repository class used to connect to data storage and perform CRUD operations.
- `WorkbenchFactory`: Factory class used to create instances of core components.

---

### `workbench_process`

`workbench_process` contains the code for loading and processing data prior to training.

Among some of the processing steps are:
- **Data loading**: Loading the data from its source
- **Data cleaning**
- **Data splitting**: Splitting the features and target variables

---

### `workbench_train`

`workbench_train` contains the code for training, validating, selecting, and exporting models that predict selected target features (e.g. compressive strength).

The training process includes:
- **Data splitting**: Splitting the data into training and test sets
- **Create preprocessor**: Creating a preprocessor to transform the data and performa feature engineering
- **Train models**: Training multiple models and performing hyperparameter tuning
- **Model selection**: Selecting the best model(s)
- **Export model**: Exporting the best model(s) for later use

---

### `workbench_optimize`

`workbench_optimize` contains the code for optimizing concrete mixtures given a set of constraints. It uses the models obtained from the `workbench_train` module to predict the strength of the concrete mixtures.

Currently, the optimization process is done using a genetic algorithm.

---

### `workbench_api`

`workbench_api` contains the code for the API that interacts with the `workbench_core` package. The API can be used to predict the compressive strength of concrete mixtures and also to optimize the mixture of concrete to maximize compressive strength.

---

### `workbench_db`


---

### `workbench_utils`





## Installation


## Development setup

After cloning the repository, you can easily install the development environment and tools
([black](https://github.com/psf/black), [pylint](https://www.pylint.org), [mypy](http://mypy-lang.org), [pytest](https://pytest.org), [tox](https://tox.readthedocs.io))
with:

```
git clone https://github.com/workbench-io/workbench-core.git
cd workbench_core
pip install -e .[dev]
```
