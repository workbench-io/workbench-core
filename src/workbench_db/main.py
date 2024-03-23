import logging

from workbench_components.workbench_configs import workbench_configs
from workbench_db.db import check_sql_model, create_db_and_tables, get_database_engine
from workbench_db.models import Optimization, Prediction

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Creating database engine")
    engine = get_database_engine(workbench_configs.database_url)

    logger.info("Creating database and tables")

    if check_sql_model(Optimization) and check_sql_model(Prediction):
        create_db_and_tables(engine, workbench_configs.database_url)
        logger.info("Database and tables created")


if __name__ == "__main__":
    main()
