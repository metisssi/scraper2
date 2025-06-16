# Projekt 3 — Parsování volebních výsledků (Výsledky voleb ČR 2017)

Autor: Andriy Simchera  
Email: simcheraandrij@gmail.com

---

## Popis projektu

Tento projekt stahuje a zpracovává výsledky voleb z webu [volby.cz](https://volby.cz).  
 python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"  projestov.csv nebo python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" benesov.csv
Na základě zadané URL adresy okresu stáhne data o jednotlivých obcích, získá podrobné výsledky hlasování a uloží je do CSV souboru s korektní českou diakritikou.

Projekt využívá vlastní parser napsaný v Pythonu, který kombinuje knihovny `requests` a `BeautifulSoup` pro stahování a analýzu HTML stránek.

---

## Použité technologie a knihovny

- **Python 3.7 a novější**  
- `requests` — stahování webových stránek  
- `beautifulsoup4` — parsování HTML obsahu  
- `csv` — práce se soubory CSV  
- (doporučeno) `pandas` — pro pohodlnou práci s daty a případný export do Excelu  
- (doporučeno) `openpyxl` — podpora Excel souborů (pokud by se chtěl exportovat do XLSX)

---

## Instalace závislostí

Doporučuji vytvořit virtuální prostředí a nainstalovat potřebné balíčky pomocí:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install requests beautifulsoup4 pandas openpyxl
