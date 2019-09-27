## exercícios de Criptoanálise

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
link para baixar o txt: [encripted text](cifra_de_cesar/encripted_text.txt)


#### Solução apresentada:  
Foi feito um scrip em python que lê o arquivo  [encripted text](cifra_de_cesar/encripted_text.txt) e testa todas as 55 combinações possíveis e salva cada uma em um arquivo.  
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