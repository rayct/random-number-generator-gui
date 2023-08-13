# Random Number Generator

## Code Stack: Python and `tkinter`

### Version 1.0.6
#### UI Version

**Major Features Update and Fixed a number of Critical Bugs.**
  
* This version of the code adds an "Open Log File" button that uses the os.system function to open the log.txt file using the default text editor. The try and except blocks are used to handle different operating systems (Windows, macOS, and Linux).

* In this updated code, I've added more specific exception handling using the os.name attribute to determine the operating system. This should help address the W0702 Pylint warning. Additionally, I've added a generic exception handler in the open_log_file function to display an error message in case of any exceptions.

* The log_filename is generated based on the process ID to create a unique log file for each execution of the program. After writing the log, the os.chmod() function is used to set the permissions of the log file to read-only. Additionally, the open_log_file function uses the process ID to open the correct log file.
  
* The shuffled_numbers list is created by shuffling the input_numbers list to ensure that each generated number is unique. This should prevent the generation of duplicate random numbers.

* In this updated version of the code, a directory named "logs" is created if it doesn't exist, and the log files are stored in that directory. The os.path.join() function is used to create the full path to the log file within the "logs" directory.

* Fixed the Bug: `Variable name "e" doesn't conform to snake_case naming stylePylintC0103:invalid-name`,
  by renaming the exception variable from `e` to `os_error` to better adhere to the `snake_case` naming style and provide a more descriptive name.

---

### Version 1.0.5
#### UI Version
**Version Changes:**
* Improved GUI (Expanded layout)
* This version of the GUI includes an expanded layout with a larger text box for output, a scrollbar for the output text box, and improved alignment of labels and entry fields. You can further customize and enhance the layout and appearance according to your preferences.

---

### Version 1.0.4
#### UI Version
**Major Feature Update:**
* Added a UI
* Incorporated a simple graphical user interface (GUI) using the `tkinter`:

* This program creates a simple GUI using the `tkinter` library. It allows you to input numbers, weights, and the number of samples, and then generates and displays random numbers based on the provided inputs. Make sure to have the `tkinter` library installed in your Python environment to run this program.

---


### Version 1.0.3
#### CMD Line Version
**Version Changes:**
* CMD Line with Prompt
* A command-line of the program that prompts the user to input the numbers, weights, and the number of samples:

* Run the program using the following command:

`python random_number_generator_cmd_prompt.py`


---

### Version 1.0.2
#### CMD Line Version
**Version Changes:**
* To generate high-quality random numbers, you can use the `random.choices()` function from the `random` module with the `weights` parameter for weighted random selection. Here's the program using the `random` module to generate high-quality random numbers based on the provided list of numbers and their weights:

* In this program, the `random.choices()` function is used to generate a list of high-quality random numbers based on the provided `numbers` and `weights`. You can adjust the `num_samples` variable to generate as many random numbers as you need. This approach ensures that the random numbers are generated with better statistical properties compared to manual weighted selection.


---

### Version 1.0.1
#### CMD Line Version
**Version Changes:**
* Using the `random` module to achieve weighted random selection:

* The `random.choices()` function from the `random` module allows you to perform weighted random selection directly, which simplifies the process. The function returns a list of randomly selected elements based on their weights, and we select the first element from that list to get the final result.

---

### Version 1.0
#### CMD Line Version
* An algorithm to generate random numbers in Python based on the provided list of numbers: 4, 6, 10, 13, 34, 3, 5.
One way to achieve this is by using a weighted random selection algorithm. Here's an example of how you can implement this:

* In this example, each number in the `numbers` list has an equal weight of 1. You can adjust the weights according to your preferences if you want certain numbers to have a higher chance of being selected.

* Please note that this algorithm ensures that numbers are selected with a probability proportional to their weights, but it may not provide the same statistical properties as Python's built-in `random` module. If you require high-quality random numbers for cryptographic or scientific purposes, it's recommended to use the `random` module provided by Python's standard library.


---


Program and Documentation Created By: **Raymond C. TURNER**

Last Updated: 1 Day ago
