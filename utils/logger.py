import logging
from pathlib import Path
from datetime import datetime


def setup_logger():
    """
    Creates the application logger.

    Logs are written to:
        logs/run_YYYYMMDD_HHMMSS.log

    Log messages are also displayed in the console.
    """

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    log_file = (
        log_directory
        / f"run_{datetime.now():%Y%m%d_%H%M%S}.log"
    )

    logger = logging.getLogger("ai_job_intelligence")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup_logger()
    # is called more than once.
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info("Logger initialized")
    logger.info("Log file: %s", log_file)

    return logger