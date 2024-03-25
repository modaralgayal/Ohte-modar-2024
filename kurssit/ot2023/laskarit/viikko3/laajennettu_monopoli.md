```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Monopolipeli "1" -- "1" Sattumaruutu
    Monopolipeli "1" -- "1" Yhteismaaruutu
    Monopolipeli "1" -- "1" Kadut
    Monopolipeli "1" -- "1" Pelaajat
    Aloitusruutu "1" -- "1" Ruutu
    Vankila "1" -- "1" Ruutu
    Sattumaruutu "1" -- "1" Ruutu
    Yhteismaaruutu "1" -- "1" Ruutu
    Kadut "1" -- "40" KadunRuutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    class Aloitusruutu{
        - sijainti
    }
    class Vankila{
        - sijainti
    }
    class Sattumaruutu{
        - sijainti
        - kortit
    }
    class Yhteismaaruutu{
        - sijainti
        - kortit
    }
    class Kadut{
        - kadut
    }
    class KadunRuutu{
        - kadunnimi
        - hinta
        - talot
        - hotelli
        - omistaja
    }
```