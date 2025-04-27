import pytest
import logging, inspect

# This base class will be inherited by all the Test class, hence the methods defined within the base class will be available to all the inherited classes
@pytest.mark.usefixtures('SetUp')
class BaseClass:
    
    # Used to log the necessary actions into the following file: './Logs/logFile.log'
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('./Logs/logFile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
