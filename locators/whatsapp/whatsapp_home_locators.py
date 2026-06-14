from appium.webdriver.common.appiumby import AppiumBy


class WhatsAppHomeLocators:

    SEARCH_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "TokenizedSearchBar_SearchButton"
    )

    SEARCH_TEXTBOX = (
        AppiumBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeSearchField'
    )