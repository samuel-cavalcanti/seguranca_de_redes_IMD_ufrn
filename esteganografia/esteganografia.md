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
$ cd esteganografia
$ chmod +x hide_on_the_image # tornar o script executável
$ ./hide_on_the_image pictures/teddy_bear_2.bmp message.txt 
# o último comando vai gerar uma nova imagem chamada modified_image.bmp na pasta pictures
```
 Para recuperar a mensagem dentro da imagem :
 
 ```zsh
#  estando dentro da pasta esteganografia execute: 
$ ./hide_on_the_image pictures/modified_image.bmp 
# o último comando deve mostrar na tela todo o README.md 
```