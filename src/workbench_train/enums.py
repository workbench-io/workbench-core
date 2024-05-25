from enum import StrEnum


class Transformers(StrEnum):
    BOOLEAN_IMPUTE_MISSING = "boolean_impute_missing"
    NUMERIC_IMPUTE_MISSING_MEDIAN = "numeric_impute_missing_median"
    NUMERIC_IMPUTE_MISSING_MEAN = "numeric_impute_missing_mean"
    NUMERIC_ADD_MISSING_INDICATOR = "numeric_add_missing_indicator"
    NUMERIC_YEOJOHNSON = "numeric_yeojohnson"
    NUMERIC_ZSCORE_SCALING = "numeric_zscore_scaling"
    NUMERIC_MINMAX_SCALING = "numeric_minmax_scaling"
    NUMERIC_WINSORIZER = "numeric_winsorizer"
    NUMERIC_OUTLIER_TRIMMER = "numeric_outlier_trimmer"
    NUMERIC_REMOVE_CORRELATED = "numeric_remove_correlated"
    CATEGORICAL_IMPUTE_MISSING = "categorical_impute_missing"
    CATEGORICAL_RARE_LABEL_ENCODER = "categorical_rare_label_encoder"
    CATEGORICAL_ONE_HOT_ENCODER = "categorical_one_hot_encoder"
    DATETIME_CREATE_FEATURES = "datetime_create_features"
    ALL_DROP_DUPLICATE = "all_drop_duplicate"
    ALL_DROP_CONSTANT = "all_drop_constant"
    ALL_DROP_MISSING = "all_drop_missing"
    ALL_REMOVE_CORRELATED = "all_remove_correlated"
    OBJECT_DROP_COLUMNS = "object_drop_columns"


class MetricsRegression(StrEnum):
    MSE = "mse"
    RMSE = "rmse"
    MAE = "mae"
    MAPE = "mape"
    MAX_ERROR = "max_error"
    R_SQUARED = "r_squared"


class ModelsRegression(StrEnum):
    DUMMY = "dummy"
    PLS = "pls"
    LASSO = "lasso"
    ELASTICNET = "elasticnet"
    SVR = "svr"
    RANDOM_FOREST = "random_forest"
    GBM = "gbm"
    NEURAL_NETWORK = "neural_network"
