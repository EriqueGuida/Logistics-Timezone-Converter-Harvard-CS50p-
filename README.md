# LOGISTICS TIMEZONE CONVERTER
#### Video Demo:  <https://youtu.be/GOYwgFry8ac>
#### Description:

The **Logistics Timezone Converter** is a Python-based command-line tool designed to solve a recurring problem in international logistics and dispatching: calculating time differences between global hubs accurately and quickly.

### Motivation
As someone with experience as a **Dispatcher for Car Hauling** in the United States, I have personally faced the challenges of managing schedules across different time zones. Coordinating drivers in California (Pacific Time) while dealing with clients in New York (Eastern Time) or support teams abroad requires constant mental math. This project was born from the desire to automate this process, ensuring that time calculations are always precise, avoiding common errors when crossing the "midnight threshold."

### How it Works
The application allows a user to input a specific time in 24-hour format (HH:MM) and select an origin city and a destination city from a pre-defined database of global hubs. The program then calculates the time in the destination city, properly handling positive and negative offsets relative to UTC.

### Project Structure
The project is divided into two main files as per CS50P requirements:

1. **`project.py`**: Contains the core logic of the application.
   - `main()`: Orchestrates the user input, validation, and the flow of conversion.
   - `validate_time()`: Uses string manipulation and error handling to ensure the user provides a valid 24h format.
   - `convert_to_utc()`: Standardizes the local time to Universal Coordinated Time (UTC). This is a crucial design choice to make the system scalable; instead of calculating offsets between every pair of cities, everything goes through UTC first.
   - `convert_from_utc()`: Takes the UTC time and applies the destination's offset. The use of the modulo operator (`% 24`) ensures that if a calculation results in 25:00 or -1:00, the program correctly displays 01:00 or 23:00, respectively.
   - `format_time()`: Ensures the output is user-friendly, adding leading zeros where necessary (e.g., "09:05" instead of "9:5").

2. **`test_project.py`**: A dedicated testing suite using `pytest`. It contains multiple test cases for each of the core functions to ensure reliability. We test edge cases like midnight transitions, invalid string formats, and cities with large positive/negative offsets.

3. **`requirements.txt`**: Lists the dependencies (pytest) needed to run the test suite.

### Design Choices
During the development, I debated whether to use external libraries like `pytz` or `datetime`. However, I chose to implement the mathematical logic manually using dictionaries and the modulo operator. This was a deliberate choice to demonstrate my understanding of Python fundamentals, logic flow, and arithmetic operations learned during the **CS50P** course. This manual implementation shows the "under the hood" logic of how timezone offsets work in a programmatic environment.

### Conclusion
This project not only fulfills the requirements for the CS50P certificate but also serves as a practical tool that reflects my career transition from logistics to Systems Development. It combines my past professional expertise with my new technical skills in Python.
