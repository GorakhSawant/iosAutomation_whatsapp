from appium.webdriver.common.appiumby import AppiumBy


class WhatsAppChatLocators:

    MESSAGE_BOX = (
        AppiumBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeTextView'
    )

    SEND_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Send"
    )