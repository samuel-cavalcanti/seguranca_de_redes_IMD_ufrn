# eduroam

_Samuel Cavalcanti_
<!-- https://github.com/samuel-cavalcanti/seguranca_de_redes_IMD/blob/master/eduroam.md -->
## O que é eduroam ? 

Eduroam significa (education roaming) é um serviço mundial de acesso seguro a internet para a comunidade acadêmica. Apesar de ter iniciado na Europa , hoje mais de 100 países participam desse projeto e no Brasil o eduroam tem mais de 2.600 prontos de acesso, desde universidades, centros de pesquisa, praças públicas, aeroportos e cafeterias. 

Você pode ver todos os pontos de acesso do eduroam aqui nesse link : [pontos de acesso eduroam](https://monitor.eduroam.org/map_service_loc.php).

## Como eu faço para me conetar ?  

Dependendo da instituição de pesquisa o eduroam possui um assistente de configuração  que pode ser encontrado nesse link: [eduroam CAT](https://cat.eduroam.org/).  
Caso sua instituição não possui um assistente de configuração, você pode tentar se conectar manualmente como a rede, é uma sequência de passos simples:

- Encontre o uma rede wifi com o nome __eduroam__.  

- tente se conectar a rede.

- ela vai lhe pedir o nome do seu usuário e senha. 

- forneça os mesmos dados da sua instituição.

Caso tenha fornecido tudo correto  <!-- alguém vai pegar o seus dados e trancar a sua matricula  --> você terá acesso a internet.



## eduroam é seguro ?  

Segundo o [site deles](https://www.eduroam.org/eduroam-security/), o eduroam é baseado nos mais seguros padrões de criptografia e autenticação existentes atualmente. O usuário também deve estar ciente que cada ponto de acesso do eduroam possui sua configuração de firewall, ou seja, dependendo do ponto de acesso você pode ou não ver conteúdos adultos, pro exemplo.

O eduroam requer o uso do [IEEE 802.1X](https://pt.wikipedia.org/wiki/IEEE_802.1X) que fornece criptografia de ponta a ponta para garantir  que suas credenciais de usuário privado estejam disponíveis apenas para sau instituição de origem. O certificado de sua instituição de origem é o único que você precisa confiar. 


O eduroam não trabalha com web portal ou Captive Portal ou Splash-Screen, pois esses mecanismos de autenticação requerem que você confie no ponto de acesso, enviando seu usuário e senha sem criptografia, quebrando a ideia de criptografia de ponta a ponta. Também como o eduroam está presente em vários países, necessitária criar vários layouts diferentes, possibilitando o usuário ser incapaz de distinguir um site falso do original.