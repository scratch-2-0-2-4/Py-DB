import sqlite3

conn = sqlite3.connect("DB.db")
cursor = conn.cursor()


def add(username, email):
    cursor.execute(
        """
        INSERT INTO utilisateurs (username, email)
        VALUES (?, ?)
    """,
        (username, email),
    )
    conn.commit()


def supp_id(user_id):
    cursor.execute("DELETE FROM utilisateurs WHERE id = ?", (user_id,))
    conn.commit()


def supp_username(username):
    cursor.execute("DELETE FROM utilisateurs WHERE username = ?", (username,))
    conn.commit()


def aff():
    cursor.execute("SELECT * FROM utilisateurs")
    membres = cursor.fetchall()
    print("\n--- Liste des utilisateurs ---")
    for membre in membres:
        print(f"ID: {membre[0]} | Username: {membre[1]} | Email: {membre[2]}")
    print("------------------------------\n")


def get_id(username):
    cursor.execute("SELECT id FROM utilisateurs WHERE username = ?", (username,))
    resultat = cursor.fetchone()

    if resultat:
        print(f"L'ID de {username} est : {resultat[0]}")
        return resultat[0]
    else:
        print(f"Aucun utilisateur trouvé avec l'username : {username}")
        return None