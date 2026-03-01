# 🚀 NextPass
**The Privacy-Centric AI Password Dictionary Generator.**

Next Pass is a specialized password dictionary generator that uses both the rule-based logic and Large Language Models to generate passwords. Designed for security researchers, it offers offline generation to generate a password dictionary on the go and also leverages AI to predict human-like password patterns while maintaining a strict privacy air-gap for target data.

---
![Screenshot](https://i.ibb.co/x83Vh5Lh/Screenshot-2026-03-01-194741.png)
---
## 🛡️ Privacy-First AI Architecture
Most AI tools leak sensitive target data (Names, Birthdays, Hobbies) by sending them directly to an LLM. **Next Pass** solves this by:
* **Local Data Processing:** Raw target information is processed locally to protect sensitive datas."
* **Abstract Prompting:** The AI receives structural patterns and linguistic archetypes rather than real-world Identifiable Information (PII).

---

## ✨ Features
* **Offline Generation:** Generates most probable human like password used by target ( generated using pre-defined rules )
* **Pure Python Core:** Built entirely with native Python logic (no `itertools` or external modules for the core engine), demonstrating high-efficiency manual iteration.
* **AI Mode:** Leverage the power of AI to go beyond the pre-defined rules and generate more varieties of passowrds
* **Clean Exports:** Outputs dictionaries in `.txt` format, optimized for tools like Hashcat and John the Ripper.

---

## ⚙ Pre-Requisites:-
* Python 3
* Gemini API Key ( Required for AI Mode )
  
---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/0xblarky/NextPass.git
cd Next-Pass
```

### 2. Install requiremenets
```bash
pip install -r requirements.txt
```

### 3. AI mode setup
* Create a new file named .env
* Inside .env, copy paste ```API_KEY={YOUR_API_KEY}```
 
### 4. Running the tool
Put the necessary details in Normal.json if using Normal mode (New key fields cannot be entered)
Put More than 2 details in AI.json if using AI mode (Can enter any data in key value pair)

Note:- You can add multiple datas in a field (Only some fields can have multiple data in Normal mode while any fields can have multiple data in AI mode)

After setting up the json files, Run the command below

Linux:-
```bash
python3 main.py
```
Windows:-
```bash
python main.py
```

After generation, Output text file can be found in the Output folder
