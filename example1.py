
'''
ConfigObj example:
Shows how to read the configuration present on the file config/example1.cnf
See config/example1.cnf for more info
'''


from configobj import ConfigObj as Config, Section


if __name__ == '__main__':
    config = Config('config/example1.cnf')

    # print(config) shows configuration data on stdout.

    # Access single values via [] operator
    print(config['DEFAULT']['User'] )
    print(config['HOME']['User'] )

    # Use in operator to check if a variable is set within a section or the global scope of the configuration
    print( 'IdentityFile' in config['DEFAULT']  )
    print( 'IdentifyFile' in config['HOME'] )

    # Print subsections in level 1
    print(config.sections)

    # Print variables in the DEFAULT section
    print(config['DEFAULT'].scalars)

    # There is also a set of methods intended to convert configuration string values to a python type.
    print(config['DEFAULT'].as_int('Port'), config['DEFAULT'].as_bool('ForwardX11Trusted'))
    # Automatic conversion type can be done using configuration spec files and validators (this will be shown
    # on other examples)


    # Finally, we can print the initial comment we added on the configuration file.
    print('\n'.join([line for line in config.initial_comment if line != '']))

