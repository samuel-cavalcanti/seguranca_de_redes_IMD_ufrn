_Samuel Cavalcanti_ 
## Configurando e testando o seu Firewall iptables
Nesta questão você precisará do iptables instalado em sua VM Servidora. Caso não esteja instalado, instale.
O objetivo desta questão é praticar a criação de regras no iptables, além de observar e compreender os seus
efeitos práticos.

Para isso, você deverá criar regras para satisfazer cada um dos itens listados abaixo. Sempre que achar
necessário, utilize ferramentas como wireshark ou tcpdump para visualizar o fluxo de dados.
Escreva em um arquivo bash script cada regra que você construir, para que possam ser devidamente aplicadas
em uma outra máquina.

### ATIVIDADES: 

1. Verifique as regras instaladas no iptables. Na possibilidade de haver alguma regra já definida, remova
(flush) todas. Caso não estejam, mude a política default de todas as chains (INPUT, OUTPUT e
FORWARD) para ACCEPT.

2. Tente efetuar um ping no endereço 8.8.8.8 de seu servidor. Agora faça o mesmo de sua máquina
cliente. Comente os resultados.

3. Aplique o conjunto de regras a seguir a fim de proteger a sua rede interna.  
- iptables -P INPUT DROP  
- iptables -P OUTPUT ACCEPT  
- iptables -P FORWARD DROP  

Efetue os mesmos passos da questão 2 e comente os resultados.

``` bash
ping 8.8.8.8 -c 5
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
--- 192.168.15.1 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 4105ms

```
Adicionando a regra __iptables -P INPUT DROP__  impede o host de receber a resposta do ping.


4. Em seu servidor, aplique o conjunto de regras a seguir:  
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT  
iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT  


Efetue os mesmos paços da questão 2 e comente os resultados.

```bash
ping 8.8.8.8 -c 5
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=67.8 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=66.9 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=65.7 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=68.0 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=67.8 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4025ms
rtt min/avg/max/mdev = 65.752/67.281/68.060/0.856 ms

```

com as novas regras do input :  
__iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT__  
__iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT__  

o firewall permite a entrada do request e reply dos pacotes icmp que o comando ping envia.



5. Habilite o acesso da rede interna à rede externa, ou seja, habilite o NAT entre as redes usando o
iptables.  

para habilitar o NAT foi executado os seguintes comandos:  

```bash 

# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE

# permitir o roteamento de ips 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"
# por padrão o roteamento de ips é falso 

```


6. Verifique se através de sua VM é possível pingar algum outro IP (por exemplo, seu host ou o 8.8.8.8).

```bash 
ping 8.8.8.8 -c 3
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=61 time=74.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=61 time=92.5 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=61 time=68.6 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 68.688/78.545/92.524/10.158 ms

```

7. Usando os utilitários __dig__ ou __nslookup__ tente resolver o endereço www.google.com.br. Comente os resultados.
```bash
dig www.google.com.br  +short
# comentei os resultados :D
# 172.217.30.3
```
O dig retorna o ip por trás do dns www.google.com.br 


8. Crie um conjunto de regras para que sua VM possa navegar, ou seja, acessar sites HTTP pela Internet.
Dica: lembre-se dos serviços necessários para a navegação na Internet.

para habilitar o acesso da rede interna à rede externa foi executado os seguintes comandos:  

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para librar ping
sudo iptables -A FORWARD -p icmp --icmp-type echo-request -j ACCEPT
sudo iptables -A FORWARD -p icmp --icmp-type echo-reply -j ACCEPT

# regras para liberar a internet 
# 53 = domain
# 80 = http 
# 443 = https

sudo iptables -A FORWARD -p tcp -m multiport --sport http,https,domain -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport http,https,domain -j ACCEPT

#DNS
sudo iptables -A FORWARD  -p udp --sport  domain -j ACCEPT
sudo iptables -A FORWARD  -p udp --dport  domain -j ACCEPT
 
```

9. Implemente um conjunto de regras que permita registrar (logar) todo o tráfego HTTP padrão, exceto
para o acesso ao portal do IMD (portal.imd.ufrn.br).  

```bash
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de FORWARD
sudo iptables -P FORWARD DROP


# regras para liberar a internet 
# 53 = domain
# 80 = http 
# 443 = https

sudo iptables -A FORWARD -p tcp -m multiport --sport http,https,domain -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport http,https,domain -j ACCEPT

# #DNS
sudo iptables -A FORWARD  -p udp --sport  domain -j ACCEPT
sudo iptables -A FORWARD  -p udp --dport  domain -j ACCEPT



