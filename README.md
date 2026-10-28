# Скрипты инициализации баз данных (Задачи 1-10)

В данном репозитории содержатся SQL-скрипты для создания и заполнения демонстрационных баз данных. Данные таблицы используются в качестве структуры для работы Python-скриптов.

## Сводный список баз данных

| Название БД | Тематика таблицы | Основная сортировка в SELECT |
| :--- | :--- | :--- |
| `alkanes_task1` | Алканы (Химия) | По числу углерода (`carbon_count`) |
| `alkenes_task2` | Алкены (Химия) | По числу углерода (`carbon_count`) |
| `alkadienes_task3` | Алкадиены (Химия) | По числу углерода (`carbon_count`) |
| `alkynes_task4` | Алкины (Химия) | По числу углерода (`carbon_count`) |
| `alcohols_task5` | Спирты (Химия) | По числу углерода (`carbon_count`) |
| `books_task6` | Книги и публикации | По году издания и названию |
| `stationery_task7` | Канцтовары (Склад) | По цене и названию |
| `sports_task8` | Спортивные секции | По стоимости и названию |
| `board_games_task9` | Настольные игры | По длительности и названию |
| `computers_task10`| Компьютерная техника | По объему диска и названию |

---

## SQL Скрипты по задачам

### Задачи 1-5: Органическая химия

<details>
<summary>Открыть SQL-код для химических соединений (Алканы, Алкены, Алкадиены, Алкины, Спирты)</summary>

```sql
-- Задача 1: Алканы
CREATE DATABASE alkanes_task1;
CREATE TABLE public.alkanes (
    name VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(20) NOT NULL,
    carbon_count INTEGER NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INTEGER NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INTEGER NOT NULL CHECK (molar_mass > 0)
);
INSERT INTO public.alkanes VALUES 
('Метан', 'CH4', 1, 4, 16),
('Этан', 'C2H6', 2, 6, 30),
('Пропан', 'C3H8', 3, 8, 44),
('Бутан', 'C4H10', 4, 10, 58),
('Пентан', 'C5H12', 5, 12, 72);

SELECT name, formula, carbon_count, hydrogen_count, molar_mass 
FROM public.alkanes 
ORDER BY carbon_count ASC;

-- Задача 2: Алкены
CREATE DATABASE alkenes_task2;
CREATE TABLE public.alkenes (
    name VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(20) NOT NULL,
    carbon_count INTEGER NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INTEGER NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INTEGER NOT NULL CHECK (molar_mass > 0)
);
INSERT INTO public.alkenes VALUES 
('Этен', 'C2H4', 2, 4, 28),
('Пропен', 'C3H6', 3, 6, 42),
('Бут-1-ен', 'C4H8', 4, 8, 56),
('Пент-1-ен', 'C5H10', 5, 10, 70),
('Гекс-1-ен', 'C6H12', 6, 12, 84);

SELECT name, formula, carbon_count, hydrogen_count, molar_mass 
FROM public.alkenes 
ORDER BY carbon_count ASC;

-- Задача 3: Алкадиены
CREATE DATABASE alkadienes_task3;
CREATE TABLE public.alkadienes (
    name VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(20) NOT NULL,
    carbon_count INTEGER NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INTEGER NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INTEGER NOT NULL CHECK (molar_mass > 0)
);
INSERT INTO public.alkadienes VALUES 
('Пропадиен', 'C3H4', 3, 4, 40),
('Бута-1,3-диен', 'C4H6', 4, 6, 54),
('Пента-1,3-диен', 'C5H8', 5, 8, 68),
('Гекса-1,3-диен', 'C6H10', 6, 10, 82),
('Гепта-1,3-диен', 'C7H12', 7, 12, 96);

SELECT name, formula, carbon_count, hydrogen_count, molar_mass 
FROM public.alkadienes 
ORDER BY carbon_count ASC;

-- Задача 4: Алкины
CREATE DATABASE alkynes_task4;
CREATE TABLE public.alkynes (
    name VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(20) NOT NULL,
    carbon_count INTEGER NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INTEGER NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INTEGER NOT NULL CHECK (molar_mass > 0)
);
INSERT INTO public.alkynes VALUES 
('Этин', 'C2H2', 2, 2, 26),
('Пропин', 'C3H4', 3, 4, 40),
('Бут-1-ин', 'C4H6', 4, 6, 54),
('Пент-1-ин', 'C5H8', 5, 8, 68),
('Гекс-1-ин', 'C6H10', 6, 10, 82);

SELECT name, formula, carbon_count, hydrogen_count, molar_mass 
FROM public.alkynes 
ORDER BY carbon_count ASC;

-- Задача 5: Спирты
CREATE DATABASE alcohols_task5;
CREATE TABLE public.alcohols (
    name VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(20) NOT NULL,
    carbon_count INTEGER NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INTEGER NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INTEGER NOT NULL CHECK (molar_mass > 0)
);
INSERT INTO public.alcohols VALUES 
('Метанол', 'CH4O', 1, 4, 32),
('Этанол', 'C2H6O', 2, 6, 46),
('Пропан-1-ол', 'C3H8O', 3, 8, 60),
('Бутан-1-ол', 'C4H10O', 4, 10, 74),
('Пентан-1-ол', 'C5H12O', 5, 12, 88);

SELECT name, formula, carbon_count, hydrogen_count, molar_mass 
FROM public.alcohols 
ORDER BY carbon_count ASC;
```
</details>

