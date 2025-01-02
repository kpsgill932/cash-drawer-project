Cash Drawer Controller Software - User Guide
Introduction
This software controls your USB-connected cash drawer using standard ESC/POS commands. It provides an easy-to-use interface that allows you to open and close the cash drawer. The software also includes an auto-start feature, ensuring it runs automatically when your computer starts, enabling continuous operation.
Features:
•	Open Cash Drawer: Sends a command to open the cash drawer.
•	Close Cash Drawer: Sends a command to close the cash drawer (if supported by your hardware).
•	Auto-Start: The software automatically starts with Windows on boot, ensuring it’s always ready to use.
•	Logging: All actions, errors, and events are logged for troubleshooting and system monitoring.
Requirements:
•	Operating System: Windows (compatible with most versions).
•	Printer and Cash Drawer: Must support ESC/POS commands. Ensure your printer and cash drawer are connected and compatible.
•	Python 3.6+: The software requires Python to run. Ensure Python is installed on your system.
•	Node.js: Required to run the cash_drawer.js script, which handles hardware communication.
Installation:
1. Install Python:
•	Download Python from the official website: Python Downloads.
•	Follow the installation instructions and ensure that Python is added to your system’s PATH.
2. Install Dependencies:
•	Open the command prompt or terminal.
•	Install the required libraries by running the following commands:
bash
Copy code
pip install pyserial winshell
3. Download and Run the Software:
•	Download the software package and unzip it into a folder.
•	Open the folder in the command prompt and run the Python script using:
bash
Copy code
python test_cash_drawer.py
4. Auto-Start Setup:
•	The first time you run the software, it will automatically add itself to the Windows registry to enable auto-start on boot. This means the software will launch automatically every time your computer starts.
________________________________________
How to Use:
1. Connect the Cash Drawer:
•	Ensure the cash drawer is properly connected to your system via USB. The software assumes the drawer is connected via COM1 (you may need to adjust this in the code if using a different port).
2. Running the Software:
•	Upon running the software, a window will appear with two buttons:
o	Open Cash Drawer: Click this to send the command to open the cash drawer.
o	Close Cash Drawer: Click this to send the command to close the drawer (if supported).
•	A pop-up message will inform you whether the action was successful or if an error occurred.
3. Auto-Start Feature:
•	Once configured, the software will automatically run in the background when your computer boots up, allowing continuous operation without needing manual intervention.
•	To test this, simply restart your computer and confirm the program starts automatically in the background.
________________________________________
Troubleshooting:
1. "Serial Communication Error":
•	This error occurs if the software cannot connect to the cash drawer through the specified port.
o	Ensure that the cash drawer is properly connected.
o	Verify that the correct port is specified in the code (COM1 by default).
o	If using a different port, change the port in the code.
2. "Unexpected Error":
•	Any unexpected error will be logged in the file logs/cash_drawer.log.
o	Open this log file to get more detailed information on the error and identify the root cause.
3. Auto-Start Not Working:
•	If the software doesn't auto-start, ensure you have run it at least once to configure the registry entry.
•	Check if your system has any restrictions on modifying the registry or auto-starting programs.
________________________________________
Notes:
•	ESC/POS Commands: This software uses standard ESC/POS commands to control the cash drawer. Make sure your hardware supports these commands for compatibility.
•	Printer Compatibility: If your printer or cash drawer does not support ESC/POS commands, the commands may not work. Consult your printer's manual to check if it supports ESC/POS or for alternative commands.
________________________________________
This guide provides the necessary information to install, run, and troubleshoot the Cash Drawer Controller software. Should you encounter any issues or need further assistance, feel free to reach out for support.

