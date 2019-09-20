import sqlite3
from games.bank.database.query import QuerySet

class Manager:
    """Use this class to perform base operations
    on the database such as inserting values, creating
    or deleting tables
    """
    def __init__(self, **kwargs):
        # The wrapper for the values
        # returned by the database
        self.queryset = QuerySet
        # Updated on database
        # call with sqlite cursor
        # and db methods
        self.cursor = None
        self.db = None

        # When calling Manager alone, the cursor
        # and db are not set, hence, impossible
        # to call definitions such as .execute()
        if not self.cursor and not self.db:
            try:
                # Try to get a database --
                # if provided by the user
                self.db = kwargs['using']
                # db needs to return something in order for
                # us to get the cursor
                if not callable(self.db) or not isinstance(self.db, type):
                    msg = 'Did you forget to pass an instance of the database?'
                    raise TypeError(msg)
                self.cursor = self.db.cursor()
            except TypeError:
                msg = "You cannot call the instance of Manager directly."\
                        "You need to set the values for cursor and db by passing the instance"\
                            " of the database and its cursor."
                print(msg)
                raise

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

    def update(self, **kwargs):
        sql = """UPDATE stars SET name='a', surname='b' WHERE id=1"""
        return self._run_sql(sql)

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
print(Manager().update(name='Kendall', surname='Jenner'))