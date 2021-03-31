import os
import configparser

def create_configuration_file():

    config = configparser.ConfigParser()

    config['PopulationFiles'] = {}
    pop = config['PopulationFiles']
    pop['path'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/population'
    pop['zip_file'] = 'population_by_age.tsv.gz'
    pop['unzip_file'] = 'population_by_age.tsv'

    config['HTTPFiles'] = {}
    http = config['HTTPFiles']
    http['cases_deaths_URL'] = 'https://github.com/cloudboxacademy/covid19/raw/main/ecdc_data/cases_deaths.csv'
    http['cases_deaths_file'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/cases-deaths/cases_deaths.csv'
    http['hospital_admissions_URL'] = 'https://github.com/cloudboxacademy/covid19/raw/main/ecdc_data/hospital_admissions.csv'
    http['hospital_admissions_file'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/hospital-admissions/hospital_admissions.csv'
    http['testing_URL'] = 'https://github.com/cloudboxacademy/covid19/raw/main/ecdc_data/testing.csv'
    http['testing_file'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/testing/testing.csv'
    http['country_response_URL'] = 'https://github.com/cloudboxacademy/covid19/raw/main/ecdc_data/country_response.csv'
    http['country_response_file'] = 'C:/Repos/Personal/Project-Covid-Reporting/data-sources/country-response/country_response.csv'

    if os.path.exists('./configuration/configs.ini'):
        os.remove('./configuration/configs.ini')
    with open('./configuration/configs.ini', 'w') as configfile:
        config.write(configfile)