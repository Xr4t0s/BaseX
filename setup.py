import os

def create_env_file():
    print("🚀 Configuration of env")

    # Demander à l'utilisateur de remplir les variables
    tg_id = input("🔹 Enter your telegram_id (API ID Telegram) : ").strip()
    tg_hash = input("🔹 Entrer your telegram_hash (API Hash Telegram) : ").strip()
    phone = input("🔹 Enter your phone number (international format) : ").strip()
    broker = input("🔹 Enter the @ of you're SigmaTrading bot : ").strip()
    target = input("🔹 Enter the X target to track (ex: infecteddotfun) : ").strip()

    # Contenu du fichier .env
    env_content = f"""TG_ID={tg_id}
TG_HASH={tg_hash}
PHONE={phone}
BROKER={broker}
TARGET={target}
"""

    # Écriture dans le fichier .env
    with open(".env", "w") as env_file:
        env_file.write(env_content)

    print("\n✅ File `.env` created with success ! 🎉")
    print("⚠️ Be aware to not share what's in the .env file.")

if __name__ == "__main__":
    create_env_file()
