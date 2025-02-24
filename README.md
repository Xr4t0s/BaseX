# BaseX

A Python bot that **scrapes X** to detect **Ethereum contract addresses** and automatically sends the information to **Telegram**.

---

## **📌 Features**
👉 Scrapes X to detect ETH addresses (`0x...`)
👉 Automatically sends detected contracts to Telegram
👉 Easy configuration using a **`.env` file**
👉 Uses **Telethon** to work with **your own Telegram account**

---

## **📌 Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/Xr4t0s/BaseX.git
cd BaseX
```

### **2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Generate the `.env` file**
Run the setup script:
```bash
python setup.py
```
Enter your details when prompted.

---

## **📌 How to get your Telegram API keys?**

### **1️⃣ Create a Telegram application**
1. Go to 👉 [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your phone number
3. Click **"Create Application"**
4. Fill in the required details
5. Take note of the following values:
   - **API ID** (`TG_ID`)
   - **API HASH** (`TG_HASH`)

### **2️⃣ Get your phone number and target contact**
- `PHONE` : Your phone number **with country code** (e.g., `+33612345678`)
- `TARGET` : The **username** of the person you are traking (e.g., `username`)
- `CONTACT` : The **contact** @ you want to send the message (ex: `SigmaTrading_Bot`)
---

## **📌 Run the bot**
```bash
python main.py
```
The bot will check Twitter **every 60 seconds** and send new contracts to Telegram. 🎯

---

## **📌 Example Telegram Messages**
💬 Example of an alert sent to Telegram:
```
🚀 New contract detected!
📌 Address: 0x1234567890abcdef1234567890abcdef12345678
```
---

## **📌 Future Improvements**
🚀 Contract analysis before sending  
🚀 Detection of high-potential contracts  
🚀 Integration with other platforms (Discord, Telegram Groups)  

---

### **📌 Contributions**
Want to improve the project?  
**Fork, PR, and suggestions are welcome!** 🔥

📩 Contact: [@xKr4t0s](https://t.me/xKr4t0s)

---

🚀 **Now, run the bot and start sniping!** 🔥

