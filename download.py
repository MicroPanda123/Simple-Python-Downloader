from tqdm import tqdm
import requests
import argparse
import time

def download_file(url, chunk_size = 1024):
    pootis = 1

    if chunk_size == 1: unit_name = "B"
    elif chunk_size == 1024: unit_name = "KB"
    elif chunk_size == 1048576: unit_name = "MB"
    else: unit_name = "parts"

    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    try:
        total_size = int(r.headers['content-length'])
    except:
        pootis = 2
        
    with open(local_filename, 'wb') as f:
        if pootis == 1:
            for chunk in tqdm(r.iter_content(chunk_size=chunk_size), total=int(total_size/chunk_size), unit = str(unit_name)):
                if chunk:
                    #time.sleep(1)
                    f.write(chunk)
                    f.flush()
        elif pootis == 2:
            print("Turning on Error mode")
            for chunk in tqdm(r.iter_content(chunk_size=chunk_size), unit = 'KB'):
                if chunk:
                    #time.sleep(1)
                    f.write(chunk)
                    f.flush()
    return local_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--chunk_size")
    args = parser.parse_args()
    download_file(args.url, int(args.chunk_size))

