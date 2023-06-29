import sys
import tkinter as tk
import subprocess


def run_file(image_path):
    python_path = sys.executable  # Get the path of the current Python interpreter
    script_path = 'NEW_digit_recog.py'  # Path to the script you want to run

    subprocess.Popen([python_path, script_path, image_path])

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("My App")

# Configure the window's appearance
root.geometry("300x200")
root.configure(bg="#f2f2f2")

# Get the image path from command-line argument
if len(sys.argv) > 1:
    image_path = sys.argv[1]
    run_file(image_path)
    exit_program()

# Start the main event loop
root.mainloop()
