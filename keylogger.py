import tkinter as tk
import json

root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger Page")
root.configure(bg="lightgray")

key_list = []
key_strokes = ""
x = False

def update_txt_file(key):
    with open("logs.txt", "w", encoding="utf-8") as key_stroke:
        key_stroke.write(key)

def update_json_file(data):
    with open("logs.json", "w", encoding="utf-8") as key_log:
        json.dump(data, key_log, indent=4)

def on_press(event):
    global x, key_list

    if not x:
        key_list.append({"Pressed": event.keysym})
        x = True
    else:
        key_list.append({"Held": event.keysym})

    update_json_file(key_list)

def on_release(event):
    global x, key_list, key_strokes

    key_list.append({"Released": event.keysym})
    x = False
    update_json_file(key_list)

    key_strokes += event.keysym + " "
    update_txt_file(key_strokes)

def butaction():
    print("[+] Running Keylogger successfully!")
    print("[!] Saving the key logs in 'logs.json'")

    text_area.focus_set()

label_title = tk.Label(root, text="Keylogger Project",
                       bg="lightgray", font=("Verdana", 11, "bold"))
label_title.pack(pady=10)

text_area = tk.Text(root, height=8, width=25)
text_area.pack()
text_area.bind("<KeyPress>", on_press)
text_area.bind("<KeyRelease>", on_release)

btn = tk.Button(root, text="Start Keylogger", command=butaction)
btn.pack(pady=10)

root.mainloop()
