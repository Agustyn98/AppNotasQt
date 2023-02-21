import dropbox
from backend import NotesDB
import os
import hashlib
from time import sleep


access_token = os.environ['TOKEN']
dir_path = NotesDB.get_dir_path()
db_name = "notes.db"
local_db_path = os.path.join(dir_path, db_name)
dpx_db_path = f"/{db_name}"

dbx = dropbox.Dropbox(access_token)


def upload_db(db_path=local_db_path):
    with open(db_path, 'rb') as f:
        dbx.files_upload(f.read(), dpx_db_path, mode=dropbox.files.WriteMode.overwrite)


DROPBOX_HASH_CHUNK_SIZE = 4*1024*1024
def compute_hash(filename):
    #file_size = os.stat(filename).st_size
    with open(filename, 'rb') as f:
        block_hashes = b''
        while True:
            chunk = f.read(DROPBOX_HASH_CHUNK_SIZE)
            if not chunk:
                break
            block_hashes += hashlib.sha256(chunk).digest()
        return hashlib.sha256(block_hashes).hexdigest()


def get_hash_cloud(dropbox_path=dpx_db_path):
    metadata = dbx.files_get_metadata(dropbox_path)
    #last_modified = metadata.client_modified
    #sv_last_modified = metadata.server_modified
    hash = metadata.content_hash
    return hash

def compare_hases(local_db, dpx_db):
    """Returns True if the hashes are the same"""
    local_hash = compute_hash(local_db)
    cloud_hash = get_hash_cloud(dpx_db)
    print(f'Local hash: {local_hash}')
    print(f'Cloud hash: {cloud_hash}')
    if local_hash == cloud_hash:
        return True
    else:
        return False


def upload_db(local_db_path, dpx_db_path=dpx_db_path):
    if compare_hases(local_db_path, dpx_db_path):
        print('Not uploading because the file has not changed')
        return -1

    with open(local_db_path, 'rb') as f:
        dbx.files_upload(f.read(), dpx_db_path, mode=dropbox.files.WriteMode.overwrite)

    print(f'File uploaded to {dpx_db_path}')

def download_db(local_db_path, dpx_db_path=dpx_db_path):
    if compare_hases(local_db_path, dpx_db_path):
        print('Not downloading because the file has not changed')
        return -1

    dbx.files_download_to_file(local_db_path, dpx_db_path)
    print(f'File downloaded to {local_db_path}')

if __name__ == '__main__':
    print('Downloading db...')
    download_db(local_db_path, dpx_db_path)
    sleep(2)
    print('Uploading db...')
    upload_db(local_db_path, dpx_db_path)

