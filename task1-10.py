import tkinter as tk
from tkinter import ttk
import psycopg

DB_NAME = "eriskin_23is"
DB_USER = "postgres"
DB_PASS = "1111"
DB_HOST = "localhost"
DB_PORT = "5432"

TASKS_CONFIG = [
    {
        "title": "Каталог: Алканы",
        "headers": ["Название", "Формула", "Атомов C", "Атомов H", "Масса, г/моль"],
        "query": "SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alkanes ORDER BY carbon_count ASC;"
    },
    {
        "title": "Каталог: Алкены",
        "headers": ["Название", "Формула", "Атомов C", "Атомов H", "Масса, г/моль"],
        "query": "SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alkenes ORDER BY carbon_count ASC;"
    },
    {
        "title": "Каталог: Алкадиены",
        "headers": ["Название", "Формула", "Атомов C", "Атомов H", "Масса, г/моль"],
        "query": "SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alkadienes ORDER BY carbon_count ASC;"
    },
    {
        "title": "Каталог: Алкины",
        "headers": ["Название", "Формула", "Атомов C", "Атомов H", "Масса, г/моль"],
        "query": "SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alkynes ORDER BY carbon_count ASC;"
    },
    {
        "title": "Каталог: Спирты",
        "headers": ["Название", "Формула", "Атомов C", "Атомов H", "Масса, г/моль"],
        "query": "SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alcohols ORDER BY carbon_count ASC;"
    },
    {
        "title": "Каталог: Библиотека",
        "headers": ["Название", "Автор", "Год", "Страниц", "Экземпляров"],
        "query": "SELECT title, author, publication_year, pages, copies FROM public.books ORDER BY publication_year ASC, title ASC;"
    },
    {
        "title": "Каталог: Магазин канцтоваров",
        "headers": ["Товар", "Категория", "Цена, руб.", "Остаток", "Порог заказа"],
        "query": "SELECT name, category, price, quantity, reorder_level FROM public.stationery ORDER BY price ASC, name ASC;"
    },
    {
        "title": "Каталог: Спортивные секции",
        "headers": ["Секция", "Вид спорта", "Участников", "Занятий/нед.", "Цена/мес., руб."],
        "query": "SELECT name, sport, participants, sessions, fee FROM public.sports ORDER BY fee ASC, name ASC;"
    },
    {
        "title": "Каталог: Настольные игры",
        "headers": ["Игра", "Жанр", "Игроков", "Минут", "Возраст, от"],
        "query": "SELECT name, genre, players, duration, min_age FROM public.board_games ORDER BY duration ASC, name ASC;"
    },
    {
        "title": "Каталог: Компьютерное оборудование",
        "headers": ["Модель", "Тип", "ОЗУ, ГБ", "Накопитель, ГБ", "Количество"],
        "query": "SELECT name, category, ram_gb, storage_gb, quantity FROM public.computers ORDER BY storage_gb ASC, name ASC;"
    }
]

current_index = 0
COLUMNS = ("c1", "c2", "c3", "c4", "c5")
DB_CONFIG = f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST} port={DB_PORT}"


def clear_treeview():
    for item in tree.get_children():
        tree.delete(item)


def get_data():
    clear_treeview()
    cfg = TASKS_CONFIG[current_index]
    try:
        with psycopg.connect(DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(cfg["query"])
                rows = cur.fetchall()
                for row in rows:
                    v1, v2, v3, v4, v5 = row
                    tree.insert("", "end", values=(v1, v2, v3, v4, v5))
    except Exception as e:
        tree.insert("", "end", values=(f"Таблица не найдена в {DB_NAME}", "", "", "", ""))
        print(f"Ошибка: {e}")


def update_ui():
    clear_treeview()
    cfg = TASKS_CONFIG[current_index]
    lbl_title.config(text=cfg["title"])
    root.title(f"{cfg['title']} — Навигатор (Работа {current_index + 1}/10)")
    for col_id, text in zip(COLUMNS, cfg["headers"]):
        tree.heading(col_id, text=text)


def next_task():
    global current_index
    if current_index < len(TASKS_CONFIG) - 1:
        current_index += 1
        update_ui()


def prev_task():
    global current_index
    if current_index > 0:
        current_index -= 1
        update_ui()


def create_app():
    global root, lbl_title, tree
    root = tk.Tk()
    root.geometry("620x350")

    lbl_title = tk.Label(root, text="", font=("Arial", 11))
    lbl_title.pack(pady=(15, 10))


    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=(0, 15))

    btn_show = tk.Button(btn_frame, text="Показать", width=15, command=get_data)
    btn_show.pack(side=tk.LEFT, padx=5)

    btn_clear = tk.Button(btn_frame, text="Очистить таблицу", width=15, command=clear_treeview)
    btn_clear.pack(side=tk.LEFT, padx=5)

    # Контейнер для таблицы и скроллбара
    table_frame = tk.Frame(root)
    table_frame.pack(fill=tk.X, padx=15, expand=False)

    tree = ttk.Treeview(table_frame, columns=COLUMNS, show="headings", height=3)

    scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    for col in COLUMNS:
        tree.column(col, width=115, anchor=tk.W)

    tree.pack(side=tk.LEFT, fill=tk.X, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    root.bind("<Left>", lambda event: prev_task())
    root.bind("<Right>", lambda event: next_task())

    update_ui()
    root.mainloop()


if __name__ == "__main__":
    create_app()
