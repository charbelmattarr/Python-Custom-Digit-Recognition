import sys
import tkinter as tk
import subprocess

import cv2  # version 3.2.0
def run_file():
    python_path = sys.executable  # Get the path of the current Python interpreter
    script_path = 'NEW_digit_recog.py'  # Path to the script you want to run

    subprocess.Popen([python_path, script_path])

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("My App")

# Configure the window's appearance
root.geometry("300x200")
root.configure(bg="#f2f2f2")

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=20)

# Create the buttons
button1 = tk.Button(button_frame, text="Run File", command=run_file, padx=10, pady=5, bg="#336699", fg="white", font=("Arial", 12))
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(button_frame, text="Exit", command=exit_program, padx=10, pady=5, bg="#cc3333", fg="white", font=("Arial", 12))
button2.pack(side=tk.LEFT, padx=10)

# Start the main event loop
root.mainloop()
