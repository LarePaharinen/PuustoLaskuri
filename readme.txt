#**PuustoLaskuri**

###Python skriptit, joilla laskea [paikkatietoikkuna.fi](https://kartta.paikkatietoikkuna.fi/) karttatasojen avulla kiinteistön puuston määrä.

##Käyttäminen:

    1. Etsi oikea kiinteistö karttapalvelusta, ja lataa kuvat halutuista karttatasoista. Koko kiinteistön olisi hyvä mahtua kerralla kuvaan, mutta laskelma on epätarkempi, jos ala on todella iso. Kiinteistörajat kannattaa näkyä
    
    2. Muokkaa vain oikea kiinteistö näkymään kuvissa. Katso samalla, kuinka monta pikseliä yksi ruudun sivu on. Tietoa tarvitaan myöhemmin.
    
    3. Avaa haluttu tiedosto (oikea karttataso) ja muokkaa muuttujiin oikeat tiedot, eli ruudun sivun pikselien määrä (64, 32, 16, jne...) ja oikea tiedostopolku. Jos ajat full.py, niin kannattaa nimetä karttatasot vastaavasti, ja antaa vain kansion polku, missä kuvat ovat. Kuvien nimeäminen ja tuetut karttatasot:
    
        +Tilavuus, koivu kuitupuu 2017 - "koivuKuitu"
        +Tilavuus, koivu tukkipuu 2017 - "koivuTukki"
        +Tilavuus, kuusi kuitupuu 2017 - "kuusiKuitu"
        +Tilavuus, kuusi tukkipuu 2017 - "kuusiTukki"
        +Tilavuus, mänty kuitupuu 2017 - "mäntyKuitu"
        +Tilavuus, mänty tukkipuu 2017 - "mäntyTukki"
        +Tilavuus, puusto yhteensä 2017 - "puustoYht"
        
    Toimii .png kuvilla.
       
    4.
    
##TODO:
    -Mahdollistaa full.py ajaminen, ilman että kaikkia seitsemää kuvaa ladattu (perus errorhandling muutenkin)
    -Eri kuva formaattien tutkiminen




