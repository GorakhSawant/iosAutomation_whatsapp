from pages.whatsapp.whatsapp_home_page import WhatsAppHomePage
from pages.whatsapp.whatsapp_chat_page import WhatsAppChatPage


def test_send_message(driver):

    home_page = WhatsAppHomePage(driver)
    chat_page = WhatsAppChatPage(driver)

    home_page.click_search()

    home_page.search_contact("Aryan")

    home_page.open_contact("Aryan")

    chat_page.send_message(
        "Hello Aryan from iOS Appium Automation 🚀"
    )