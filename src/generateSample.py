import subprocess
import os
import argparse
import platform

class Samples:
   def __init__(self, timeSample):
      self.timeSample = timeSample
      
   def generateSamples(self):
       my_os = platform.system()
       if my_os == "Windows":
           entries = os.listdir('..\\music\\')
       elif my_os == "Linux":
            entries = os.listdir('../music/')
     
       for entry in entries:
          if my_os == "Windows":
              command = 'sox "'"..\\music\\"+str(entry)+'"  "'+"..\\samples\\"+str(entry)+'" trim 1.0 '+str(self.timeSample)
          elif my_os == "Linux":
              command = 'sox "'"../music/"+str(entry)+'"  "'+"../samples/"+str(entry)+'" trim 1.0 '+str(self.timeSample)
          subprocess.run(command,  shell=True)

parser = argparse.ArgumentParser(description='I honestly have no clue what this is for.')
parser.add_argument("-ts", type=str, default=10)
 
args = parser.parse_args()
timeSample = str(args.ts)
samples = Samples(timeSample)
samples.generateSamples()