from pages.base_page import BasePage
from locators.whatsapp.whatsapp_chat_locators import WhatsAppChatLocators


class WhatsAppChatPage(BasePage):

    def type_message(self, message):
        self.send_keys(
            WhatsAppChatLocators.MESSAGE_BOX,
            message
        )

    def click_send(self):
        self.click(WhatsAppChatLocators.SEND_BUTTON)

    def send_message(self, message):
        self.type_message(message)
        self.click_send()