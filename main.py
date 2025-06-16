import sys
import csv
from myparser import get_html, parse_main_page, parse_detail_page

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <URL> <output_filename.csv>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    main_html = get_html(url)
    municipalities = parse_main_page(main_html, url)

    if not municipalities:
        print("No municipalities found.")
        sys.exit(1)

    headers = ["Kód", "Obec", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]

    all_parties = set()
    data_rows = []

    for m in municipalities:
        detail_html = get_html(m["link"])
        voters, envelopes, valid, parties = parse_detail_page(detail_html)
        all_parties.update(parties.keys())

        row = {
            "Kód": m["code"],
            "Obec": m["name"],
            "Voliči v seznamu": voters,
            "Vydané obálky": envelopes,
            "Platné hlasy": valid,
            **parties
        }
        data_rows.append(row)

    sorted_parties = sorted(all_parties)
    headers.extend(sorted_parties)

    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')  # <-- здесь добавлен delimiter=';'
        writer.writeheader()
        for row in data_rows:
            writer.writerow(row)

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
