import string
import random
import time


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



class projectHelper:

    def __init__(self, app):
        self.app = app


    def check_on_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.get(self.app.base_url + "/manage_proj_create_page.php")


    def create_new(self):
        wd = self.app.wd
        name = random_string(20)
        self.change_field_value("name", name)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        return name


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def get_count(self):
        wd = self.app.wd
        self.open_list_page()
        return len(wd.find_elements_by_css_selector("table:nth-child(6) tr:not(.row-category) a"))


    def open_list_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get(self.app.base_url + "/manage_proj_page.php")


    def del_random_project(self):
        wd = self.app.wd
        self.open_list_page()
        del_project = random.choice(wd.find_elements_by_css_selector("table:nth-child(6) tr:not(.row-category) a"))
        removed_project = del_project.text
        del_project.click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        return removed_project


    def get_list(self):
        wd = self.app.wd
        list = []
        for element in wd.find_elements_by_css_selector("table:nth-child(6) tr:not(.row-category) a"):
            list.append(element.text)
        return list

