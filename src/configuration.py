import os
import configparser

def create_configuration_file():

    config = configparser.ConfigParser()

    config['PopulationFiles'] = {}
    sources = config['PopulationFiles']
    sources['path'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/population'
    sources['zip_file'] = 'population_by_age.tsv.gz'
    sources['unzip_file'] = 'population_by_age.tsv'


    if os.path.exists('./configuration/configs.ini'):
        os.remove('./configuration/configs.ini')
    with open('./configuration/configs.ini', 'w') as configfile:
        config.write(configfile)