import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from deep_translator import GoogleTranslator
import arabic_reshaper
from bidi.algorithm import get_display

def perform_translation():
    text_to_translate = input_box.get("1.0", tk.END).strip()
    target_lang = lang_selection.get().lower()
    
    if not text_to_translate:
        return

    try:
        
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
        
        
        if target_lang == 'arabic':
            reshaped_text = arabic_reshaper.reshape(translated)
            final_text = get_display(reshaped_text)
        else:
            final_text = translated

        
        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, final_text)
        output_box.config(state='disabled')
            
    except Exception as e:
        messagebox.showerror("Error", "Check your internet connection!")

def copy_to_clipboard():
    text = output_box.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Success", "Translation copied!")


root = tk.Tk()
root.title("Mini Translator App")
root.geometry("480x620")
root.configure(bg="#2c3e50")


style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="#ecf0f1", background="#34495e")


header = tk.Label(root, text="MINI TRANSLATOR APP", font=("Helvetica", 20, "bold"), 
                  bg="#2c3e50", fg="#1abc9c")
header.pack(pady=25)


tk.Label(root, text="Type here:", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10, "bold")).pack()
input_box = tk.Text(root, height=6, width=45, font=("Arial", 11), 
                    bg="#ecf0f1", relief="flat", padx=10, pady=10)
input_box.pack(pady=10)


tk.Label(root, text="Choose Language:", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10, "bold")).pack()
languages = ['arabic', 'english', 'japanese', 'french', 'spanish', 'german', 'korean', 'chinese (simplified)', 'russian']
lang_selection = ttk.Combobox(root, values=languages, font=("Arial", 11), state="readonly")
lang_selection.set('english')
lang_selection.pack(pady=5)


btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=20)

translate_btn = tk.Button(btn_frame, text="TRANSLATE", command=perform_translation, 
                          bg="#1abc9c", fg="white", font=("Arial", 10, "bold"), 
                          width=15, relief="flat", cursor="hand2", activebackground="#16a085")
translate_btn.pack(side=tk.LEFT, padx=10)

copy_btn = tk.Button(btn_frame, text="COPY RESULT", command=copy_to_clipboard, 
                     bg="#34495e", fg="white", font=("Arial", 10, "bold"), 
                     width=15, relief="flat", cursor="hand2", activebackground="#2c3e50")
copy_btn.pack(side=tk.LEFT, padx=10)


tk.Label(root, text="Translation result:", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10, "bold")).pack()
output_box = tk.Text(root, height=6, width=45, font=("Arial", 12), 
                     bg="#34495e", fg="#ecf0f1", relief="flat", padx=10, pady=10)
output_box.config(state='disabled')
output_box.pack(pady=10)

root.mainloop()