import gzip as zp
import shutil as sh
import os 


def ingest_local_file(p_origin_path, p_dest_path, p_zp_file_name, p_unzp_file_name): 
    if os.path.exists(p_origin_path + '/' + p_unzp_file_name):
        os.remove(p_origin_path + '/' + p_unzp_file_name)
    with zp.open(p_origin_path + '/' + p_zp_file_name, 'rb') as f_in:
        with open(p_origin_path + '/' + p_unzp_file_name, 'wb') as f_out:
            sh.copyfileobj(f_in, f_out)   

def ingest_http_file():
    pass