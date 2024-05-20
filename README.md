# workbench-core

This repository contains the code for the `workbench_core` package.

This is a package that is used for:
- **Data processing**: it loads a dataset containing data of concrete mixtures and their corresponding compressive strengths. The data is processed prior to training. The code for this is in the `workbench_process` module.
- **Model training and selection**: it trains several models to predict the compressive strength of a concrete mixture. The best performing model is automatically selected and exported. The code for this is in the `workbench_train` module.
- **Solution optimization**: it creates a mixture of concrete that maximizes compressive strength given a set of constraints (e.g. minimum and maximum amounts of certain components). The code for this is in the `workbench_optimize` module.
- **API**: it provides an API to interact with the package. The API has one endpoint to predict the compressive strength of concrete mixtures given its composition, and also one endpoint to generate a concrete mixture with the maximum strength given a set of constraints. The code for this is in the `workbench_api` module.


Throughout this project, I have used design patterns like factory, abstract factory, template and repository. A wide range of regressors are tested to predict the target feature, from relatively simple algorithms like PLS, LASSO and ElasticNet, to more complex algorithms like GBM and neural networks.

All of the modules in this package are extensively tested, including the API endpoints. You can find all tests in the `tests` directory.

In this project, I use GitHub Actions to create a CI/CD pipeline that publishes the packages in a private PyPI repository on Azure DevOps. You can find the files with the GitHub Actions workflows in `.github/workflows/`.

---

## Structure

The package is structured into the following modules:
- `workbench_components`: common components used throughout the package
- `workbench_process`: data loading and processing
- `workbench_train`: model training and selection
- `workbench_optimize`: solution optimization
- `workbench_api`: API for predicting compressive strength and optimizing concrete mixtures
- `workbench_utils`: utility functions and classes
- `workbench_db`: utilities for connecting to a database

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

### `workbench_process`

`workbench_process` contains the code for loading and processing data prior to training.

Among some of the processing steps are:
- **Data loading**: Loading the data from its source
- **Data cleaning**
- **Data splitting**: Splitting the features and target variables

### `workbench_train`

`workbench_train` contains the code for training, validating, selecting, and exporting models that predict selected target features (e.g. compressive strength).

The training process includes:
- **Data splitting**: Splitting the data into training and test sets
- **Create preprocessor**: Creating a preprocessor to transform the data and performa feature engineering
- **Train models**: Training multiple models and performing hyperparameter tuning
- **Model selection**: Selecting the best model(s)
- **Export model**: Exporting the best model(s) for later use

### `workbench_optimize`

`workbench_optimize` contains the code for optimizing concrete mixtures given a set of constraints. It uses the models obtained from the `workbench_train` module to predict the strength of the concrete mixtures.

Currently, the optimization process is done using a genetic algorithm.

### `workbench_api`

`workbench_api` contains the code for the API that interacts with the `workbench_core` package.

The API has one endpoint to predict the compressive strength of a concrete mixture given its composition (`/predict`), and also one endpoint to generate a concrete mixture with the maximum strength given a set of constraints  (`/optimize`).

### `workbench_db`

`workbench_db` contains utilities for connecting to a database. It also contains classes of models for the database tables and repostory classes for CRUD operations.

### `workbench_utils`

`workbench_utils` contains utility functions and classes used throughout the package.

---

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
