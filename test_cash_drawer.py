import os
import logging
import tkinter as tk
from tkinter import messagebox
import subprocess  # Import subprocess to call Node.js script
import sys
import winshell
from win32com.client import Dispatch
import winreg as reg

# Ensure the 'logs' folder exists inside the CashDrawerProject folder
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Set up logging to save in the 'logs' folder within the CashDrawerProject directory
logging.basicConfig(filename=os.path.join(log_folder, 'cash_drawer.log'), level=logging.INFO, format='%(asctime)s - %(message)s')

# Test log entry to check if logging is working at the start
logging.info("Cash Drawer Controller started")

def open_cash_drawer():
    """Function to open the cash drawer by sending a command to the hardware"""
    try:
        # Call the Node.js script to open the cash drawer
        result = subprocess.run(['node', 'D:/CashDrawerProject/js_solution/cash_drawer.js', 'open'], capture_output=True, text=True, check=True)
        logging.info(f"Sent 'open' command to cash drawer via Node.js. Output: {result.stdout}")
        messagebox.showinfo("Success", "Cash drawer opened successfully!")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Node.js script: {e.stderr}")
        messagebox.showerror("Error", f"Error opening cash drawer: {e.stderr}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        messagebox.showerror("Error", f"Unexpected error: {e}")

def close_cash_drawer():
    """Function to close the cash drawer by sending a command to the hardware"""
    try:
        # Call the Node.js script to close the cash drawer (if supported by the cash drawer)
        result = subprocess.run(['node', 'D:/CashDrawerProject/js_solution/cash_drawer.js', 'close'], capture_output=True, text=True, check=True)
        logging.info(f"Sent 'close' command to cash drawer via Node.js. Output: {result.stdout}")
        messagebox.showinfo("Success", "Cash drawer closed successfully!")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Node.js script: {e.stderr}")
        messagebox.showerror("Error", f"Error closing cash drawer: {e.stderr}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        messagebox.showerror("Error", f"Unexpected error: {e}")

def create_ui():
    """Create the user interface for controlling the cash drawer"""
    root = tk.Tk()
    root.title("Cash Drawer Controller")

    # Add a button to open the cash drawer
    open_button = tk.Button(root, text="Open Cash Drawer", command=open_cash_drawer)
    open_button.grid(row=0, column=0, pady=20, padx=20)

    # Add a button to close the cash drawer
    close_button = tk.Button(root, text="Close Cash Drawer", command=close_cash_drawer)
    close_button.grid(row=1, column=0, pady=20, padx=20)

    # Add a label to give additional context or instructions to the user
    label = tk.Label(root, text="Control your cash drawer", font=("Helvetica", 14))
    label.grid(row=2, column=0, pady=20)

    # Start the GUI loop
    root.mainloop()

def create_shortcut():
    """Create a shortcut in the Windows Startup folder to auto-start the program"""
    # Get the path to the Startup folder
    startup_folder = winshell.startup()

    # Get the full path to the Python script
    script_path = os.path.abspath(sys.argv[0])

    # Define the shortcut's name
    shortcut_name = "CashDrawerController.lnk"

    # Define the full path to the shortcut
    shortcut_path = os.path.join(startup_folder, shortcut_name)

    # Create the shortcut
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = sys.executable  # Path to the Python executable
    shortcut.Arguments = script_path  # Path to the script
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.save()

    logging.info(f"Shortcut created in Startup folder: {shortcut_path}")
    print(f"Shortcut created in Startup folder: {shortcut_path}")

def add_to_registry():
    """Add the program to Windows Registry for auto-start"""
    # Path to the Python script
    script_path = os.path.abspath(sys.argv[0])

    # Registry path for startup programs
    registry_key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    # Open the registry key (creating if it doesn't exist)
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_key, 0, reg.KEY_WRITE)

    # Add the program to the registry
    reg.SetValueEx(key, "CashDrawerController", 0, reg.REG_SZ, script_path)
    reg.CloseKey(key)

    logging.info("Added to registry for auto-start.")
    print("Added to registry for auto-start.")

if __name__ == "__main__":
    # Choose one method to implement auto-start
    # create_shortcut()  # To use the Startup folder method
    add_to_registry()  # To use the Registry method
    
    create_ui()  # Start the application (GUI for opening/closing the cash drawer)
