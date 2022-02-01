import subprocess
from compresser import Compresser
from setUp import SetUp
import argparse
import platform
from os import listdir
from os.path import isfile, join
import os, shutil
import time

my_os = platform.system()

def calculateSimilarity(arraySizes, sizeCat):
    return (sizeCat - min(arraySizes))/max(arraySizes)

def clearFolders():
    if my_os == "Windows":
        arrayString = ["..\\catResults", "..\\sampleFrequences", "..\\targetFrequences", "..\\zippedCat", "..\\zippedSamples", "..\\zippedTarget"]
    elif my_os == "Linux":
        arrayString = ["../catResults", "../sampleFrequences", "../targetFrequences", "../zippedCat", "../zippedSamples", "../zippedTarget"]

    for folder in arrayString:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
clearFolders()

defaultTarget = ""
defaultTypeCompression = ""
if my_os == "Windows":
     defaultTarget = "..\\samples\\WORIMI-_bounce"
     defaultTypeCompression = "lzma"
elif my_os == "Linux":
     defaultTarget = "../samples/WORIMI-_bounce"
     defaultTypeCompression = "lzma"
 
parser = argparse.ArgumentParser(description='I honestly have no clue what this is for.')
parser.add_argument("-ws", type=str, default=1024)
parser.add_argument("-sh", type=str, default=256)
parser.add_argument("-ds", type=str, default=4)
parser.add_argument("-nf", type=str, default=4)
parser.add_argument("-tc", type=str, default=defaultTypeCompression)
parser.add_argument("-t", type=str, default=defaultTarget)
parser.add_argument("-n", type=str, default=0)
parser.add_argument("-tn", type=str, default="whitenoise")
 
args = parser.parse_args()
winSize = str(args.ws)
shift = str(args.sh)
downSampling = str(args.ds)
nFreqs = str(args.nf)
typeCompression = str(args.tc)
targetPath = str(args.t)
valueNoise = str(args.n)
typesOfNoise = str(args.tn)
 
compresser = Compresser(typeCompression, my_os)
setUp = SetUp(my_os, winSize, shift, downSampling, nFreqs)
 
if my_os == "Windows":
    sampleFiles = [f for f in listdir("..\\samples") if isfile(join("..\\samples", f))]
elif my_os == "Linux":
    sampleFiles = [f for f in listdir("../samples") if isfile(join("../samples", f))]

t0 = time.time()
if my_os == "Windows":
     command = 'sox "'+targetPath+".wav"+'" -p synth '+str(typesOfNoise)+' vol '+str(valueNoise)+' | sox -m "'+targetPath+".wav"+'" - ..\\samples\\sampleNoise\\noise.wav'
     subprocess.run(command,  shell=True)
         
     # Preparing the frquency and the compression of the target
     setUp.createGetMaxFreqsFile("..\\targetFrequences\\target.freq", "..\\samples\\sampleNoise\\noise.wav")
     compresser.compressFile("..\\targetFrequences\\target.freq", "..\\zippedTarget\\target")
     
     # Preparing the freq of samples, zipping them and using cat
     
     for file in sampleFiles:
         setUp.createGetMaxFreqsFile("..\\sampleFrequences\\" + file.replace(".wav", ".freq"), "..\\samples\\" + file)
         compresser.compressFile("..\\sampleFrequences\\" + file.replace(".wav", ".freq"), "..\\zippedSamples\\" + file.replace(".wav", ""))
         setUp.cat("..\\sampleFrequences\\" + file.replace(".wav", ".freq"))
         compresser.compressFile("..\\catResults\\" +  file.replace(".wav", ".freq"), "..\\zippedCat\\" +  file.replace(".wav", ""))
         
         
     resultDict = {}
     arraySizes = [0 ,0]
     zippedFiles = [f for f in listdir("..\\zippedSamples") if isfile(join("..\\zippedSamples", f))]
     arraySizes[0] = compresser.getFileSize("..\\zippedTarget\\target." + zippedFiles[0].rpartition(".")[2])
     
     for file in zippedFiles:
         path = "..\\zippedSamples\\" + file
         arraySizes[1] = compresser.getFileSize(path)
         
         path = "..\\zippedCat\\" + file
         cat_size = compresser.getFileSize(path)
         
         resultDict[file.replace("." + zippedFiles[0].rpartition(".")[2] ,"")] = calculateSimilarity(arraySizes, cat_size) 
     
     resultDict = {k: v for k, v in sorted(resultDict.items(), key=lambda item: item[1])}
     i=1
     for key, value in resultDict.items():
         print(str(key) + " - " + str(value))
         if i == 10:
             break
         i+=1
elif my_os == "Linux":
    command = 'sox "'+targetPath+".wav"+'" -p synth '+str(typesOfNoise)+' vol '+str(valueNoise)+' | sox -m "'+targetPath+".wav"+'" - ../samples/sampleNoise/noise.wav'
    subprocess.run(command,  shell=True)
        
    # Preparing the frquency and the compression of the target
    setUp.createGetMaxFreqsFile("../targetFrequences/target.freq", "../samples/sampleNoise/noise.wav")
    compresser.compressFile("../targetFrequences/target.freq", "../zippedTarget/target")
    
    # Preparing the freq of samples, zipping them and using cat
    
    for file in sampleFiles:
        setUp.createGetMaxFreqsFile("../sampleFrequences/" + file.replace(".wav", ".freq"), "../samples/" + file)
        compresser.compressFile("../sampleFrequences/" + file.replace(".wav", ".freq"), "../zippedSamples/" + file.replace(".wav", ""))
        setUp.cat("sampleFrequences/" + file.replace(".wav", ".freq"))
        compresser.compressFile("../catResults/" +  file.replace(".wav", ".freq"), "../zippedCat/" +  file.replace(".wav", ""))
        
        
    resultDict = {}
    arraySizes = [0 ,0]
    zippedFiles = [f for f in listdir("../zippedSamples") if isfile(join("../zippedSamples", f))]
    arraySizes[0] = compresser.getFileSize("../zippedTarget/target." + zippedFiles[0].rpartition(".")[2])
    
    for file in zippedFiles:
        path = "../zippedSamples/" + file
        arraySizes[1] = compresser.getFileSize(path)
        
        path = "../zippedCat/" + file
        cat_size = compresser.getFileSize(path)
        
        resultDict[file.replace("." + zippedFiles[0].rpartition(".")[2] ,"")] = calculateSimilarity(arraySizes, cat_size) 
    
    resultDict = {k: v for k, v in sorted(resultDict.items(), key=lambda item: item[1])}
    i=1
    for key, value in resultDict.items():
        print(str(key) + " - " + str(value))
        if i == 10:
            break
        i+=1
t1 = time.time()
print("Tempo de execução:"+str(t1 - t0))
    