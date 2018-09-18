import sqlite3 as db
import datetime
import os

class DatabaseMigrator:
    def __init__(self, connection, *kwargs):
        if 'commit' in kwargs:
            if kwargs['commit']:

                if isinstance(connection, db):
                    print('We can migrate the database')
                    self.connection = connection

                else:
                    print('%s is not an instance if sqlite3')
                    raise TypeError

    def _migrate(self):
        try:
            sql = ''
            self.connection.execute(sql)
        
        except db.Error as error :
            print('There was an error %s' % error.__str__())
            raise
        
        else:
            return self

    def _create_migration_file(self):
        current_date = datetime.datetime.now().timestamp()
        filename = 'migration_' + str(current_date) + '.py'
        migration_directory = os.path.join('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations', filename)

        migration_path = os.path.exists('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations')

        if not migration_path:
            print('We create the migration directory')
            os.mkdir('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations')
            with open('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations/__init__.py', 'w', encoding='utf-8') as new_init:
                new_init.writelines('Nothing')

        else:
            print('We create the migration file')

            with open(filename, 'w', encoding='utf-8') as migration_file:
                migration_file.writelines('')
    