import os
import Modules.hash as hash
import Modules.SQLite as DB
import questionary
from dotenv import load_dotenv, set_key, find_dotenv

env = find_dotenv()
load_dotenv()

ADMIN_MDP = os.getenv("ADMIN_MDP")

menu = questionary.select(
    "Menu :",
    choices=[
        "Changer le mot de passe",
        "Actions sur la DB",
    ]).ask()

if menu == "Changer le mot de passe":
    MDP_TEST = hash.hash(questionary.password("Ancien mot de passe >>> ").ask())
    if hash.compare_hash(MDP_TEST, ADMIN_MDP):
        NEW_MDP = hash.hash(questionary.password("Nouveau mot de passe >>> ").ask())
        NEW_MDP_CONFIRM = hash.hash(questionary.password("Confirmez le nouveau mot de passe >>> ").ask())
        if hash.compare_hash(NEW_MDP, NEW_MDP_CONFIRM):
            set_key(env, "ADMIN_MDP", NEW_MDP)
        else:
            print("Les mots de passes ne correspondent pas.")
    else:
        print("Mot de passe incorrect. Le mot de passe par défaut est 'Admin123!'")

elif menu == "Actions sur la DB":
    MDP_TEST = hash.hash(questionary.password("Mot de passe >>> ").ask())
    if hash.compare_hash(MDP_TEST, ADMIN_MDP):
        menu_admin = questionary.select(
            "Menu ADMIN :",
            choices=[
                "Ajouter un utilisateur",
                "Supprimer un utilisateur",
                "Afficher les utilisateurs",
                "Obtenir l'ID d'un utilisateur",
            ]).ask()
            
        if menu_admin == "Ajouter un utilisateur":
            new_username = questionary.text("Nom d'utilisateur >>> ").ask()
            new_email = questionary.text("E-mail >>> ").ask()
            DB.add(new_username, new_email)
        elif menu_admin == "Supprimer un utilisateur":
            menu_supp = questionary.select(
                "Supprimer un utilisateur :",
                choices=[
                    "Par ID",
                    "Par nom d'utilisateur",
                ]).ask()
            if menu_supp == "Par ID":
                ID_supp = questionary.text("ID >>> ").ask()
                confirm_ID_supp = questionary.select(
                    "Voulez-vous vraiment supprimer cet utilisateur ?",
                    choices=[
                        "Oui",
                        "Non",
                    ]).ask()
                if confirm_ID_supp == "Oui":
                    DB.supp_id(ID_supp)
            elif menu_supp == "Par nom d'utilisateur":
                username_supp = questionary.text("Nom d'utilisateur >>> ").ask()
                confirm_username_supp = questionary.select(
                    "Voulez-vous vraiment supprimer cet utilisateur ?",
                    choices=[
                        "Oui",
                        "Non",
                    ]).ask()
                if confirm_username_supp == "Oui":
                    DB.supp_username(username_supp)
        elif menu_admin == "Afficher les utilisateurs":
            DB.aff()
        elif menu_admin == "Obtenir l'ID d'un utilisateur":
            ID_search = questionary.text("Nom d'utilisateur >>> ").ask()
            DB.get_id(ID_search)

