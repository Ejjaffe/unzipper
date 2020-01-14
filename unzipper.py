#Elias Jaffe 2019

import zipfile          # the zipfile utility
import os               # talks to your operating system. For making files
from glob import glob   # will let me grab all zip files in a folder

def main():
    '''
    Unzips all files in the directory. Not recursive.
    '''
    # get the names of every zip file in the directory
    zipped = glob("*.zip")
    print("Files to unzip:", zipped)
    
    # new directory names for the unzipped files
    unzipped = [fname.replace(".zip","") for fname in zipped]
    
    # zip() here just returns pairs of objects, one from each list
    for zipped_file, extraction_file in zip(zipped, unzipped):
        
        # read each zipfile
        with zipfile.ZipFile(zipped_file, 'r') as zip_ref:

            print("Unzipping:", zipped_file)

            try:
                # extract all to the new file
                zip_ref.extractall(extraction_file)

            except:
                # if there's a problem, make the file and try again
                os.mkdir(extraction_file)
                zip_ref.extractall(extraction_file)
                
            print("Unzipped.")

    print("Complete!")
    return 0

if __name__ == "__main__":
    main()
