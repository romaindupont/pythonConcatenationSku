import os
import os.path

fileDir = os.getcwd()
familySku = []
designsSku = []
finishSku = []
sizeSku = []
configSku = []
certifSku = []

def searchFile():

  with open(fileDir+"\\ListfamilySku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      familySku.append(newL)
  with open(fileDir+"\\ListDesignsSku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      designsSku.append(newL)
  with open(fileDir+"\\ListconfigurationSku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      configSku.append(newL)
  with open(fileDir+"\\ListFinishSku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      finishSku.append(newL)
  with open(fileDir+"\\ListSizeSku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      sizeSku.append(newL)
  with open(fileDir+"\\ListCertificationSku.csv") as file_in:
    for line in file_in:
      newL = line.strip('\n')
      certifSku.append(newL)
  newFileCreation()

def newFileCreation():
 registerLine = open(fileDir+"\\modifyFiles.txt", "wt")
 for line in familySku:
  for designLine in designsSku:
   for configLine in configSku:
    for finishLine in finishSku:
     for sizeLine in sizeSku:
      for certifLine in certifSku:
       newline = line + designLine + '-' + configLine + '-' + finishLine + '-' + sizeLine + '-' + certifLine + '\n'
       print(newline)
       registerLine.write(newline)


searchFile()