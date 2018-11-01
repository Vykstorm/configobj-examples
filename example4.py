
'''
Example of ConfigObj
This script demonstrates the use of default values on configuration entries using config spec files
'''

from configobj import ConfigObj as Config
from configobj.validate import Validator

if __name__ == '__main__':
    config = Config('config/example4.cnf',
                    configspec = 'config/example4.spec.cnf',
                    stringify = True)

    validator = Validator()

    result = config.validate(validator, preserve_errors = True)

    if not result is True:
        print('Configuration variables {} doesnt match the specs'.format(
            ' and '.join(['"{}"'.format(key) for key, value in result.items() if value is not True])))
        exit()


    # Print config variables and its default values
    # Default values can be accessed via .default_values attributte
    for varname in config.scalars:
        print('{} = {}, default value = {} (is of type {})'.format(
            varname,
            config[varname],
            config.default_values[varname],
            type(config[varname]).__name__))


