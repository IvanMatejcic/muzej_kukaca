# Muzej Kukaca

## Opis projekta
"Muzej Kukaca" Je Django projekt kreiran kao završni rad iz kolegija "Programiranje za Web".
Svrha aplikacije je prikazivanje, dodavanje i uređivanje raznoraznih kukaca od strane korisnika koji ima mogućnost prijave i odjave.

## Detalji
Projekt je kreiran pomoću jednog modela, *Kukac*.
Klasa sadrži podatke o pojedinom kukcu: vrsta, red, lokalitet, datum dodavanja, duljina, spol, opis i lovac kukca.
Korisnik ima mogućnost prijave. Ovo je ostvareno pomoću built-in USER_AUTH_MODEL modela untar Django-a.
Korisnik koji nije ulogiran ima mogućnost pregledavanja kukaca i prijave.
Korisnik koji je ulogiran ima mogućnost pregledavanja, dodavanja, uređivanja i brisanja kukaca.
