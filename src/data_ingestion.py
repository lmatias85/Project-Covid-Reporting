import gzip as zp
import shutil as sh
import urllib.request as rq
import os 


def ingest_local_file(p_origin_path, p_dest_path, p_zp_file_name, p_unzp_file_name): 
    if os.path.exists(p_origin_path + '/' + p_unzp_file_name):
        os.remove(p_origin_path + '/' + p_unzp_file_name)
    with zp.open(p_origin_path + '/' + p_zp_file_name, 'rb') as f_in:
        with open(p_origin_path + '/' + p_unzp_file_name, 'wb') as f_out:
            sh.copyfileobj(f_in, f_out)   

def ingest_http_file(p_url_file, p_dest_file):
    if os.path.exists(p_dest_file):
        os.remove(p_dest_file)
    rq.urlretrieve(p_url_file, p_dest_file)


