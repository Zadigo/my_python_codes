import sqlite3
from games.bank.database.expressions import SQLStatement


class QuerySet:
    """A wrapper class used to construct database
    queries in more functionnal manner

    Description
    -----------

    `obj` is a sqlite .cursor() method that wraps
    a query into an object that can be converted for
    example into a list
    """

    objs_cache = None

    def __init__(self, objs, **kwargs):
        # Cache objects -;
        # When using the objs once,
        # you cannot access them another time
        # self.objs_cache = list(objs).copy()
        # obj is the .cursor() method
        # object returned by an SQL instruction
        # such as SELECT
        # ..
        # Convert obj as list
        queryset = list(objs)
        self.queryset  = queryset

    def __unicode__(self):
        return f'QuerySet({self.queryset})'

    def __repr__(self):
        return self.__unicode__()

    def __getitem__(self, index):
        values = self.queryset[index]
        return str(values)

    def __len__(self):
        return len(self.queryset)

    def count(self):
        return len(self.queryset)

class Manager:
    """Use this class to perform base operations
    on the database such as inserting values, creating
    or deleting tables
    """
    def __init__(self, **kwargs):
        self.queryset = QuerySet
        self.cursor = None
        self.db = None

    @staticmethod
    def _parse_values(values):
        pass

    def save(self, commit=True):
        """Commit an object to the database

        Description
        -----------

        This method only calls the .commit() method
        on the database object in order to perform the changes.

        If you want to pass the objects, you have to use the
        .run_sql() definition

        Parameters
        ----------

        Use `commit` equals true in order to call the .save() definition
        in order to commit the changes to the database
        """
        try:
            if commit:
                value = self.db.commit()
                # self.database.close()
        except sqlite3.OperationalError:
            raise
        else:
            if value:
                # Return the newly created
                # object from the database
                return value

    def _run_sql(self, sql, **kwargs):
        """Run an SQL statement on the database
        """
        try:
            result = self.cursor.execute(sql)
        except sqlite3.OperationalError:
            raise
        else:
            if result:
                return self.queryset(result)
    
    def _all(self):
        statement = 'SELECT * FROM stars'
        return self._run_sql(statement)

    def get(self, **kwargs):
        statement = """SELECT * FROM stars WHERE name='Kendall'"""
        return self._run_sql(statement)

    def _filter(self, **kwargs):
        # statement = """SELECT * FROM stars WHERE name LIKE 'K%'"""
        # statement = """SELECT * FROM stars WHERE name LIKE 'Kendall'"""
        statement = """SELECT * FROM stars WHERE name LIKE '%all%'"""

        filters = ['contains']
        
        parameters = []

        # We have to transform the kwargs
        # into a list of tuples containing
        # the filter and then the value
        # for that given filter
        # e.g. [(column__filter, value)]
        for key, value in kwargs.items():
            items = key, value                
            parameters.append(items)

        # column = f = None

        # for parameter in parameters[0]:
        #     # We can then split the column
        #     # from the filter (column__filter)
        #     try:
        #         column, f = parameter.split('__', 1)
        #     except BaseException:
        #         pass
        # print(column, f)
        
        # return self._run_sql(statement)

    def create(self, **kwargs):
        sql = 'INSERT INTO stars(name, surname) VALUES ("Marlène", "Hoes")'
        self._run_sql(sql)
        self.save()

    def bulk_create(self, **kwargs):
        """Save multiple values in the database at once
        """
        try:
            sql = 'INSERT INTO stars(name, surname) VALUES (?, ?)'
            _save = self.cursor.executemany(sql, [('Kelly', 'Vedovelli'), ('Bella', 'Hadid')])
        except sqlite3.OperationalError:
            raise
        else:
            if _save:
                self.save()
                return _save

    def bulk_delete(self, **kwargs):
        pass

    # def update(self, **kwargs):
    #     pass

    def get_or_create(self, **kwargs):
        # First we query the database to
        # see if there's an existing value
        statement = """SELECT * FROM stars WHERE name='Kendall' AND surname='Jenner'"""
        values = self._run_sql(statement)
        # If we have more than two values,
        # then we already some things
        if values.count().__gt__(2):
            raise TypeError()
        # Otherwise, we can create
        # that unique value
        create_statement = """INSERT INTO stars VALUES('Kendall2', 'Jenner')"""
        self._run_sql(create_statement)
        self.db.commit()

    # def delete(self, **kwargs):
    #     pass

    def last_created(self):
        statement = """SELECT * FROM stars ORDER BY name DESC LIMIT 1"""
        return self._run_sql(statement)
