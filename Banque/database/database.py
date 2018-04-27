import sqlite3 as db
import os

# DATABASE_PATH = os.path.join(os.getcwd(), 'Python\\python_codes\\Banque\\bank_db.db')
DATABASE_PATH = 'bank_db.db'

class DataBaseMixins:
    context = None
    
    def get_context(self, *args, **kwargs):
        # Puts context
        if self.context is not None:
            kwargs.update(context=self.context)

        # Puts instance of class
        if 'method' not in kwargs:
            kwargs['method'] = self

        return kwargs


class DataBase(DataBaseMixins):
        def _cursor(self):
            try:
                # Connect to database, 
                _conn = db.connect(DATABASE_PATH)

            except Exception as error:
                print('There was an error. %s' % error.args )
                raise
            
            with _conn:
                self._cursor = _conn.cursor()
                return self._cursor


class DatabaseQueries(DataBase):
    table_name = None

    def select_all(self, *args, **kwargs):
        if 'table_name' in kwargs:
            self.table_name = kwargs.get('table')

        records = super()._cursor().execute('SELECT ? FROM ?', (args, self.table_name,))
        print(records)
        # if 'records' not in kwargs:
        #     kwargs['records'] = records

        # else:
        #     kwargs.update(records=records)

        # return kwargs

print(DatabaseQueries().select_all())
