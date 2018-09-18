import os
from importlib import import_module

class DiscoverApps:
    def __init__(self):
        """
        This class lists all the applications present
        in the program.
        """
        dirs = os.walk('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque')
        w = list(dirs)[0]
        applications_path = w[0]
        applications = w[1]
        available_apps = ['banque_applications', 'banque_database', 'banque_settings']
        if not applications:
            print('There was an error %s')
            raise TypeError

        else:
            if 'banque_settings' not in available_apps:
                print('There was an error')
                raise TypeError
            if 'banque_database' not in available_apps:
                print('There was an error')
                raise TypeError

        self.applications_path = applications_path
        self.available_apps = available_apps

    @property
    def get_available_applications(self):
        return self.available_apps

    def _apps_init(self):
        """
        This function builds the full path
        of each path in order to do somthing
        with them.
        """
        application_full_path = []
        for application in self.available_apps:
            application_full_path.append(os.path.join(self.applications_path, application))
