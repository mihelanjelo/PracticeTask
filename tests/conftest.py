from utils.logger import Logger


def pytest_runtest_setup(item):
    Logger.get_instance().info("%s стартует.... " % item.name)

