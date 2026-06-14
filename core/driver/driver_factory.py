"""WHY DRIVER FACTORY?

This centralizes:

Appium session management
driver initialization
future environments/devices

Professional frameworks NEVER initialize drivers inside tests.
"""

from appium import webdriver
from appium.options.ios import XCUITestOptions

from config.capabilities.ios_capabilities import (
    IOS_CAPABILITIES
)


class DriverFactory:

    @staticmethod
    def get_driver():

        options = XCUITestOptions()

        options.load_capabilities(
            IOS_CAPABILITIES
        )

        driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )

        driver.implicitly_wait(10)

        return driver