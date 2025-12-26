# Keystroke Logging Demonstration (Educational Project)

This project demonstrates the basic concept of keystroke logging in a **controlled and ethical environment** using Python and Tkinter.
It records only the keystrokes typed inside the application window for learning purposes.

---

## Project Objective

The aim of this project is to help students understand:

* How keystroke logging works
* How sensitive information can be captured
* Why keyloggers are considered a serious cybersecurity threat
* The importance of detection and prevention mechanisms

---

## Features

* Simple graphical interface using Tkinter
* Captures key press and key release events inside the app window
* Saves keystroke data in:

  * `logs.txt` (plain text)
  * `logs.json` (structured format)

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* JSON (Data storage)

---

## How to Run

```bash
python3 keylogger.py
```

---

## How It Works

1. Open the application.
2. Click on the text box and start typing.
3. Click **Start Keylogger**.
4. Your keystrokes will be saved automatically in:

   * `logs.txt`
   * `logs.json`

---

## Output Files

| File Name | Description                                         |
| --------- | --------------------------------------------------- |
| logs.txt  | Stores all captured keystrokes                      |
| logs.json | Stores detailed key press, hold, and release events |

---

## Important Note

This project is strictly for **educational purposes only**.
It does **not** record system-wide keystrokes and should never be used for malicious activity.

---

## Author

**Sabarna Barik**
Cybersecurity Demonstration Project
