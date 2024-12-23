# Random Number Generator with GUI

## Code Stack: Python and `tkinter`

![Version](https://img.shields.io/badge/version-0.1.1.beta.1-blue)
### UI Version

**Features Update and Fixed a number of Critical Bugs.**

* Improved GUI (Expanded layout)
  This version of the GUI includes an expanded layout with a larger text box for output, a scrollbar for the output text box, and improved alignment of labels and entry fields. You can further customize and enhance the layout and appearance according to your preferences.
  
* Added an "Open Log File" button that uses the os.system function to open the `log.txt` file using the default text editor. The try and except blocks are used to handle different operating systems (Windows, macOS, and Linux).

* I've added more specific exception handling using the os.name attribute to determine the operating system. This should help address the `W0702 Pylint warning`. Additionally, I've added a generic exception handler in the `open_log_file` function to display an error message in case of any exceptions.

* The `log_filename` is generated based on the process `ID` to create a unique log file for each execution of the program. Additionally, the `open_log_file` function uses the process ID to open the correct log file.
  
* The `shuffled_numbers` list is created by shuffling the `input_numbers` list to ensure that each generated number is unique. This should prevent the generation of duplicate random numbers.

* A directory named `"logs"` is created if it doesn't exist, and the log files are stored in that directory. The `os.path.join()` function is used to create the full path to the log file within the `"logs"` directory.

* Fixed the Bug: `Variable name "e" doesn't conform to snake_case naming stylePylintC0103:invalid-name`, by renaming the exception variable from `e` to `os_error` to better adhere to the `snake_case` naming style and provide a more descriptive name.

---

![Version](https://img.shields.io/badge/version-0.1.0.beta-blue)
### UI Version
**First Beta Release**
Random Number Generator with GUI

---

Program and Documentation Created By: **Raymond C. TURNER**

Last Updated: 1 Day ago
