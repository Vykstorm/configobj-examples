

'''
ConfigObj example
This little example illustrates how subsections can be declared in a configuration file and how to access them
See config/example2.cnf for more info.
'''


from configobj import ConfigObj as Config

if __name__ == '__main__':
    config = Config('config/example2.cnf')
    # print(config)


    # Print a list of our subsections inside the section called 'SITES'
    print('Sites: ', config['SITES'].sections)

    # For each subsection in 'SITES' we print their variable entries.
    for sitename in config['SITES'].sections:
        site = config['SITES'][sitename]
        print('Site: ', sitename)
        print('Request-type: ', site['request-type'])
        print('Endpoint: ', site['endpoint'])
        print()