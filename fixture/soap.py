from suds.client import Client
from suds import WebFault

class soapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client(app.configuration["soap"]["baseUrl"])


    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        return self.client.service.mc_projects_get_user_accessible(username, password)

