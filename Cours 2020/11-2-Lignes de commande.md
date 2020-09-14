Certaines commandes du [terminal](https://fr.wikipedia.org/wiki/Terminal_(informatique)) 
permettent d'obtenir des informations sur le réseau.

Les commandes suivantes concernent le terminal Linux. 
Elles existent sur les autres Systèmes d'Exploitation mais, parfois, sous une syntaxe différente.

* **ip a**

Cette commande permet d'obtenir les informations sur son poste ([adresse MAC](https://fr.wikipedia.org/wiki/Adresse_MAC), 
[adresse IP](https://fr.wikipedia.org/wiki/Adresse_IP), ...)
```
utilisateur@machine:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.x/24 brd 192.168.0.255 scope global dynamic noprefixroute enp2s0
       valid_lft 2674sec preferred_lft 2674sec
    inet6 xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64 scope global temporary dynamic 
       valid_lft 3600sec preferred_lft 3600sec
    inet6 xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 3600sec preferred_lft 3600sec
    inet6 xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

* **nslookup**

Cette commande permet de rechercher les informations dans le 
[Domain Name System (DNS)](https://fr.wikipedia.org/wiki/Domain_Name_System), qui associe nom de domaine et adresses IP.

```
utilisateur@machine:~$ nslookup www.inria.fr
Server:  127.0.1.1
Address: 127.0.1.1#53

Non-authoritative answer:
www.inria.fr canonical name = ezp3.inria.fr.
Name: ezp3.inria.fr
Address: 128.93.162.84
```


* **ping**

Cette commande permet de tester l'accessibilité d'une autre machine à travers un réseau IP.
```
utilisateur@machine:~$ ping www.inria.fr -c 4
PING ezp3.inria.fr (128.93.162.84) 56(84) bytes of data.
64 bytes from ezp3.inria.fr (128.93.162.84): icmp_seq=1 ttl=46 time=229 ms
64 bytes from ezp3.inria.fr (128.93.162.84): icmp_seq=2 ttl=46 time=231 ms
64 bytes from ezp3.inria.fr (128.93.162.84): icmp_seq=3 ttl=46 time=230 ms
64 bytes from ezp3.inria.fr (128.93.162.84): icmp_seq=4 ttl=46 time=229 ms

--- ezp3.inria.fr ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 229.824/230.516/231.779/0.931 ms
```

* **traceroute**

Cette commande permet de suivre les chemins qu'un paquet de données (paquet IP) 
va prendre pour aller de la machine locale à une autre machine connectée au réseau IP.

```
utilisateur@machine:~$ traceroute www.cnil.fr
traceroute to www.cnil.fr (46.18.194.181), 30 hops max, 60 byte packets
 1  _gateway (10.X.X.X)  0.685 ms  1.453 ms  1.820 ms
 2  10.X.X.X (10.X.X.X)  5.894 ms  5.894 ms  5.877 ms
 3  200-159-101-97.customer.tdatabrasil.net.br (200.159.101.97)  6.396 ms  6.330 ms  6.344 ms
 4  187-8-227-129.customer.tdatabrasil.net.br (187.8.227.129)  6.541 ms  6.577 ms  6.625 ms
 5  187-100-173-166.dsl.telesp.net.br (187.100.173.166)  6.561 ms 187-100-35-241.dsl.telesp.net.br (187.100.35.241)  6.614 ms  6.637 ms
 6  84.16.7.69 (84.16.7.69)  19.749 ms 84.16.7.73 (84.16.7.73)  12.398 ms  12.725 ms
 7  5.53.3.167 (5.53.3.167)  121.298 ms  125.218 ms  125.231 ms
 8  ix-ae-15-0.tcore1.mln-miami.as6453.net (63.243.152.141)  120.166 ms  120.423 ms  121.078 ms
 9  if-ae-7-2.tcore1.aeq-ashburn.as6453.net (66.198.154.177)  218.954 ms  223.439 ms  219.896 ms
10  if-ae-2-2.tcore2.aeq-ashburn.as6453.net (216.6.87.1)  217.500 ms  217.857 ms  218.324 ms
11  if-ae-12-2.tcore4.njy-newark.as6453.net (216.6.87.43)  218.813 ms  223.626 ms  221.335 ms
12  if-ae-1-3.tcore3.njy-newark.as6453.net (216.6.57.5)  216.807 ms  217.683 ms  213.843 ms
13  if-ae-15-2.tcore1.l78-london.as6453.net (80.231.130.25)  218.540 ms  218.502 ms  223.580 ms
14  if-ae-3-2.tcore1.pye-paris.as6453.net (80.231.154.142)  220.433 ms  220.173 ms  224.672 ms
15  if-ae-11-2.tcore1.pvu-paris.as6453.net (80.231.153.49)  220.797 ms  217.033 ms  221.828 ms
16  80.231.153.82 (80.231.153.82)  224.743 ms  225.106 ms  225.484 ms
17  ds-198-145.dri-services.net (46.18.198.145)  233.192 ms  222.404 ms  218.379 ms
18  ds-198-145.dri-services.net (46.18.198.145)  223.167 ms *  228.464 ms
```

On peut alors déterminer le [chemin parcouru](https://stefansundin.github.io/traceroute-mapper/?trace=1%20%20_gateway%20(10.X.X.X)%20%200.685%20ms%20%201.453%20ms%20%201.820%20ms%0A%202%20%2010.X.X.X%20(10.X.X.X)%20%205.894%20ms%20%205.894%20ms%20%205.877%20ms%0A%203%20%20200-159-101-97.customer.tdatabrasil.net.br%20(200.159.101.97)%20%206.396%20ms%20%206.330%20ms%20%206.344%20ms%0A%204%20%20187-8-227-129.customer.tdatabrasil.net.br%20(187.8.227.129)%20%206.541%20ms%20%206.577%20ms%20%206.625%20ms%0A%205%20%20187-100-173-166.dsl.telesp.net.br%20(187.100.173.166)%20%206.561%20ms%20187-100-35-241.dsl.telesp.net.br%20(187.100.35.241)%20%206.614%20ms%20%206.637%20ms%0A%206%20%2084.16.7.69%20(84.16.7.69)%20%2019.749%20ms%2084.16.7.73%20(84.16.7.73)%20%2012.398%20ms%20%2012.725%20ms%0A%207%20%205.53.3.167%20(5.53.3.167)%20%20121.298%20ms%20%20125.218%20ms%20%20125.231%20ms%0A%208%20%20ix-ae-15-0.tcore1.mln-miami.as6453.net%20(63.243.152.141)%20%20120.166%20ms%20%20120.423%20ms%20%20121.078%20ms%0A%209%20%20if-ae-7-2.tcore1.aeq-ashburn.as6453.net%20(66.198.154.177)%20%20218.954%20ms%20%20223.439%20ms%20%20219.896%20ms%0A10%20%20if-ae-2-2.tcore2.aeq-ashburn.as6453.net%20(216.6.87.1)%20%20217.500%20ms%20%20217.857%20ms%20%20218.324%20ms%0A11%20%20if-ae-12-2.tcore4.njy-newark.as6453.net%20(216.6.87.43)%20%20218.813%20ms%20%20223.626%20ms%20%20221.335%20ms%0A12%20%20if-ae-1-3.tcore3.njy-newark.as6453.net%20(216.6.57.5)%20%20216.807%20ms%20%20217.683%20ms%20%20213.843%20ms%0A13%20%20if-ae-15-2.tcore1.l78-london.as6453.net%20(80.231.130.25)%20%20218.540%20ms%20%20218.502%20ms%20%20223.580%20ms%0A14%20%20if-ae-3-2.tcore1.pye-paris.as6453.net%20(80.231.154.142)%20%20220.433%20ms%20%20220.173%20ms%20%20224.672%20ms%0A15%20%20if-ae-11-2.tcore1.pvu-paris.as6453.net%20(80.231.153.49)%20%20220.797%20ms%20%20217.033%20ms%20%20221.828%20ms%0A16%20%2080.231.153.82%20(80.231.153.82)%20%20224.743%20ms%20%20225.106%20ms%20%20225.484%20ms%0A17%20%20ds-198-145.dri-services.net%20(46.18.198.145)%20%20233.192%20ms%20%20222.404%20ms%20%20218.379%20ms%0A18%20%20ds-198-145.dri-services.net%20(46.18.198.145)%20%20223.167%20ms%20*%20%20228.464%20ms%0A).

![traceroute wwww.cnil.fr](https://jdolivet.github.io/ISN-Cours/Cours%202019/11-3-Traceroute%20visualisation.png)
