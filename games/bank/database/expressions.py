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

    def resolve(self, **values):
        parameters = []
        new_values = []

        # For create and insert, we need
        # parameters such as (1, a, b)
        if self.for_create:
            for key, value in values.items():
                new_values.append(value)
            return str(tuple(new_values))
        
        else:
            # For none create statements,
            # we need a=b OPERATOR b=c
            for key, value in values.items():
                parameters.append(str(key) + '=' + str(value))
            # new_parameters = self.joiner.join(parameters)
            # return new_parameters
            # Return the parameters as an array
            # because we might need to include
            # some sort of operator
            return ' AND '.join(parameters)

class SQLStatement(Expressions):
    operators = {
        'and': 'AND',
        'or': 'OR',
        'wild_cards': {
            '1': '%',
            '2': '_'
        }
    }
    templates = {
        'insert': """INSERT INTO %(table)s VALUES(%(parameters)s)"""
    }

    def create_statement(self, table=None, template=None, **parameters):
        template = """{}({}) VALUES('{}')"""
        # Get the corresponding template to use
        # statement_template = self.templates[template]
        # # Resolve the parameters and transform
        # # them to a readable SQL statement
        # resolved_parameters = self.resolve(**parameters)
        # statement_template % {
        #     'table': table,
        #     'parameters': resolved_parameters
        # }
        # print(statement_template)
        return template.format('CREATE stars', 'science')
