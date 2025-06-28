# 🔐 Secure Password Generator Using Python 

## 📌 Project Overview
This project is a **Secure Password Generator** built with Python. It allows users to generate strong, randomized passwords based on customizable preferences, including the choice of uppercase letters, lowercase letters, numbers, and special symbols. It also includes features like bulk password generation, password strength checks, clipboard copying, and the ability to save passwords to a file for future use.

The tool helps enhance online security by avoiding weak or predictable passwords and is designed for both beginners and advanced users who prioritize cybersecurity.

---

## ⏳ Duration Time Taken to Complete the Project
The project was completed within **5 to 6 hours**, including:
- Planning the features
- Writing the core logic
- Testing different scenarios
- Adding enhancements like clipboard functionality and file export
- Writing documentation (README), 

---

## 🎯 Outcome
- A fully functional **command-line-based Secure Password Generator**.
- Supports:
  - Custom password lengths
  - Optional inclusion of uppercase, lowercase, numbers, and symbols
  - Batch password generation
  - Clipboard support (last password copied automatically)
  - Save generated passwords to a `.txt` file
- Easy to use, lightweight, and highly customizable.

---

## 🚧 Challenges Faced
- Ensuring the generated passwords always include at least one character from each selected type (uppercase, lowercase, digits, symbols).
- Handling edge cases where users might disable all character types.
- Balancing password strength while maintaining readability (avoiding ambiguous characters if needed).
- Adding clipboard support with `pyperclip` and ensuring compatibility across systems.
- Creating a user-friendly and clean command-line interface with clear prompts.

---

## 🚀 How to Run

### ✅ Prerequisites:
- Python 3 installed on your machine.
- Install the required package for clipboard functionality:
```bash
python -m venv venv # To Create Enviornment Variable
venv\Scripts\Activate # To Activate
Python pass.py # Run The Code
```
---

## ✅ Conclusion
This Secure Password Generator is a simple yet powerful tool to help users create robust passwords tailored to their needs. It enhances security practices by avoiding common and weak passwords. This project not only strengthened Python skills in string manipulation, user input handling, and file operations but also emphasized the importance of security in digital tools.
