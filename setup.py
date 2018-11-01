
'''
Installation script
'''

from setuptools import setup



if __name__ == '__main__':
    setup(
        name = 'ConfigObj examples',
        version = '1.0.0',
        description = 'Very basic examples of using the python library ConfigObj',
        author = 'Vykstorm',
        author_email = 'victorruizgomezdev@gmail.com',
        python_requires = '>=2.7',
        install_requires = ['configobj'],
        dependency_links = ['https://github.com/DiffSK/configobj/tarball/master#egg=configobj'],
        keywords = ['config', 'configobj', 'validation', 'examples']
    )
