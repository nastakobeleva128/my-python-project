import csv
import random
import xml.etree.ElementTree as ET


def process_books_csv():
    title_30 = 0
    all_books = []
    unique_publishers = set()
    
    with open("books-en.csv", "r", encoding="windows-1252") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)  
        
        for row in reader:
            if len(row) < 7:
                continue
                
            title = row[1]
            author = row[2]
            year_str = row[3]
            publisher = row[4]    
            downloads_str = row[5]  
            
            if len(title) > 30:
                title_30 += 1
                
            unique_publishers.add(publisher)
            
            try:
                year = int(year_str)
                downloads = int(downloads_str)
            except ValueError:
                year = 0
                downloads = 0

            all_books.append({
                "title": title,
                "author": author,
                "year": year,
                "publisher": publisher,
                "downloads": downloads
            })
            
    #1 задание
    print(title_30)
    print()

    #2 задание
    search_author = input().strip()
    for book in all_books:
        if search_author.lower() in book["author"].lower() and 1991 <= book["year"] <= 1995:
            print(f"{book['title']} ({book['year']})")
    print()   

    #3 задание
    random_books = random.sample(all_books, 20)
    with open("links.txt", "w", encoding="utf-8") as out_file:
        for idx, book in enumerate(random_books, 1):
            out_file.write(f"{idx}. {book['author']}. {book['title']} - {book['year']}\n")
    print()

    #допзадание 1
    sorted_publishers = sorted(list(unique_publishers))
    for p in sorted_publishers[:10]:
        print(p)
    print()

    #допзадание 2
    sorted_by_popularity = sorted(all_books, key=lambda x: x["downloads"], reverse=True)
    for idx, book in enumerate(sorted_by_popularity[:20], 1):
        print(f"{idx}. {book['title']}, {book['author']}, {book['year']} (Скачиваний: {book['downloads']})")
    print()

#работа с валютами
def parse_currency_xml():
    tree = ET.parse("currency.xml")
    root = tree.getroot()
    
    for valute in root.findall("Valute"):
        nominal = int(valute.find("Nominal").text)
        char_code = valute.find("CharCode").text
        
        if nominal == 10 or nominal == 100:
            print(char_code)


if __name__ == "__main__":
    process_books_csv()
    parse_currency_xml()

