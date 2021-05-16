#Käyttöohje
 
Lataa ohjelman lähdekoodi viimeisimmästä releasesta. 
Saat koodin ladattua "Assets"-otsikon alta valitsemalla "Source code" haluamallasi tiedostotyypillä (zip tai tar.gz)
 
##Käynnistäminen:
 
Asenna ensin riippuvuudet komennolla:
> poetry install
 
Ohjelma käynnistyy komennolla:
> poetry run invoke start

##Ohjelma:
 
Ohjelma aukeaa menuvalikkoon, josta pääset peliin tai ohjeisiin valikon nappeja painamalla.
Ohjelman voi sulkea joko ESC-näppäimen avulla tai ohjelmaruudun yläreunassa olevasta x:stä.
Tietokoneesi resoluutiosta riippuen käynnistysruutu ei saata näkyä ohjelmaruudussa kokonaan. Voit säätää ohjelmaruudun kokoa vetämällä ohjelmaruudun reunaa siihen suuntaan, jossa näkymää "katkeaa". 
 

##Pelaaminen:
Tarkoituksenasi on kerätä kolme pelikentällä olevaa huivia.
Ne kerättyäsi sinun tulee loikkia ovelle, joka on nyt auennut.
Aukinaisen oven kohdalla ollessasi pääset pelin läpi, kun painat nuolinäppäintä ylös.
Mikäli osut kentällä liikkuvaan Simon Cowelliin, menetät viimeisimmäksi keräämäsi huivin/huivit ja joudut keräämään ne uudelleen.
 
Pelihahmoa, Harrya, ohjataan oikealla ja vasemmalla nuolinäppäimellä. Hyppääminen onnistuu välilyöntinäppäintä käyttämällä.

Pelin läpäisyn jälkeen voit pelata uudelleen tai palata käynnistysvalikkoon ruudulle ilmaantuvien näppäinten kautta.
