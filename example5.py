

'''
Another example of using ConfigObj module.
In this example, we illustrate how we can use the module ConfigObj and access configuration data using DictNamespace class
For more info about DictNamespace, read https://github.com/Vykstorm/dictnamespace/blob/master/README.md
'''

from configobj import ConfigObj as Config, Section
from configobj.validate import Validator
from utils.dictnamespace import DictNamespace


if __name__ == '__main__':
    # Same configuration file and spec as example 3
    config = Config('config/example3.cnf',
                    configspec='config/example3.spec.cnf',
                    stringify=True)
    result = config.validate(Validator(), preserve_errors=True)
    if result is not True:
        raise Exception('Invalid configuration file: {}'.format(result))

    # Now we create a DictNamespace object
    config = DictNamespace(config, recursive=True)

    # And we can access config entries using the DictNamespace object via attribute indexation or operator []...
    print(config.A, config.B, config.C, config['D'])
    print(config.FOO.E, config.FOO.F, config.FOO['G'])