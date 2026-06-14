from pages.base_page import BasePage
from locators.whatsapp.whatsapp_home_locators import WhatsAppHomeLocators


class WhatsAppHomePage(BasePage):

    def click_search(self):
        self.click(WhatsAppHomeLocators.SEARCH_BUTTON)

    def search_contact(self, contact_name):
        self.send_keys(
            WhatsAppHomeLocators.SEARCH_TEXTBOX,
            contact_name
        )

    def open_contact(self, contact_name):

        contact_locator = (
            "accessibility id",
            contact_name
        )

        self.driver.find_element(*contact_locator).click()