---

### Задача 6: Книги (`books_task6`)
```sql
CREATE DATABASE books_task6;
CREATE TABLE public.books (
    title VARCHAR(150) PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    publication_year INTEGER NOT NULL CHECK (publication_year > 0),
    pages INTEGER NOT NULL CHECK (pages > 0),
    copies INTEGER NOT NULL CHECK (copies >= 0)
);
INSERT INTO public.books VALUES 
('Путь к звёздам', 'Анна Мирова', 2018, 180, 3),
('Лесные истории', 'Иван Ветров', 2020, 240, 5),
('Мир роботов', 'Ольга Север', 2021, 320, 2),
('Тайна острова', 'Павел Лисов', 2022, 280, 4),
('Город будущего', 'Мария Луч', 2024, 400, 1);

SELECT title, author, publication_year, pages, copies 
FROM public.books 
ORDER BY publication_year ASC, title ASC;
```

---

### Задача 7: Канцтовары (`stationery_task7`)
```sql
CREATE DATABASE stationery_task7;
CREATE TABLE public.stationery (
    name VARCHAR(100) PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    price INTEGER NOT NULL CHECK (price > 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    reorder_level INTEGER NOT NULL CHECK (reorder_level >= 0)
);
INSERT INTO public.stationery VALUES 
('Тетрадь', 'Бумага', 60, 25, 10),
('Блокнот', 'Бумага', 180, 8, 10),
('Ручка', 'Письмо', 40, 50, 20),
('Маркер', 'Письмо', 120, 5, 10),
('Папка', 'Хранение', 150, 12, 5);

SELECT name, category, price, quantity, reorder_level 
FROM public.stationery 
ORDER BY price ASC, name ASC;
```

---

### Задача 8: Спортивные секции (`sports_task8`)
```sql
CREATE DATABASE sports_task8;
CREATE TABLE public.sports (
    name VARCHAR(100) PRIMARY KEY,
    sport VARCHAR(50) NOT NULL,
    participants INTEGER NOT NULL CHECK (participants > 0),
    sessions INTEGER NOT NULL CHECK (sessions > 0),
    fee INTEGER NOT NULL CHECK (fee > 0)
);
INSERT INTO public.sports VALUES 
('Старт', 'Плавание', 12, 2, 2500),
('Волна', 'Плавание', 16, 3, 3500),
('Темп', 'Бег', 10, 3, 1800),
('Пас', 'Футбол', 20, 2, 2200),
('Ритм', 'Гимнастика', 14, 4, 4000);

SELECT name, sport, participants, sessions, fee 
FROM public.sports 
ORDER BY fee ASC, name ASC;
```

---

### Задача 9: Настольные игры (`board_games_task9`)
```sql
CREATE DATABASE board_games_task9;
CREATE TABLE public.board_games (
    name VARCHAR(100) PRIMARY KEY,
    genre VARCHAR(50) NOT NULL,
    players INTEGER NOT NULL CHECK (players > 0),
    duration INTEGER NOT NULL CHECK (duration > 0),
    min_age INTEGER NOT NULL CHECK (min_age > 0)
);
INSERT INTO public.board_games VALUES 
('Остров', 'Стратегия', 4, 60, 10),
('Маршрут', 'Приключения', 3, 45, 8),
('Слова', 'Викторина', 6, 30, 12),
('Башня', 'Ловкость', 2, 15, 6),
('Космос', 'Стратегия', 5, 90, 14);

SELECT name, genre, players, duration, min_age 
FROM public.board_games 
ORDER BY duration ASC, name ASC;
```

---

### Задача 10: Компьютерная техника (`computers_task10`)
```sql
CREATE DATABASE computers_task10;
CREATE TABLE public.computers (
    name VARCHAR(100) PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    ram_gb INTEGER NOT NULL CHECK (ram_gb > 0),
    storage_gb INTEGER NOT NULL CHECK (storage_gb > 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0)
);
INSERT INTO public.computers VALUES 
('Учебный-1', 'ПК', 8, 256, 12),
('Учебный-2', 'ПК', 16, 512, 8),
('Мобильный-1', 'Ноутбук', 8, 512, 5),
('Мобильный-2', 'Ноутбук', 16, 1024, 3),
('Сервер-1', 'Сервер', 32, 2048, 1);

SELECT name, category, ram_gb, storage_gb, quantity 
FROM public.computers 
ORDER BY storage_gb ASC, name ASC;
```
