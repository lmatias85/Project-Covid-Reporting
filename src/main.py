import configparser as confrd

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