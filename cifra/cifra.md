## exercício Cifra 

_Samuel Cavalcanti_  

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

link para o código: [cifra](crypy)
