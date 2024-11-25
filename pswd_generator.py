import random
import string
import hashlib

def generate_password(length=16):
    """Génère un mot de passe sécurisé aléatoire."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    """Hache le mot de passe avec SHA-256."""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def show_info(language):
    """Affiche des informations sur le programme."""
    if language == "fr":
        print("\n=== Informations sur le programme ===")
        print("Ce programme génère des mots de passe sécurisés aléatoires et les crypte à l'aide de SHA-256.")
        print("Options disponibles :")
        print("1. Générer un mot de passe aléatoire.")
        print("2. Afficher des informations sur le programme.")
        print("3. Quitter le programme.")
        print("=====================================\n")
    else:
        print("\n=== Program Information ===")
        print("This program generates secure random passwords and encrypts them using SHA-256.")
        print("Available options:")
        print("1. Generate a random password.")
        print("2. Show program information.")
        print("3. Exit the program.")
        print("=====================================\n")

def main():
    print("=== Welcome to the Secure Password Generator ===")
    print("=== Bienvenue dans le générateur de mots de passe sécurisé ===")
    
    language = input("Choose your language (English: 'en', Français: 'fr') : ").strip().lower()
    if language not in ["en", "fr"]:
        print("Invalid choice. Defaulting to English.")
        language = "en"

    while True:
        if language == "fr":
            print("\n--- Menu ---")
            print("1. Générer un mot de passe sécurisé.")
            print("2. Afficher des informations sur le programme.")
            print("3. Quitter.")
            choice = input("Entrez votre choix (1-3) : ")
        else:
            print("\n--- Menu ---")
            print("1. Generate a secure password.")
            print("2. Show program information.")
            print("3. Exit.")
            choice = input("Enter your choice (1-3) : ")

        if choice == '1':
            try:
                if language == "fr":
                    length = int(input("Entrez la longueur du mot de passe (par défaut 16) : ") or 16)
                    password = generate_password(length)
                    hashed_password = hash_password(password)
                    print(f"\nMot de passe généré : {password}")
                    print(f"Mot de passe crypté (SHA-256) : {hashed_password}")
                else:
                    length = int(input("Enter the password length (default 16) : ") or 16)
                    password = generate_password(length)
                    hashed_password = hash_password(password)
                    print(f"\nGenerated password : {password}")
                    print(f"Encrypted password (SHA-256) : {hashed_password}")
            except ValueError:
                if language == "fr":
                    print("Erreur : Veuillez entrer un nombre valide.")
                else:
                    print("Error: Please enter a valid number.")
        elif choice == '2':
            show_info(language)
        elif choice == '3':
            if language == "fr":
                print("Merci d'avoir utilisé le programme. À bientôt !")
            else:
                print("Thank you for using the program. See you soon!")
            break
        else:
            if language == "fr":
                print("Option invalide. Veuillez réessayer.")
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
