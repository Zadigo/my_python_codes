import os
# from importlib import import_module

class DiscoverApps:
    def __init__(self):
        """
        This class lists all the applications present
        in the program
        """
        # dirs = os.walk('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque')
        dirs = os.walk('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque')
        w = list(dirs)[0]
        # applications_path = w[0]
        applications = w[1]
        # available_apps = ['banque_applications', 'banque_database', 'banque_errors', 'banque_settings', 'banque_utils']
        if not applications:
            print('There was an error %s')
            raise TypeError

        else:
            pass
            # if 'banque_settings' not in available_apps:
            #     print('There was an error')
            #     raise TypeError
            # if 'banque_database' not in available_apps:
            #     print('There was an error')
            #     raise TypeError

        # self.applications_path = applications_path
        # self.available_apps = available_apps
        self._applications = []
        for application in applications:
            application_list = application, os.path.join('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque', application)
            self._applications.append(application_list)

class BanqueApps(DiscoverApps):
    @property
    def get_available_applications(self):
        return self._applications
