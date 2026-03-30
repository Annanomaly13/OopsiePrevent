import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

HISTORY_FILE = "history.json"

# ---------- History Handling ----------
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {"sources": [], "destinations": []}

def save_history():
    data = {
        "sources": list(source_combo["values"]),
        "destinations": list(dest_combo["values"])
    }
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_to_history(combo, value):
    values = list(combo["values"])
    if value and value not in values:
        values.append(value)
        combo["values"] = values

# ---------- Folder Selection ----------
def select_source():
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)
        add_to_history(source_combo, folder)

def select_destination():
    folder = filedialog.askdirectory()
    if folder:
        dest_var.set(folder)
        add_to_history(dest_combo, folder)

# ---------- Backup Logic ----------
def backup():
    source = source_var.get()
    dest = dest_var.get()

    if not source or not dest:
        messagebox.showerror("Error", "Please select both folders.")
        return

    copied_files = 0

    for root_dir, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root_dir, source)
        dest_path = os.path.join(dest, rel_path)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        for file in files:
            src_file = os.path.join(root_dir, file)
            dest_file = os.path.join(dest_path, file)

            # Copy new or updated files
            if (not os.path.exists(dest_file) or
                os.path.getmtime(src_file) > os.path.getmtime(dest_file)):
                
                shutil.copy2(src_file, dest_file)
                copied_files += 1

    save_history()

    messagebox.showinfo("Done", f"Backup complete!\n{copied_files} files copied/updated.")

# ---------- GUI ----------
root = tk.Tk()
root.title("Backup Tool")
root.geometry("500x250")

history = load_history()

source_var = tk.StringVar()
dest_var = tk.StringVar()

# Source
tk.Label(root, text="Source Folder").pack(pady=5)
source_combo = ttk.Combobox(root, textvariable=source_var, width=60)
source_combo["values"] = history["sources"]
source_combo.pack()
tk.Button(root, text="Browse", command=select_source).pack(pady=5)

# Destination
tk.Label(root, text="Destination Folder").pack(pady=5)
dest_combo = ttk.Combobox(root, textvariable=dest_var, width=60)
dest_combo["values"] = history["destinations"]
dest_combo.pack()
tk.Button(root, text="Browse", command=select_destination).pack(pady=5)

# Start Button
tk.Button(root, text="Start Backup", command=backup, bg="green", fg="white").pack(pady=20)

root.mainloop()
