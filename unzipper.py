#Elias Jaffe 2019

import zipfile
import os
from glob import glob

def main():
    zipped = glob("*.zip")
    print("Files to unzip:", zipped)
    unzipped = [fname.replace(".zip","") for fname in zipped]

    for zipped_file, extraction_file in zip(zipped, unzipped):
        with zipfile.ZipFile(zipped_file, 'r') as zip_ref:

            print("Unzipping:", zipped_file)

            try:
                zip_ref.extractall(extraction_file)

            except:
                os.mkdir(extraction_file)
                zip_ref.extractall(extraction_file)
                
            print("Unzipped.")

    print("Complete!")
    return 0

if __name__ == "__main__":
    main()
