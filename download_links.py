from pytube import YouTube
import argparse
from glob import glob
import os

def read_links_file(links_file):
    links = []
    file = open(links_file,'r')
    while True:
        # Get next line from file
        line = file.readline()
    
        if not line:
            break
        links.append(line.strip())
  
    file.close()
    
    return links

def download_links(links, save_dir):

    downloaded_files = glob(save_dir + '/*')
    
    # for file in downloaded_files:

    for link in links:
        try:
            youtubeObject   = YouTube(link)
            file_name       = youtubeObject.title
            replaced_fname  = file_name.replace('|','').replace('\'','').replace('*','').replace('.','').replace('%','')\
                        .replace('#','').replace('!','').replace('\"','')
            download = True
            for downloaded_title in downloaded_files:
                if replaced_fname in downloaded_title:
                    download = False
                    print(f'-Already downloaded {downloaded_title}')
            
            if download:
                youtubeObject   = youtubeObject.streams.get_highest_resolution()
                try:
                    print(f'Downloading: {replaced_fname} ...')
                    youtubeObject.download(save_dir)
                except Exception as e:
                    print(f'ERROR downloading: {replaced_fname}: {link}: {e}')
                print(f'\t Download Success')
        except:
            pass
    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--links_file', type=str, default='links.txt',  help='name of the text file with links to download')
    parser.add_argument('--output_dir', type=str, default='vids',       help='name of the folder to save the file')
    parser.add_argument('--retries',    type=int, default=3,            help='number of times to retry downloading the files')

    opts =  parser.parse_args()
    os.makedirs(opts.output_dir,exist_ok=True)
    links = read_links_file(opts.links_file)
    for i in range(opts.retries):
        download_links(links, opts.output_dir)