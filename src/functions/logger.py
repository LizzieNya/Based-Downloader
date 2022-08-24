# import Python's standard libraries
import logging
import sys
from datetime import datetime
from typing import Any, NoReturn

# import local files
if (__name__ != "__main__"):
    from .crucial import __version__
    from .functional import check_and_make_dir, get_saved_folder_path, print_danger
else:
    from crucial import __version__
    from functional import check_and_make_dir, get_saved_folder_path, print_danger

def get_exception_logger() -> logging.Logger:
    """Get the exception logger."""
    name = f"Cultured Downloader V{__version__}"
    logger = logging.getLogger(name)

    logger.setLevel(logging.ERROR)
    separator = "-" * 100
    formatter = logging.Formatter(f"{separator}\n%(asctime)s [{name}] [%(levelname)s]: %(message)s\n{separator}")

    currentDate = datetime.now().strftime("%Y-%m-%d")
    loggingFilePath = get_saved_folder_path().joinpath("logs")
    check_and_make_dir(loggingFilePath)
    fileHandler = logging.FileHandler(
        filename=loggingFilePath.joinpath( f"cultured-downloader_v{__version__}_{currentDate}.log"), mode="a"
    )
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

def exception_handler(excType: Any, excValue: Any, execTraceback: Any) -> NoReturn:
    """Use a custom logger to log exceptions to a file."""
    logger.exception(f"Uncaught {excType.__name__}", exc_info=(excType, excValue, execTraceback))
    print_danger(f"\nUncaught {excType.__name__}")
    print_danger(f"Please provide the developer with the error log generated at\n{logger.handlers[0].baseFilename}")

    input("Please press ENTER to exit...")
    return sys.exit(1)

logger = get_exception_logger()