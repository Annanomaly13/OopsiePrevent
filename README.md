# 🛡️ OopsiePrevent

A simple local backup tool to protect your files from accidental deletion.

---

## 📖 Overview

**OopsiePrevent** was created after accidentally deleting a large collection of photo mode content from a game during a reinstall.

While backing up files locally is easy in theory, the small amount of friction involved often leads to it not getting done. This tool removes that friction by making backups quick and effortless.

---

## ⚙️ Features

- 📁 Select a **source folder** and **destination folder**
- 💾 One-click backup
- 🔁 **Incremental copying** (only new or updated files are copied)
- 🧠 Remembers previously used folders (history dropdowns)
- ⚡ Lightweight and fast (built with Python + Tkinter)

---

## 🚀 How It Works

1. Choose your **source folder**
2. Choose your **backup destination**
3. Click **Start Backup**

That’s it — the app will:
- Copy all files on first run
- Only copy **new or changed files** on future runs

---

## 🖥️ Running the App

### Option 1: Command Line

```bash
python your_script.py
```
### Option 2: Run as a Windows App (No Console Window)

1. Create a shortcut to your `.py` file  
2. Right-click → **Properties**  
3. In the **Target** field, prepend:

pythonw.exe

**Example:**

pythonw.exe "C:\path\to\your_script.py"

This runs the app without opening a terminal window.

---

## But Why?

Sometimes the hardest part of backing things up isn't the complexity, it's the *inconvenience*.

OopsiePrevent is designed to remove that barrier so you actually **follow through before an “oopsie” happens**.
