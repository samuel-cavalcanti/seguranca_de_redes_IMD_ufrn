# seguranca de redes IMD

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
o deslocamento é de valor 33 e a resposta é:  
````
Olha que coisa mais linda
Mais cheia de graça
E ela, menina
Que vem e que passa
Num doce balanco
A caminho do mar

Moça do corpo dourado
Do sol de Ipanema
O seu balançado é mais que um poema
É a coisa mais linda que eu ja vi passar

Ah, por que estou tao sozinho?
Ah, por que tudo e tao triste?
Ah, a beleza que existe
A beleza que nao e so minha
Que tambem passa sozinha

Ah, se ela soubesse
Que quando ela passa
O mundo inteirinho se enche de graca
E fica mais lindo
Por causa do amor
````

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


## Estudo sobre os Modos de Operação de cifra de bloco  
Aprofunde os seus estudo sobre o algoritmo de criptografia DES apresentado nesta aula e explique os diferentes modos de operação de cifras de bloco, deixando claro as vantagens de cada um.


### Eletronic CodeBook (ECB)  
Cada bloco de bits de texto claro é codificado independentemente usando a mesma chave

#### Vantagem:  

+ O modo mais simples de criptografia, Fácil implementação 

+ os blocos são cifrados independentemente , podendo ser paralelizado

+ Um ou mais bits de erro na operação de cifrar em um determinado bloco, afeta a operação de decifrar do próprio bloco, não se propagando

+ é o algoritmo mais rápido dessa lista

#### Desvantagem:
+ Blocos idênticos possuem textos cifrados idênticos se utilizado a mesma chave, ou seja ele não oculta padrões dos dados

+ Não recomendo para mensagens de maiores do que um bloco ou se houver possibilidade de reuso de chave em blocos idênticos de mensagens diferentes

### Cipher-block chaining (CBC)
A entrada do algoritmo de encriptação é o XOR dos 64 bits de texto claro e os 64 bits anteriores de texto cifrado

#### Vantagem:  

+ tão simples e fácil de implementação quando ECB 

+ Cada bloco cifrado fica dependente de todos os blocos de texto simples processados até este momento, ocultando os padrões dos dados 

+ Um único erro de bit em um texto cifrado afeta a operação de decifrar do próprio bloco e do bloco seguinte. Os demais blocos são decifrados corretamente

#### Desvantagem:
+ Sua criptografia é sequencial ou seja não pode ser paralelizada  

+ Modificações em um bloco de texto legível durante o processo de cifrar altera todos os blocos de texto cifrado subsequentes. Isto inviabiliza que esse modo de operação seja utilizado em aplicações que requeiram acesso de ler/gravar randômicos para encriptar dados.


### CIPHER FEEDBACK (CFB)
A entrada é processada _s_ bits de cada vez. O texto cifrado anterior é usado como entrada para o algoritmo de encriptação a fim de produzir saida pseudoaleatória, que é aplicada a um XOR com o texto claro para criar a próxima unidade de texto cifrado

#### Vantagem:

+ é uma cifra de fluxo , ou seja  pode operar em tempo real e não necessita preencher uma mensagem para que haja um número inteiro de blocos 

+  assim como CBC, sua criptografia oculta os padrões dos dados 

#### Desvantagem:

+ Assim como CBC, a sua criptografia é sequencial impossibilitando o paralelismo

+  Modificações em um bloco de texto legível durante o processo de cifrar altera todos os blocos de texto cifrado subsequentes. Isto inviabiliza que esse modo de operação seja utilizado em aplicações que requeiram acesso de ler/gravar randômicos para encriptar dados.

### Output FeedBack (OFB)
Semelhante ao CFB, exceto que a entrada do algoritmo de encriptação é a saida DES anterior, e são usados blocos completos 

#### Vantagem:

+ Erro de bit na transmissão não se propagam. Se acontecer de um ou mais bits de erro em qualquer carácter de um texto cifrado comprometerá apenas a decifração daquele bloco, na precisa posição do erro

+ Assim como CFB, o OFB é uma cifra de fluxo ou seja pode operar em temo real

#### Desvantagem:

+ O OFB é mais vulnerável a um ataque por modificação de fluxo de mensagem do que o CFB


### CounTeR (CTR)
Cada bloco de texto claro é aplicado a um XOR com contador encriptado. O contador é incrementado para cada bloco subsequente


#### Vantagem:

+ CTR tem vantagens de eficiência significantes sobre os modos de operação de
confidencialidade padronizados, sem reduzir a segurança

+ O bloco de texto cifrado i não necessita ser decifrado antes do bloco i+1, ou seja, é paralelizável 

#### Desvantagem:

+ Sucessivos blocos CTR e CTR+1 tem pequenas diferenças de Hamming Isto pode municiar um atacante em obter muitos pares de textos legíveis com uma pequena diferença conhecida, o que deveria facilitar uma criptoanálise diferencial. Mas isso só ocorrerá, se a cifra básica for fraca.


#### Referencias :
Stallings, William. "Criptografia e segurança de redes. Princípios e práticas, ch. 6." (2006).

