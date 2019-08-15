# seguranca_de_redes_IMD

## exercício Cifra 
Escreva um programa (na linguagem que você domina) que permitam cifrar e decifrar um arquivo de
texto indicado pela linha de comando, seguindo a __Cifra de Troca de Data__. O script deve ler um arquivo de texto em claro (não cifrado - .txt), indicado na linha de comando e gerar um arquivo texto cifrado (.sec). Para decifragem deve ler um arquivo de texto cifrado (.sec), indicado na linha de comando e imprimir em tela o texto decifrado
### Solução apresentada:  
foi feito um script em python que recebe dois argumentos uma data e o caminho de um arquivo.  
Exemplo de uso:  

__cifrando frase__: 
``` bash
$ chmod + x crypy # para tornar o script executável
$ echo "mensagem que deve ser cifrada" > messagem.txt
$ ./crypy 02/5/2019 messagem.txt
```  

__descifrando frase__:
``` bash
$ ./crypy 02/5/2019 messagem.sec  
mensagem que deve ser cifrada # provável output
```  

link para o código: [cifra](cifra/crypy)


## exercícios de Criptoanálise
Todos os arquivos desse exercício podem ser encontrados na pasta [criptoanalise](criptoanalise/)

###  Quebrar cifra de César

Escreva um programa que quebre por força bruta a cifra de César  
#### Messagem a ser descifrada:  
````
sSOHEX?LEJVPZHETHPZESPUKH
qHPZEJOLPHEKLENYHçH
iELSHGETLUPUH
u?LE,LTELEX?LEWHZZH
r?TEKVJLEIHSHUJV
eEJHTPUOVEKVETHY

qVçHEKVEJVYWVEKV?YHKV
hVEZVSEKLEmWHULTH
sEZL?EIHSHUçHKVEéETHPZEX?LE?TEWVLTH
ÉEHEJVPZHETHPZESPUKHEX?LEL?EQHE,PEWHZZHY

eOGEWVYEX?LELZ V?E HVEZVdPUOVF
eOGEWVYEX?LE ?KVELE HVE YPZ LF
eOGEHEILSLdHEX?LELbPZ L
eEILSLdHEX?LEUHVELEZVETPUOH
u?LE HTILTEWHZZHEZVdPUOH

eOGEZLELSHEZV?ILZZL
u?LEX?HUKVELSHEWHZZH
sET?UKVEPU LPYPUOVEZLELUJOLEKLENYHJH
iEMPJHETHPZESPUKV
tVYEJH?ZHEKVEHTVY
````
link para baixar o txt: [encripted text](criptoanalise/cifra_de_cesar/encripted_text.txt)


#### Solução apresentada:  
Foi feito um scrip em python que lê o arquivo  [encripted text](criptoanalise/cifra_de_cesar/encripted_text.txt) e testa todas as 55 combinações possíveis e salva cada uma em um arquivo.  
o deslocamento é de valor 7 e a resposta é:  
````
OLHA QUE COISA MAIS LINDA
MAIS CHEIA DE GRAçA
E ELA, MENINA
QUE VEM E QUE PASSA
NUM DOCE BALANCO
  CAMINHO DO MAR

MOçA DO CORPO DOURADO
DO SOL DE IPANEMA
O SEU BALANçADO é MAIS QUE UM POEMA
É A COISA MAIS LINDA QUE EU JA VI PASSAR

 H, POR QUE ESTOU TAO SOZINHO?
 H, POR QUE TUDO E TAO TRISTE?
 H, A BELEZA QUE EXISTE
  BELEZA QUE NAO E SO MINHA
QUE TAMBEM PASSA SOZINHA

 H, SE ELA SOUBESSE
QUE QUANDO ELA PASSA
O MUNDO INTEIRINHO SE ENCHE DE GRACA
E FICA MAIS LINDO
POR CAUSA DO AMOR
````
__OBS:__ foi encontrado uma segunda cifra de Cesár de valor 29 , talvéz exista uma terceira 

### Quebrar a cifra de Vigenère
Escreva um programa que desencripte a mensagem cifrada com a cifra de Vigenère  
````
W gags domj a esgpi so eiu dm goze qnyjaaxa hikinq frmh tvkdea irvwfea eaee frmh peefoa
se gvugw

````
### Solução apresentada:
Primeiro foi implementado um programa que desencripta uma message com a cifra de Vigenère.
Segundo foi descoberto por tentativa e erro qual era a chave. Sabendo que a música se chama Garota de Ipanema, 
então tentei __ipanema__ e obtive o seguinte resultado:  
````
o rato roeu a roupa do rei de roma enquanto haviam tres tigres tristes para tres pratos de trigo

````

## Exercício de Esteganografia  
Escreva um programa que lê uma mensagem e a esconda em um arquivo de imagem
no formato Bitmap (um dos formatos mais utilizados na esteganografia pelo fato de não
possuir compactação) e outro que permita extrair a mensagem do arquivo novamente.  
Técnica de ocultação: A cada 3 pixels da imagem, composto por 3 bytes cada (RGB), têm-se 9 bytes  
Desses 9 bytes, pegar o bit menos significativo dos 8 primeiros e ocultar os bits de caractere da mensagem
(char = 8 bits)  

### Solução apresentada  
Primeiramente obrigado _Stackoverflow_ , segundamente foi escrito um script em python que recebe a 
imagem com a mensagem embutida ou uma imagem qualquer e um arquivo txt contendo a mensagem.  
_OBS:_ para esse script foi utilizado a biblioteca de processamento de imagem chamada __OpenCV__  
Para sua instalação use o comando:
 ```zsh
 pip install opencv-python
```

Exemplo de utilização do script:  
```zsh
$ cat README.md > esteganografia/message.txt
$ echo "_|_" >> esteganografia/message.txt # esse é o token que simboliza o fim da mensagem
$ cd esteganografia
$ chmod +x hide_on_the_image # tornar o script executável
$ ./hide_on_the_image pictures/teddy_bear_2.bmp message.txt 
# o último comando vai gerar uma nova imagem chamada modified_image.bmp na pasta pictures

```
  
