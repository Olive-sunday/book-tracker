import json
from datetime import datetime

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book():
    books = load_books()
    
    author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()
    
    for book in books:
        if book['author'].lower() == author.lower() and book['title'].lower() == title.lower():
            print("Ошибка: такая книга уже есть в списке!")
            return
    
    while True:
        rating = input("Введите оценку (1-5): ").strip()
        if rating.isdigit() and 1 <= int(rating) <= 5:
            rating = int(rating)
            break
        print("Оценка должна быть числом от 1 до 5!")
    
    date_read = input("Введите дату прочтения (YYYY-MM-DD): ").strip()
    
    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read
    }
    
    books.append(book)
    save_books(books)
    print(f"Книга '{title}' добавлена успешно!")

def show_all_books():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    
    print("\n=== Все книги ===")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} — \"{book['title']}\" (оценка: {book['rating']}, дата: {book['date_read']})")
    print()

def show_average_rating():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    
    avg = sum(book['rating'] for book in books) / len(books)
    print(f"\nСредняя оценка: {avg:.2f}\n")

def show_author_stats():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    
    author_count = {}
    for book in books:
        author = book['author']
        author_count[author] = author_count.get(author, 0) + 1
    
    print("\n=== Статистика по авторам ===")
    for author, count in sorted(author_count.items()):
        print(f"{author}: {count} книге(ах)")
    print()

def delete_book():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    
    show_all_books()
    try:
        index = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"Книга '{removed['title']}' удалена.")
        else:
            print("Неверный номер книги.")
    except ValueError:
        print("Введите число.")

def main():
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("Выберите пункт меню (1-6): ").strip()
        
        if choice == '1':
            add_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_stats()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()