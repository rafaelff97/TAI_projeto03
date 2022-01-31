# Lab Work 3

O objectivo do programa é realizar a identificação da música através de pequenas amostras, utilizando a Distância de Compressão Normalizada (NCD). A NCD é calculada com base em compressores, e indicará o grau de semelhança entre uma música e a amostra, sendo que quanto menor o valor, maior o grau de semelhança.
Devido a existir problemas do programa fornecido com o ubuntu não foi possivel testar para linux, contudo foi implementado.

# Elementos do grupo

Nome: Rafael da Fonseca

Email: rafaelfonseca97@ua.pt

Nº: 95319

<br>

Nome: Gonçalo Junqueira

Email: g.junqueira@ua.pt

Nº: 95314

<br>

## Lab Work 3

### Como correr:
Para executar o programa basta executar os comandos abaixo.

### Requirements:
Ter instalado os seguintes módulos:
- 7zip
- sox

### Parâmetros:
##### accuracy ou project:
- <b>-tc</b>: Método de compressão a ser utilizado no cálculo da DCN. Métodos de compressão disponíveis: gzip, bzip2, lzma, 7Zip e zlib.<br>
- <b>-t</b>: Caminho para o ficheiro target.
- <b>-n</b>: Volume do ruído que será adicionado à amostra a ser identificada (0 <= nível de ruído <= 1)
- <b>-tn</b>: Tipo de ruído que será adicionado à amostra a ser identificada. Tipos de ruído disponíveis: whitenoise, pinknoise or brownnoise.

#### generateSamples:
- <b>-ts</b>: O comprimento, em segundos, das amostras que serão geradas.

#### Notas:
- Os ficheiros de áudio devem ser .wav, estéreo, amostrados a 44100 Hz, 16 bits.

#### Iniciar o generateSample:
```
generateSample.py -ts=15
```
O programa generateSamples não retorna nenhuma saída. Os arquivos gerados podem ser verificados na pasta indicada no programa.
#### Iniciar o project:
1º (assume valores por default):
```
project.py
```
2º (valores inseridos pelo utilizador)
```
project.py -ws=1000 -sh=256 -tc=gzip -tn=pinknoise -t="..\\samples\\Adam Lambert - Runnin" -n=0.2
```
#### Iniciar o accuracy:
```
accuracy.py -ws=1000 -sh=256 -tc=gzip -tn=pinknoise -n=0.2
```

##### Resultados do project:
```
Adam Lambert - Runnin - 0.939521800281294
Ed Sheeran - Bad Habits (HBz Bounce Remix) - 1.0168776371308017
Cobra Effect - Bring The Voice (Original Mix) - 1.0196905766526019
BAD BUNNY x JHAY CORTEZ - DÁKITI - 1.0246132208157526
d1sHLGrmRCJ-z-0-y-61f5bfb0ee3aed2e95a2367e - 1.0246132208157526
DHuVLJwRoW6-z-0-y-61f5a799ee3aed2e95a22beb - 1.0246132208157526
ANGEMI - Witches (Original Mix) - 1.0267229254571026
Libercio - Flutter - 1.0314465408805031
Baxter's Science Serenade - 1.0323488045007032
Fifth Harmony ft. Kid Ink - Worth It (Bounce Squad Remix) - 1.0337552742616034
Tempo de execução:5.196348190307617
```

##### Resultados do accuracy:
Accuracy: 93.81443298969072
Tempo de execução: 566.162216424942