
-- Создание таблиц
--------------------------------------
CREATE TABLE surnames (
    id SERIAL PRIMARY KEY,
    surname VARCHAR(50)
);

CREATE TABLE names (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE patronymics (
    id SERIAL PRIMARY KEY,
    patronymic VARCHAR(50)
);

-- Наполнение таблиц данными
--------------------------------------
INSERT INTO surnames (surname) VALUES ('Иванов'), ('Петров'), ('Сидоров');
INSERT INTO names (name) VALUES ('Иван'), ('Петр'), ('Сидор');
INSERT INTO patronymics (patronymic) VALUES ('Иванович'), ('Петрович'), ('Сидорович');

-- Запрос на выборку
--------------------------------------   
SELECT 
    s.surname || ' ' || n.name || ' ' || p.patronymic AS full_name
FROM 
    surnames s
JOIN 
    names n ON s.id = n.id
JOIN 
    patronymics p ON s.id = p.id
ORDER BY 
    s.surname DESC;
