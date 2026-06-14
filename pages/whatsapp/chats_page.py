from pages.base_page import BasePage

from locators.whatsapp.chats_locators import (
    ChatsLocators
)


class ChatsPage(BasePage):

    def click_search_button(self):

        self.click_element(
            ChatsLocators.SEARCH_BUTTON
        )