# log de tudo menos portal.imd.ufrn.br que possui o ip 177.20.147.222
sudo iptables -I FORWARD 1 -p tcp --sport http --dport http -j LOG ! -s 177.20.147.222

```

10. Crie as regras necessárias para garantir que a sua VM só possa estabelecer conexões SSH para o host
www.seguro.com.br.

```bash
dig www.seguro.com.br +short
www.icpseguros.com.br.
icpseguros.com.br.
186.202.153.16

```

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP

# regras de FORWARD
sudo iptables -P FORWARD DROP

# ssh  www.seguro.com.br == 186.202.153.16
#ssh =22
sudo iptables -A FORWARD -p udp --sport ssh -s 186.202.153.16 -j ACCEPT
sudo iptables -A FORWARD -p udp --dport ssh -s 186.202.153.16 -j ACCEPT

sudo iptables -A FORWARD -p tcp --dport ssh -s 186.202.153.16 -j ACCEPT
sudo iptables -A FORWARD -p tcp --sport ssh -s 186.202.153.16 -j ACCEPT

```

11. Implemente um conjunto de regras que permita somente o acesso aos seguintes serviços externos:
HTTP, FTP, DNS, SMTP, POP e IMAP.

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP


# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para liberar a internet 
# 53 = domain
# 80 = http 
# #20/TCP FTP 
# #25/TCP,UDP SMTP
# #109/TCP POP
# #220/TCP,UDP IMAP

sudo iptables -A FORWARD -p tcp -m multiport --sport domain,http,ftp,25,109,220 -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport domain,http,ftp,25,109,220 -j ACCEPT


sudo iptables -A FORWARD  -p udp -m multiport --sport domain,25,109,220 -j ACCEPT
sudo iptables -A FORWARD  -p udp -m multiport --dport domain,25,109,220 -j ACCEPT
```

12. Implemente um conjunto de regras que permita o acesso somente a servidores HTTP seguros. Outros serviços deverão ser negados.  

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP


# regras de FORWARD
sudo iptables -P FORWARD DROP

sudo iptables -A FORWARD -p tcp -m multiport --sport domain,https -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport domain,https -j ACCEPT


sudo iptables -A FORWARD  -p udp -m multiport --sport domain -j ACCEPT
sudo iptables -A FORWARD  -p udp -m multiport --dport domain -j ACCEPT
```

13. Liberar o acesso SSH de qualquer origem.

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP

# regras de FORWARD
sudo iptables -P FORWARD DROP

#ssh =22
sudo iptables -A FORWARD -p tcp --dport ssh -j ACCEPT
sudo iptables -A FORWARD -p tcp --sport ssh -j ACCEPT

sudo iptables -A FORWARD -p udp --sport ssh -j ACCEPT
sudo iptables -A FORWARD -p udp --dport ssh -j ACCEPT
```

14. Seu servidor deve aceitar ping apenas de sua rede interna.

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP

# # permitindo o ping
sudo iptables -A INPUT -p icmp -m iprange --icmp-type echo-request --src-range 192.168.33.0-192.168.33.255  -j ACCEPT
sudo iptables -A INPUT -p icmp -m iprange --icmp-type echo-reply --src-range 192.168.33.0-192.168.33.255 -j ACCEPT


# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para librar ping
sudo iptables -A FORWARD -p icmp --icmp-type echo-request -j ACCEPT
sudo iptables -A FORWARD -p icmp --icmp-type echo-reply -j ACCEPT


```

15. Explique a função do conjunto de regras a seguir. Tente identificar o sentido de cada regra e, no seu
conjunto, do que tratam.
```bash
echo "0" > /proc/sys/net/ipv4/icmp_echo_ignore_all
$IPTABLES -N REGRA-X
$IPTABLES -A INPUT -p icmp --icmp-type echo-request -j REGRA-X
$IPTABLES -A REGRA-X -m limit --limit 1/s --limit-burst 4 -j RETURN
$IPTABLES -A REGRA-X -j DROP
```
- __echo "0" > /proc/sys/net/ipv4/icmp_echo_ignore_all__   
habilita o reply de um pacote icmp, ou seja torna a máquina "pingavel".

- __$IPTABLES -N REGRA-X__  
cria uma nova chain chamada REGRA-X.

- __$IPTABLES -A INPUT -p icmp --icmp-type echo-request -j REGRA-X__ 
transmite a resposta de um pacote icmp do tipo echo-request para a chain REGRA-X

