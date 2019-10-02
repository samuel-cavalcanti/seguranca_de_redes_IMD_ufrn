## Operação “Leva Jeito”
Implemente o programa guarda que, usando de calculo de puro Hash ou HMAC, permita garantir a autenticação de um conjunto de arquivos para uma determinada pasta (recursivamente). O programa deverá ser executado em linha de comando, seguindo a sintaxe:  

__./guarda < metodo > < opcao> < pasta > < saída >__  

- método : indica o método a ser utilizado ( -hash ou -hmac senha)
- opção: indica a ação a ser desempenhada pelo programa
    - -i: inicia a guarda da pasta indicada em <pasta>, ou seja, faz a leitura de todos os arquivos da pasta (recursivamente)  

    - -t: faz o rastreio (tracking) da pasta indicada em <pasta>, inserindo informações sobre novos arquivos e indicando

    - -x: desativa a guarda e remove a estrutura alocada

- pasta: indica a pasta a ser “guardada

- saida: indica o arquivo de saída para o relatório (-o saída). Caso não seja passado este parâmetro saída deve ser feita em tela.  



### Solução apresentada  
Para essa atividade foi feito um script python que calculava os hashs dos arquivos e caso houvesse uma diferença entre o hash armazenado e o hash calculado era verificado essa diferença.
Foi adotado o mesmo padrão do Unix para receber os parâmetros do script o que diverge levemente o pedido. Onde  ao invés de digitar __-hash__ ou __-hmac__ , deve-se passar __--hash__ ou __--hmac senha__. Também foi sugerido a utilização da implementação da estrutura arvore B para otimizar o software, mas por motivos de simplificação, a estrutura utilizada o json.

#### exemplo de uso:
Para utilizar o script guarda, clone esse repositório ou baixe o script separadamente, clicando no link: [guarda](hash/guarda) e salve o arquivo __ctrl + s__ caso esteja usando google chrome.

```zsh
# primeiro torne o script executável 
chmod +x guarda
# depois execute o script passando corretamente os parâmetros
# caso tenha alguma duvida use -h 
./guarda --hash -i .# exemplo de saida:
# monitorando os arquivos: 
# 	./.gitignore  f44f56cbf895e7325f3e9a31c0083045
# 	./guarda  301ce6ab30711d7704c5f77e98825c3f

```

#### dificuldades:
A atividade em geral é bem simples quando resolvida de maneira ingênua. Tendo em vista que não foi utilizado nenhuma estrutura de dados para otimizar a aplicação, logo não houve complicações. 


#### testes:
Para mostrar o funcionamento do __guarda__ foi feito um vídeo:  

[![](http://img.youtube.com/vi/vWDRlpgR6Bo/0.jpg)](http://www.youtube.com/watch?v=vWDRlpgR6Bo "Teste guarda")