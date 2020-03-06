# PRODUCTION

def generateOrmClass(columns, aliased):
    """Generates a mapping class table for SQLAlchemy ORM
    
    Keyword arguments:
    columns: tuple -- formatted as ('col_name', 'data-type') e.g. ('id', 'Integer')
    aliased: string -- how sqlalchemy has been imported as e.g. sql, db
        
    """
    repr_list = []
    alias = aliased + '.'
    for col in columns:    
        name, dtype = col
        print('\t' + name + ' = ' + alias + 'Column' + '(' + alias + dtype + ')')
        repr1 = name + ': self.' + name
        repr_list.append(repr1)
    rep1 = '\t' + 'def __repr__(self):' + '\n' + '\t\t' + 'return "<('
    rep2 = ' , '.join(repr_list)
    rep3 = ')>"'
    print(rep1 + rep2 + rep3)
    
## Some test data
columns = ('id', 'Integer'), ('name', 'String'), ('fullname', 'String'), ('nickname', 'String')
alias = 'sql.'

## Usage
# generateOrmClass(columns, 'db.')