-__$IPTABLES -A REGRA-X -m limit --limit 1/s --limit-burst 4 -j RETURN__  
define uma regra embaixo de todas as outras e essa regra diz que: retorna para a chain anterior caso aparaça mais que 4 pacotes em 1 segundo. 

- __$IPTABLES -A REGRA-X -j DROP__  
define uma regra embaixo de todas as outras e essa regra diz que: descarta todos os pacotes silenciosamente.
 

16. Explique a função do conjunto de regras a seguir. Tente identificar o sentido de cada regra e, no seu conjunto, do que tratam.
```bash
echo "0" > /proc/sys/net/ipv4/tcp_syncookies
$IPTABLES -N REGRA-Y
$IPTABLES -A INPUT -i $WAN -p tcp --syn -j REGRA-Y
$IPTABLES -A REGRA-Y -m limit --limit 1/s --limit-burst 4 -j RETURN
$IPTABLES -A REGRA-Y -j DROP
```
- __echo "0" > /proc/sys/net/ipv4/tcp_syncookies__   
desabilita a proteção contra SYN flood attack

- __$IPTABLES -N REGRA-Y__  
cria uma nova chain chamada REGRA-Y.

- __$IPTABLES -A INPUT -i $WAN -p tcp --syn -j REGRA-Y__  
cria uma regra na posição __$WAN__ que transmite as possíveis conexões tcp para a chain REGRA-Y

- __$IPTABLES -A REGRA-Y -m limit --limit 1/s --limit-burst 4 -j RETURN__  
define uma regra embaixo de todas as outras e essa regra diz: retorna para a chain anterior caso aparaça mais que 4 pacotes em 1 segundo. 

- __$IPTABLES -A REGRA-Y -j DROP__  
define uma regra embaixo de todas as outras e essa regra diz: descarta todos os pacotes silenciosamente.

17. Implemente um firewall/proxy transparente com o iptables e Squid (pesquisar). O serviço Squid será configurado na porta 3300. Implemente um conjunto de regras que permita que requisições que vierem da rede interna para acesso internet sejam automaticamente redirecionadas para a porta usada pelo Squid. Testem a sua implementação.

```bash
sudo squid -a 3300 # configurando o squid para  a porta 3300

```

```bash
# regras de PREROUTING (DNAT)

sudo iptables -t nat -A PREROUTING -i enp0s8 -s 192.168.33.1/24 -p tcp --dport http -j REDIRECT --to-port 3300

# regras de POSTROUTING (SNAT)
										#-o enp0s3 (interface de saida)
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"

# regras de INPUT
sudo iptables -P INPUT ACCEPT

# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para librar ping
sudo iptables -A FORWARD -p icmp --icmp-type echo-request -j ACCEPT
sudo iptables -A FORWARD -p icmp --icmp-type echo-reply -j ACCEPT

# regras para liberar a internet 
# 53 = domain
# 80 = http 
# 443 = https
sudo iptables -A FORWARD -o enp0s3 -i enp0s8 -s 192.168.33.1/24 -m conntrack --ctstate NEW -j ACCEPT
sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

sudo iptables -A FORWARD -p tcp -m multiport --sport http,https,domain -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport http,https,domain -j ACCEPT

#DNS
sudo iptables -A FORWARD  -p udp --sport  domain -j ACCEPT
sudo iptables -A FORWARD  -p udp --dport  domain -j ACCEPT

# regras de OUTPUT
sudo iptables -P OUTPUT ACCEPT
```

```bash

# regras de PREROUTING (DNAT)
# redirecionando a porta http para o squid
sudo iptables -t nat -A PREROUTING -i enp0s8 -s 192.168.33.1/24 -p tcp --dport http -j REDIRECT --to-port 3300 

# regras de POSTROUTING (SNAT)
										#-o enp0s3 (interface de saida)
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para librar ping
sudo iptables -A FORWARD -p icmp --icmp-type echo-request -j ACCEPT
sudo iptables -A FORWARD -p icmp --icmp-type echo-reply -j ACCEPT

# regras para liberar a internet 
# 53 = domain
# 80 = http 
# 443 = https

sudo iptables -A FORWARD -p tcp -m multiport --sport http,https,domain -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport http,https,domain -j ACCEPT

#DNS
sudo iptables -A FORWARD  -p udp --sport  domain -j ACCEPT
sudo iptables -A FORWARD  -p udp --dport  domain -j ACCEPT


```
referencia: https://coderwall.com/p/t_isaa/create-a-gateway-with-a-transparent-proxy-iptables-squid


18. Permitir o acesso a servidores MySQL e PostgreSQL apenas para conexões da rede interna.

