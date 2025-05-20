DANIELS NOVIKOVS 241EDB142 2.GRUPA


Šī projekta mērķis ir izveidot PVN kalkulatoru, kas ļauj lietotājam:

1)Pievienot preces ar to cenām (bez PVN)
2)Automātiski aprēėināt PVN summu (21% no cenas)
3)Aprēėināt kopējo cenu ar PVN
4)Apskatīt visu pievienoto preču sarakstu
5)Dzēst preces no saraksta
6)Saglabāt un lasīt datus no CSV faila

Programma darbojas caur komandas interfeisu, kur lietotājs var ievadīt komandas ("add", "delete", "list", "exit").

Izmantotās Python Bibliotēkas un To Lietojums

csv - Izmantota darbam ar CSV failiem - datu saglabāšanai un lasīšanai no faila, ļauj strukturēti glabāt preču datus (nosaukums, cena bez PVN, PVN summa, kopējā cena)
os - Izmantota failu sistēmas operācijām - pārbaudīt, vai eksistē datu fails pirms lasīšanas/dzēšanas un pārbaudīt, vai fails ir tukšs pirms header ierakstīšanas



Projekta kods galvenokārt izmanto Python vārdnīcas, kā datu struktūru:

Katra prece tiek glabāta kā vārdnīca ar atslēgām:
'Prece' - preces nosaukums
'Bez PVN' - cena bez PVN
'PVN' - aprēėinātā PVN summa
'Kopa' - kopējā cena ar PVN


Darbības ar šīm struktūrām:
ADD (Pievienošana): Izveido jaunu vārdu un pievieno to CSV failam
DELETE (Dzēšana): Nolasa visas preces atmiņā kā vārdu sarakstu, filtrē ārā dzēšamo preci, pēc tam pārraksta visu failu
LIST (Parādīšana): Nolasa visas preces no faila un formatē to izvadei
EXIT (Pabeigšana): Pabeidz programmu un saglabā csv failu


Programmatūras Izmantošanas Metodes

Interaktīvais režīms:

Lietotājs ievada komandas teksta formātā
Programma interpretē komandas un izpilda atbilstošās darbības
Katras komandas rezultāts tiek parādīts uzreiz

Datu glabāšana:

Visi dati tiek saglabāti CSV failā (preces (4).csv)
Datu formāts: Prece;Bez PVN;PVN;Kopa (ar semikolu kā atdalītāju)
Faila struktūra tiek automātiski izveidota pie pirmās preces pievienošanas

Kļūdu apstrāde:
Pārbauda ievades pareizību (piemēram, cena jābūt skaitlim)
Pārbauda, vai fails eksistē pirms operācijām
Pārbauda, vai dzēšamā prece eksistē

Lietošanas instrukcijas:

Programma sākumā izdrukā visu pieejamo komandu sarakstu

Komandu sintakse:

add <preces nosaukums>
delete <preces nosaukums>
list
exit
