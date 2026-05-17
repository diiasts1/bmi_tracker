# BMI Fitness Tracker Project

## Project Design
We made a modular system using Python. The project follows all the course requirements and is divided into distinct packages and files:
- `models.py`: Contains the main classes for users and implements Object-Oriented Programming (OOP) like Encapsulation, Inheritance, and Polymorphism.
- `storage.py`: Handles saving and loading user profiles into a local JSON text file so data is not lost.
- `utils.py`: Includes helper tools like drawing the progress chart with ASCII symbols, validating input using regular expressions (Regex), and tracking function calls with decorators.
- `main.py`: The central file that runs the system and controls the user menu loop.

## Team Work and Individual Contributions
We divided the project into separate domains. Each member worked as a Lead for a specific module and integrated them together:

* **Dias (Team Lead & Database Lead)**
  - Responsible for the `storage.py` module.
  - Designed the data persistence layer using Python's `json` and `os` modules to save and load user history safely.
  - Helped with the integration phase in `main.py`.

* **Erasyl (Logic & Processing Lead)**
  - Responsible for the `utils.py` module.
  - Implemented core logic functions: the ASCII progress graph generation, validation using the `re` module, and high BMI filtering using `lambda`, `map`, and `filter`.
  - Created custom decorators and generators for processing data.

* **Elina (Quality Assurance & UI Lead)**
  - Responsible for the `models.py` module and `tests.py`.
  - Created the class hierarchies (`Person` and `User`) with strict encapsulation rules.
  - Wrote 5 unit tests using the `unittest` framework to guarantee a 100% test pass rate and ensured PEP8 code compliance.

## How to Run the Project
1. Open the project folder in PyCharm.
2. To run the main app menu, execute:
   `python main.py`
3. To run and check the automatic tests, execute:
   `python tests.py`