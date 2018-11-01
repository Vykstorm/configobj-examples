

'''
ConfigObj example.
This example illustrates how to use spec configuration files and validators using the library ConfigObj
Read the docs for more info: https://configobj.readthedocs.io/en/latest/validate.html
'''


from configobj import ConfigObj as Config, Section
from configobj.validate import Validator




if __name__ == '__main__':
    config = Config('config/example3.cnf',
                    configspec = 'config/example3.spec.cnf',
                    stringify = True)
    # print(config)

    # We need to create a validator to check configuration values using the spec file.
    validator = Validator()

    # Now we validate the config
    success = config.validate(validator)

    # success maybe false or true whatever config file matches the spec
    if not success:
        print('Configuration entries doesnt match the specs')

    # You can specify the argument preserve_errors when validating.
    result = config.validate(validator, preserve_errors=True)

    # if validation succeed, result is True. Otherwise its a dictionary that indicates what configuration entries doesnt
    # match the spec
    if result is not True:
        print('Configuration spec errors: ', result)

    # After calling validate() method, config variables will change its types with the indicated in the config spec
    # (only for entries that passed the test)
    # This behaviour can be changed indicating the parameter stringify to False at ConfigObj instantiation.
    for varname in config.scalars:
        varvalue = config[varname]
        print('{} = {} (is of type {})'.format(varname, varvalue, type(varvalue).__name__))



    # Validation will check also configuration entries on subsections

    if result is not True and 'FOO' in result:
        print()
        print('Foo subsection spec errors: ', result['FOO'])

    print()
    print('[FOO]')
    for varname in config['FOO'].scalars:
        varvalue = config['FOO'][varname]
        print('{} = {} (is of type {})'.format(varname, varvalue, type(varvalue).__name__))

