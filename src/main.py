import configparser as confrd
import urllib as url

import configuration as conf
import data_ingestion as ingest


# Config File
print('Creating Configuration File...')
conf.create_configuration_file()
print('\t"configs.ini" File created. [OK]')

# Load Config File
config = confrd.ConfigParser()
config.read('C:/Repos/Personal/Project-Covid-Reporting/configuration/configs.ini')

# Ingest Local Files
print('Ingesting local files...')
pop_path = config['PopulationFiles']['path']
pop_zip_file = config['PopulationFiles']['zip_file']
pop_unzip_file = config['PopulationFiles']['unzip_file']
ingest.ingest_local_file(pop_path,pop_path,pop_zip_file,pop_unzip_file)
print('\tLocal Files ingested. [OK]')

# Ingest URL Files
print('Ingesting HTTP files')
url_cases_deaths = config['HTTPFiles']['cases_deaths_URL']
file_cases_deaths = config['HTTPFiles']['cases_deaths_file']
ingest.ingest_http_file(url_cases_deaths,file_cases_deaths)

url_cases_deaths = config['HTTPFiles']['hospital_admissions_URL']
file_cases_deaths = config['HTTPFiles']['hospital_admissions_file']
ingest.ingest_http_file(url_cases_deaths,file_cases_deaths)

url_cases_deaths = config['HTTPFiles']['testing_URL']
file_cases_deaths = config['HTTPFiles']['testing_file']
ingest.ingest_http_file(url_cases_deaths,file_cases_deaths)

url_cases_deaths = config['HTTPFiles']['country_response_URL']
file_cases_deaths = config['HTTPFiles']['country_response_file']
ingest.ingest_http_file(url_cases_deaths,file_cases_deaths)
print('\t HTTP files ingestd. [OK]')