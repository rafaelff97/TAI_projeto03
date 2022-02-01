import subprocess

class SetUp:
  def __init__(self, OS, winSize, shift, downSampling, nFreqs):
    self.OS = OS
    self.winSize = winSize
    self.shift = shift
    self.downSampling = downSampling
    self.nFreqs = nFreqs

  def createGetMaxFreqsFile(self, savePath, targetPath):
      if self.OS == "Windows":
          command =  '..\\GetMaxFreqs\\bin\\GetMaxFreqs -ws ' + self.winSize + ' -sh ' + self.shift +  '-ds ' + self.downSampling + '-nf ' + self.nFreqs +  ' -w "' + savePath + '" "' + targetPath +'"'
          subprocess.run(command, shell=True)
      elif self.OS == "Linux":
          command =  '../GetMaxFreqs/bin/GetMaxFreqs -ws ' + self.winSize + ' -sh ' + self.shift +  '-ds ' + self.downSampling + '-nf ' + self.nFreqs +  ' -w "' + savePath + '" "' + targetPath +'"'
          subprocess.run(command, shell=True)

  def cat(self, pathFile2):
      if self.OS == "Windows":
          command = 'type ' + ' ..\\targetFrequences\\target.freq' + ' "' + pathFile2 + '" > ' + '"..\\catResults\\' + pathFile2.rpartition("\\")[2]+'"'
          subprocess.run(command,  shell=True)
      elif self.OS == "Linux":
          command = 'cat ' + '../targetFrequences/target.freq' + ' "' + pathFile2 + '" > ' + '"../catResults/' + pathFile2.rpartition("/")[2]+'"'
          subprocess.run(command,  shell=True)
            