```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP

# # permitindo o ping
sudo iptables -A INPUT -p icmp -m iprange --icmp-type echo-request --src-range 192.168.33.0-192.168.33.255  -j ACCEPT
sudo iptables -A INPUT -p icmp -m iprange --icmp-type echo-reply --src-range 192.168.33.0-192.168.33.255 -j ACCEPT

#servidor MYSQL e POSTGRESQL (não precisa se o servidor for outro ip)
sudo iptables -A INPUT -p tcp -m multiport -m iprange --sport 3306,5432 --src-range 192.168.33.0-192.168.33.255  -j ACCEPT
sudo iptables -A INPUT -p tcp -m multiport -m iprange --dport 3306,5432 --src-range 192.168.33.0-192.168.33.255  -j ACCEPT

sudo iptables -A INPUT -p udp -m iprange --sport 3306 --src-range 192.168.33.0-192.168.33.255 -j ACCEPT
sudo iptables -A INPUT -p udp -m iprange --dport 3306 --src-range 192.168.33.0-192.168.33.255 -j ACCEPT

# regras de FORWARD
sudo iptables -P FORWARD DROP


# 3306/tcp,udp MYSQL
# 5432/tcp	POSTGRESQL
MYSQLSERVER=192.168.33.1
POSTGRESQL=192.168.33.1

sudo iptables -A FORWARD -p tcp -m multiport -m iprange --sport 3306,5432 --src-range 192.168.33.0-192.168.33.255 -d $MYSQLSERVER,$POSTGRESQL -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport -m iprange --dport 3306,5432 --src-range 192.168.33.0-192.168.33.255 -d $MYSQLSERVER,$POSTGRESQL -j ACCEPT

sudo iptables -A FORWARD -p udp -m iprange --sport 3306 --src-range 192.168.33.0-192.168.33.255 -d $MYSQLSERVER -j ACCEPT
sudo iptables -A FORWARD -p udp -m iprange --dport 3306 --src-range 192.168.33.0-192.168.33.255 -d $MYSQLSERVER -j ACCEPT

# regras de OUTPUT
sudo iptables -P OUTPUT ACCEPT
```

19. Permitir todo tráfego de entrada para o serviço SMTP, IMAP, IMAPS, POP3 e POP3S.


```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de INPUT
sudo iptables -P INPUT DROP


# regras de FORWARD
sudo iptables -P FORWARD DROP
 
# POP3
# Port 110/TCP - this is the default POP3 non-encrypted port
# Port 995/TCP - this is the port you need to use if you want to connect using POP3 securely

# IMAP -tcp
# Port 143/TCP,UDP - this is the default IMAP non-encrypted port
# Port 993/TCP - this is the port you need to use if you want to connect using IMAP securely
# 220/TCP,UDP IMAP version 3

# SMTP
# Port 25/TCP,UDP - this is the default SMTP non-encrypted port
# Port 465/TCP - this is the port used if you want to send messages using SMTP securely
# 366/TCP,UDP SMTP

# Fonte: https://pt.wikipedia.org/wiki/Lista_de_portas_dos_protocolos_TCP_e_UDP 

sudo iptables -A FORWARD -p tcp -m multiport --sport 110,995,143,993,220,25,465,366 -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport 110,995,143,993,220,25,465,366 -j ACCEPT

sudo iptables -A FORWARD -p udp -m multiport --sport 143,220,25,366  -j ACCEPT
sudo iptables -A FORWARD -p udp -m multiport --dport 143,220,25,366  -j ACCEPT


```

20. Permitir o acesso ao Facebook apenas no período de almoço, ou seja, das 12:00h às 14:00h.

```bash
dig www.facebook.com +short                                                                  
star-mini.c10r.facebook.com.
157.240.222.35
```


```bash
# habilitar o NAT
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE 
sudo su -c "echo "1" > /proc/sys/net/ipv4/ip_forward"


# regras de FORWARD
sudo iptables -P FORWARD DROP

# regras para liberar a internet 
# 53 = domain
# 80 = http 
# 443 = https


sudo iptables -A FORWARD -s 157.240.222.35 -m time --timestart 12:00 --timestop 14:00 -j ACCEPT
sudo iptables -A FORWARD -s 157.240.222.35 -j DROP


sudo iptables -A FORWARD -p tcp -m multiport --sport http,https,domain -j ACCEPT
sudo iptables -A FORWARD -p tcp -m multiport --dport http,https,domain -j ACCEPT

#DNS
sudo iptables -A FORWARD  -p udp --sport  domain -j ACCEPT
sudo iptables -A FORWARD  -p udp --dport  domain -j ACCEPT

```