import gzip
import shutil
import os
import subprocess
import zipfile
import zlib
import bz2
import lzma

class Compresser:
    def __init__(self, typeCompression, OS):
        self.typeCompression = typeCompression
        self.OS = OS
    
    def getFileSize(self, path):
        return os.path.getsize(path)

    def compressFile(self, pathFile, saveFolder):
        if self.typeCompression == "WinRar" or self.typeCompression == "gzip":
            self.gZipCompression(pathFile, saveFolder)
        elif self.typeCompression == "7Zip":
            self.zip7(pathFile, saveFolder)
        elif self.typeCompression == "zlib":
            self.zlib(pathFile, saveFolder)
        elif self.typeCompression == "bzip2":
            self.bzip2(pathFile, saveFolder)
        elif self.typeCompression == "lzma":
            self.lzma(pathFile, saveFolder)
      
#-------------------------------------GZIP--------------------------------------
    def gZipCompression(self, pathFile, saveFolder):
        with open(pathFile, 'rb') as f_in:
            with gzip.open(saveFolder + ".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)  
#-------------------------------7ZIP-------------------------------------------
    def zip7(self, pathFile, saveFolder):
        if self.OS == "Windows":
            subprocess.call(['7z', 'a', saveFolder + '.7z', pathFile])
        elif self.OS == "Linux":
            subprocess.call(['7z', 'e', saveFolder + '.zip', pathFile])
 #---------------------- zlib ---------------------------
    def zlib(self, pathFile, saveFolder):
          
         with open(pathFile, "rb") as fin:
            with open(saveFolder + ".zlib", mode="wb") as fout:
                data = fin.read()
                compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
                fout.write(compressed_data)
                fout.close()
 #---------------------- bzip2 ---------------------------
    def bzip2(self, pathFile, saveFolder):
         with open(pathFile, "rb") as fin:
            with open(saveFolder + ".bzip2", mode="wb") as fout:
                data = fin.read()
                compressed_data = bz2.compress(data)
                fout.write(compressed_data)
                fout.close()
 #---------------------- lzma  ---------------------------
    def lzma(self, pathFile, saveFolder):
         with open(pathFile, "rb") as fin:
            with open(saveFolder+".xz", mode="wb") as fout:
                data = fin.read()
                compressed_data = lzma.compress(data)
                fout.write(compressed_data)
                fout.close()