Ribeiro, Carlos Henrique Calazans, and Luciana Hyodo Roiha. "Estudo Comparativo dos Modos de Operação de Confidencialidade: um Overview para Iniciantes." Revista Ciência e Tecnologia 8.13 (2010).


## Cifras Modernas:  Simple DES e RC4

Implemente o algoritmo de criptografia S-DES apresentado em aula para cifrar/decifrar um
arquivo texto passado por parâmetro em linha de comando.

Implementar o protótipo do algoritmo RC4 para cifra qualquer texto usando uma chave de
tamanho variável entre 1 a 256 bytes.

### Solução apresentada

para essa atividade foi necessário criar duas classes: SimpleDes e RC4. Para cifrar textos a partir desses algorítmos foi necessário criar uma interface por linha de comando chamado de __encrypt__. Ele é um script python que recebe 4 argumentos:

- Primeiro argumento você escolher se vai usar o Simple DES ou RC4, caso seja escolha  o Simple DES digite: __des__, caso seja RC4 digite: __rc4__.

- Segundo argumento é o aquivo que contém a mensagem cifrada ou não.

- Terceiro argumento é a chave, os critérios da chave variam dependendo do algorítmo a ser utilizado caso seja o Simple Des a chave só pode ter um carácter, o RC4 pode ter até  256 caracteres , o resto será descartado.

- Quarto argumento indica se você vai encriptar a mensagem ou vai descriptografar a mensagem. Digite __e__ para encriptar ou  __d__ para descriptografar.


Exemplo: utilizando o des para encriptar a mensagem:
```zsh
$ cd cifras_modernas_simetricas
# python3 caso esteja utilizando ubuntu
$ python encrypt.py des message.txt e e 
```

Exemplo: utilizando o RC4 para encriptar a mensagem:
```zsh
$ cd cifras_modernas_simetricas
# python3 caso esteja utilizando ubuntu
$ python encrypt.py rc4 message.txt segredo e 
```

Tando as classes quanto a interface pode ser encontrado na pasta [cifras_modernas_simetricas](cifras_modernas_simetricas/). Nos arquivos: [s_des.py](cifras_modernas_simetricas/s_des.py), [rc4.py](cifras_modernas_simetricas/rc4.py) e [encrypt.py](cifras_modernas_simetricas/encrypt.py).


## Chat seguro  
Desenvolva uma aplicação para troca de mensagens de texto (estilo chat) entre você e seus colegas de maneira que seja possível trocar mensagens de texto entre pares utilizando criptografia com o S-DES e o RC4, desenvolvidos por você

- Assuma que a comunicação será feita pela porta 5354, com socket TCP

- Assuma também que ambos os pares já conhecem a chave de segurança e essa poderá ser
modificada pelo usuário em tempo de execução da aplicação, bem como o algoritmo de
criptografia utilizado (S-DES ou RC4)


### Solução apresentada  

Para essa Atividade foi necessário criar duas classes Server e Client. A classe server é responsável por transmitir a mensagem para todos os clientes. A classe cliente é responsável por receber, enviar, cifrar e descifrar a mensagem.


Exemplo de utilização em localhost: 

```zsh
$ cd cifras_modernas_simetricas
# python3 caso esteja utilizando ubuntu
$ python socket_server.py
```

Abra outro terminal.

```zsh
$ cd cifras_modernas_simetricas
# python3 caso esteja utilizando ubuntu
$ python socket_client.py 127.0.0.1 
```

abra mais um terminal.

```zsh
$ cd cifras_modernas_simetricas
# python3 caso esteja utilizando ubuntu
$ python socket_client.py 127.0.0.1 
```
<!-- 
Boatos dizem que ter um tempo para conversar consigo mesmo é bom para saúde. Experimente.  
**Lembrar de apagar isso antes de enviar para o professor** -->

O chat possui alguns comandos que são apresentados ao usuários assim que eles se conectam. Esses comandos são:

- __\exit__ para sair do chat

- __\crypt sdes "chave"__ para cifrar a conversa usando o simple DES, onde a chave deve ser escrita entre aspas duplas e permitindo apenas zeros e uns

- __\crypt rc4 "segredo"__ para cifrar a conversa usando o RC$, onde a chave pode ter no máximo 256 caracteres 

- exemplo de utilização do __Simple DES__ :  \crypt sdes "1010101010"  
Observe que a chave só tem 10 dígitos, onde cada digito representa um byte, a chave do Simple DES tem o tamanho máximo de 10 bytes  

- exemplo de utilização do __RC4__ :   \crypt rc4 "segredo"  
No RC4 a chave ou frase que digitar entre as aspas duplas devera ser menor ou igual a 256 caracteres se a chave dada for maior que 256 caracteres o resto da frase ou da palavra será descartado  

### Dificuldades 

A única e verdadeira dificuldade encontrada em todas as atividades foi a implementação do RC4, ao contrário dos outros algoritmos ele possui muita operação aritmética, algo que pessoalmente me deixou confuso alem de ter demorado 30 minutos pesquisando na internet como usar o o algoritmo para descifrar, algo que me frustrou muito. Nas demais atividades, apesar de não ter uma dificuldade, foram trabalhos trabalhosos, ou seja requeriam um certo tempo e organização para que tudo seja feito em tempo hábil.  
