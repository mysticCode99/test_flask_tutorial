CREATE TABLE IF NOT EXISTS main_menu (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    url text NOT NULL
)

CREATE TABLE IF NOT EXISTS irregular_verbs (
    translation TEXT NOT NULL,
    verb1 TEXT NOT NULL PRIMARY KEY,
    verb2 TEXT NOT NULL,
    verb3 TEXT NOT NULL
)