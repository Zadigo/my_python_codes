import sqlite3
import psycopg2
import datetime
import os

class Database:
    def __init__(self):
        # Get the user preference

        # Connect to database

        pass

    def save(self, commit=True):
        pass

class Migrator(Database):
    def _init(self):
        pass

    def migrate_model(self):
        pass

    def _create_file(self):
        pass


# class BaseMigrator:
#     def __init__(self, connection, **kwargs):
#         self.connection = connection
#         if 'commit' in kwargs:
#             to_commit = kwargs['commit']
#             if to_commit:
#                 self._init()

#             else:
#                 print('-'*10 + '>', 'We do not have to commit the migration in the database')
    
#     @property
#     def return_instance(self):
#         return self

#     def _init(self):
#         print('-'*10 + '>', 'We have to commit the migration in the database')
#         sqls = (
#             ('bank__auth', 'CREATE TABLE bank__auth (person_id int, email varchar(255))', '- Creating table bank__auth'),
#             ('bank__main', 'CREATE TABLE bank__main (account_id int)', '- Creating table bank__main'),
#             ('bank__backend', 'CREATE TABLE bank__backend (id int)', '- Creating table bank__backend'),
#             ('bank__logs', 'CREATE TABLE bank__logs (log_id int)', '- Creating table bank__logs'),
#             ('bank__apps', 'CREATE TABLE bank__logs (app_id int, app_key varchar(70), app_name varchar(50), app_path varchar(255))', '- Creating table bank__apps')
#         )
#         for sql in sqls:
#             # print('We execute the sql %s' % sql[0])
#             try:
#                 print(sql[2])
#                 self.connection.execute(sql[1])
#             except db.Error:
#                 print('-'*10 + '>', 'Was not able to create table: %s' % sql[0])

#     def _create_migration_directory(self):
#         # migration_directory = os.path.join('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations', filename)
#         # migration_path = os.path.exists('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations')
#         migration_directory = os.path.exists('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque\\migrations')

#         if not migration_directory:
#             print('-'*10 + '>', 'We create the migration directory')
#             # os.mkdir('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations')
#             # with open('/Users/talentview/Documents/DataAnalysis2/python_django_codes/Games/Banque/migrations/__init__.py', 'w', encoding='utf-8') as new_init:
#                 # new_init.writelines('Nothing')
#             os.mkdir('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque\\migrations')
#             with open('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque\\migrations\\__init__.py', 'w', encoding='utf-8') as new_init_file:
#                 new_init_file.writelines('Nothing')

#     def _create_migration_file(self):
#         # 1. We check that the migration folder exits
#         # 2. If it does exist, we create a base migration file —; else, we create the migration folder then the file
#         self._create_migration_directory()
#         current_date = datetime.datetime.now().timestamp()
#         filename = 'migration_' + str(current_date) + '.py'
#         migration_file_path = os.path.join('D:\\Programs\\Python\\repositories\\python_codes\\Games\\Banque\\migrations\\%s', filename)
#         print('-'*10 + '>', 'We create the migration file')
#         with open(migration_file_path.format(filename), 'w', encoding='utf-8') as migration_file:
#             migration_file.writelines('')
    

# class Migrator(BaseMigrator):
#     """
#     This class is used to run overall migration tasks
#     into the database.
#     """
#     def _migrate(self):
#         # 1. We check that the migration folder exits
#         # 2. If it does exist, we create a base migration file —; else, we create the migration folder then the file
#         # 3. We migrate all the application settings in the database
#         try:
#             sql = ''
#             self.connection.execute(sql)
        
#         except db.Error as error :
#             print('There was an error %s' % error.__str__())
#             raise
        
#         else:
#             return self
