class Expressions:
    """Base class to manage all SQL type statements
    such as transforming python type writting to SQL

    Parameters
    ----------

        - for_save: Whether the statement is to be used for
          a save or update SQL statement
    """
    # If not for create,
    # then for write
    for_create = False
    joiner = ', '

    wild_cards = ['%', '_']

    def resolve(self, **values):
        """This defininition resolves the parameters
        of and SQL statement

        Description
        -----------

        When calling function such as ._filter(a=b, c=d), we
        need to resolve these parameters such as a=b AND c=d if
        it's in a SELECT case.

        Parameters
        ----------

        `values` is a set of keyword values to resolve
        """
        parameters = []

        new_columns = []
        new_values = []

        # For create and insert, we need
        # parameters such as (1, a, b)
        if not self.for_create:
            for key, value in values.items():
                new_columns.append(key)
                new_values.append(value)
            return [str(tuple(new_columns)), str(tuple(new_values))]
        
        else:
            # For none create statements,
            # we need a=b AND b=c
            for key, value in values.items():
                parameters.append(str(key) + '=' + str(value))
            # Return the parameters as an array
            # because we might need to include
            # some sort of operator
            return ' AND '.join(parameters)

    def where(self, **values):
        """A defintion that resolves the where clause
        """
        return ' WHERE ' + self.resolve(**values)

    @classmethod
    def wilcards(cls):
        """A definition used to resolve wildcards.

        Result
        ------

            Returns a WildCard class -- which can be used
            as so:

                WildCard().icontains(value)

                SQLStatement().wildcards().icontains(value)
        """
        @staticmethod
        def icontains(value):
            return '%{}%'.format(value)

        @staticmethod
        def startswith(value):
            return '%{}'.format(value)

        @staticmethod
        def endswith(value):
            return '{}%'.format(value)
        
        class_dict = {
            'icontains': icontains,
            'startswith': startswith,
            'endswith': endswith
        }

        klass = type('WildCards', (cls,), class_dict)

        klass.__repr__ = "google"
        klass.__unicode__ = klass.__repr__()

        return klass()

class SQLStatement(Expressions):
    operators = {
        'and': 'AND',
        'or': 'OR',
    }
    templates = {
        # template = """{}({}) VALUES('{}')"""
        'insert': """INSERT INTO {}{} VALUES{}""",
        # 'create': """CREATE TABLE {} {}""",
        'select': """SELECT {} FROM {}"""
    }

    def create_statement(self, table=None, template=None, for_create=False, **parameters):
        # Indicate if the statement is to
        # create or retrieve data
        self.for_create = for_create
        # Get the corresponding template to use
        statement_template = self.templates[template]
        # Resolve the parameters and transform
        # them to a readable SQL statement
        resolved_parameters = self.resolve(**parameters)
        # [(columns), (values)]
        if for_create:
            return statement_template.format(table, resolved_parameters[0], resolved_parameters[1])
        else:
            return statement_template.format(resolved_parameters[0], table)

# s = SQLStatement().create_statement('stars', 'select', for_create=False, name='Kendall', surname='Jenner')
# print(s)
# print(SQLStatement().wilcards().value)

# def collate(**params):
#     s = []

#     def connector(param):
#         s.append(param)

#     if len(params).__eq__(1):
#         for name, value in params.items():
#             connector(name + "=" + value)
#         return s
#     else:
#         for name, value in params.items():
#             connector(name + "='" + value + '\'')
#             final = ' AND '.join(s)
#     return final

# # SELECT * FROM x WHERE a=a
# params = {
#     'a': 'a'
# }
# print(collate(**params))

# params = {
#     'a': 'a',
#     'w': 'c'
# }
# print(collate(**params))

# print(repr(SQLStatement().wilcards))