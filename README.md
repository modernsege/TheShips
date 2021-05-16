# TheShips
## TWÓRCY PROJKETU
Szymon Cygan Informatyka Techniczna, gr. proj. 1
Maciej Leśniak Informatyka Techniczna, gr. proj. 2

### IDEA PROJEKTU
Ideą projektu jest stworzenie bazy danych do gry, którą planujemy napisać. Gra ma być zmodyfikowaną i komputerową wersją tradycyjnej gry w statki (na kartkach papieru). 
Główna mechanika gry będzie działać w opisany poniżej sposób.

Na początku ustawiane będą ogólne parametrey rozgrywki (takie jak wielkość planszy czy częstotliwość występowania na mapie przeszkód).
Następnie gracze będą mieli możliwość wybrania frakcji, którą będą reprezentować w danym meczu. Będzie to znacząco wpływać na rozgrywkę. Każda frakcja będzie zapewniać określoną ilość waluty w grze (której znaczenie będzie opisane później) jak i specjalne umiejętności (zarówno aktywne jak i pasywne).
Później grający dostaną możliwość wykorzystania waluty “zapewnionej im przez frakcje”. Dokładniej - pojawi się okienko sklepu. Tutaj rywale będą mogli kupić przedmioty jednorazowego użytku i ulepszenia statków, które pomogą im wygrać.
Kolejną rzeczą będzie wygenerowanie map dla obydwu graczy, które będą zależne od poprzednich ustawień lub/i decyzji.
Dalej gracze dostaną możliwość ustawienia swoich statków na swojej planszy (ich ilość i wielkość będzie zależna od poprzednich faz).
Następnie rozpocznie się najważniejszy element gry - walka. Celem obydwu graczy będzie zatopienie wszystkich statków przeciwnika, zanim on to zrobi. Każdy z graczy będzie widział 2 plansze (swoją-odkrytą i przeciwnika-zasłoniętą), interfers umiejętności i oś rudny z zaznaczonymi turami. Bitwa będzie podzielona na rundy i tury. 
Runda będzie składać się z tylu tur ile będzie niezatopionych statków. 
Tura będzie symbolizować działanie jednego statku, więc po wykonaniu jednej akcji (będzie ona opisana trochę dalej) tura kończy się i rozpoczyna się tura następnego statku (obecnie tury statków będą przyznawane graczom na zmianę, ale rozważamy uzależnienie tego od jakiegoś parametru, na który będzie mogła wpływać umiejętność jakiejś frakcji lub sklepu). 
Akcja to wykonanie jednej z czynności:
- użycie przedmiotu ze sklepu,
- użycie umiejętności frakcji,
- oddanie strzału.


Po zatopieniu wszystkich statków jednego z graczy wyświetli się ekran końcowy.
