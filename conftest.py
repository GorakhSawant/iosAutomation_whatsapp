import pytest

from core.driver.driver_factory import (
    DriverFactory
)


@pytest.fixture(scope="function")
def driver():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()