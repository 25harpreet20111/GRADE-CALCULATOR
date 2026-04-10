import tkinter as tk
from tkinter import messagebox

def grade_function(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def calculate():
    try:
        grades = entry.get().split(',')
        grades = [float(g.strip()) for g in grades]

        if len(grades) < 1 or len(grades) > 5:
            messagebox.showerror("Error", "Enter 1 to 5 grades only")
            return

        avg = sum(grades) / len(grades)
        grade = grade_function(avg)

        result_label.config(
            text=f"📊 Average: {avg:.2f}   |   🎓 Grade: {grade}",
            fg="#1B4F72"
        )

    except:
        messagebox.showerror("Error", "Invalid input")

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("🎓  Grade Calculator")
root.geometry("420x500")
root.config(bg="#EAF2F8")

header = tk.Frame(root, bg="#5DADE2", relief="raised", bd=4)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="🎓 GRADE CALCULATOR 🎓",
    font=("Comic Sans MS", 20, "bold"),
    bg="#5DADE2",
    fg="white",
)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#EAF2F8")
frame.pack(pady=30)

label = tk.Label(
    frame,
    text="Enter grades (comma separated):",
    font=("Comic Sans MS", 12, "bold"),
    bg="#EAF2F8",
    fg="#1B4F72"
)
label.pack(pady=10)

entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=25,
    bd=3,
    relief="groove",
    justify="center"
)
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#EAF2F8")
btn_frame.pack(pady=15)

calc_btn = tk.Button(
    btn_frame,
    text="📊 Calculate",
    command=calculate,
    bg="#58D68D",
    fg="white",
    font=("Comic Sans MS", 12, "bold"),
    width=15,
    relief="raised",
    bd=3
)
calc_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(
    btn_frame,
    text="🔄 Reset",
    command=reset,
    bg="#EC7063",
    fg="white",
    font=("Comic Sans MS", 12, "bold"),
    width=15,
    relief="raised",
    bd=3
)
reset_btn.grid(row=0, column=1, padx=10)

result_label = tk.Label(
    root,
    text="",
    font=("Comic Sans MS", 14, "bold"),
    bg="#EAF2F8",
)
result_label.pack(pady=25)

footer = tk.Label(
    root,
    text="Developed by Harpreet Kaur~25MCA20111",
    bg="#EAF2F8",
    fg="#5D6D7E",
    font=("Arial", 10, "italic"),
)
footer.pack(side="bottom", pady=10)

root.mainloop()