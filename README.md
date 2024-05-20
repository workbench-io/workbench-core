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

You can clone the repository with:

```bash
git clone https://github.com/workbench-io/workbench-core.git
```

Then, navigate to the repository with:
```bash
cd workbench_core
```

This package is being developed with python 3.11.7. You can use `pyenv` to manage your python versions and install python 3.11.7 with:
```bash
pyenv install 3.11.7
```

You can set the local python version to 3.11.7 with:
```bash
pyenv local 3.11.7

```
The package is setup with poetry. You can install the package with:
```bash
poetry install
```

---

## Development setup

To setup the development environment, you first have to follow the installation steps above. Once you have the package installed, you can create a virtual environment with poetry.

You can activate the virtual environment with:
```bash
poetry shell
```

You can install the dependencies with:
```bash
poetry install
```

Once all the dependencies are installed, you can run the tests with:
```bash
poetry run pytest
```

You can also run the tests with coverage with:
```bash
poetry run pytest --cov=workbench_core
```

---

## Usage

### Running the processing, training and optimization logic

If you would like to run the logic to load and process the data, train the models, and optimize the concrete mixtures, you can use the `main.py` script in the root directory.

You can run the script with:
```bash
poetry run python main.py
```

This script will run the entire pipeline, from loading the data to optimizing the concrete mixtures. It may take more than 5 minutes to run depending on your machine and the settings you have set for each step. The settings for each step are defined in the JSON files in `./settings`

```
settings
├── process_settings.json  # Settings for data loading and  processing
├── train_settings.json    # Settings for model training and selection
└── optimize_settings.json # Settings for the optimization process
```

### Running the API

#### Running the API locally

You can run the API locally with the following command:

```bash
poetry run uvicorn src.workbench_api.main:app --reload
```

#### Generating predictions

You can find below an example of how to generate predictions using the API. You can use `curl` or any other tool to make HTTP requests.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/compressive_strength' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "water": 8.33,
  "coarse_aggregate": 42.23,
  "slag": 0,
  "cement": 12.09,
  "superplasticizer": 0,
  "fine_aggregate": 37.35,
  "fly_ash": 0,
  "age": 28
}'
```

The response will be a JSON object with the predicted compressive strength.
```
{
  "id": 2,
  "value": 26.52264422267783,
  "feature": "compressive_strength",
  "inputs": {
    "cement": 12.09,
    "slag": 0,
    "fly_ash": 0,
    "water": 8.33,
    "superplasticizer": 0,
    "coarse_aggregate": 42.23,
    "fine_aggregate": 37.35,
    "age": 28
  },
  "version": null
}
```


#### Optimizing concrete mixtures

You can find below an example of how to generate optimized concrete mixtures using the API. You can use `curl` or any other tool to make HTTP requests.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/optimize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "num_genes": 7,
  "num_generations": 10,
  "sol_per_pop": 10,
  "num_parents_mating": 5,
  "keep_parents": 0,
  "init_range_low": 0,
  "init_range_high": 100,
  "gene_space": {
    "low": 0,
    "high": 100
  },
  "parent_selection_type": "sss",
  "crossover_type": "single_point",
  "crossover_probability": 0.2,
  "mutation_type": "random",
  "mutation_probability": 0.2,
  "random_seed": 1
}'
```

The response will be a JSON object with the optimized concrete mixture.
```
{
  "id": 1,
  "value": 61.68289803952541,
  "solution": {
    "superplasticizer": 54.66200250647524,
    "cement": 63.65402903614014,
    "slag": 92.09472156251303,
    "fine_aggregate": 68.84132523859434,
    "coarse_aggregate": 14.038693859523377,
    "fly_ash": 19.22500168221477,
    "water": 7.838689985494796,
    "age": 28
  },
  "inputs": {
    "num_genes": 7,
    "num_generations": 10,
    "sol_per_pop": 10,
    "num_parents_mating": 5,
    "keep_parents": 0,
    "init_range_low": 0,
    "init_range_high": 100,
    "gene_space": {
      "low": 0,
      "high": 100
    },
    "parent_selection_type": "sss",
    "crossover_type": "single_point",
    "crossover_probability": 0.2,
    "mutation_type": "random",
    "mutation_probability": 0.2,
    "random_seed": 1
  }
}
```

---
