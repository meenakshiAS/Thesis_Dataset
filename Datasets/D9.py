def select_option(self, option):
    """
    Performs selection of provided item from Web List

    @params option - string item name
    """
    items_list = self.get_options()

    for item in items_list:
        if item.get_attribute("value") == option:
            item.click()
            break
