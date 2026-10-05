# Astronomy Observation Logger

A Python-based application for recording, managing, analyzing, and visualizing astronomical observations.

## Project Description

This project is an astronomy observation logger developed in Python. It allows users to record different types of astronomical observations and manage the collected data using a Pandas DataFrame.

The application supports both **photometric** and **spectroscopic** observations.

## Features

* Add photometric observations
* Add spectroscopic observations
* Display all observations
* Calculate average exposure time
* Find maximum exposure time
* Find minimum exposure time
* Calculate total exposure time
* Search for observations by target name
* Save observations to a CSV file
* Save observations to an SQLite database
* Visualize target exposure times using a bar chart
* Test the project using Jupyter Notebook

## Observation Types

### Photometric Observation

Photometric observations contain:

* Target
* Observer
* Filter
* Exposure time
* Magnitude

### Spectroscopic Observation

Spectroscopic observations contain:

* Target
* Observer
* Filter
* Exposure time
* Wavelength

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Jupyter Notebook

## Project Structure

```text
astronomy-observation-logger/
│
├── main.py
├── observation.py
├── database.py
├── visualization.py
├── for_test_in_jupyter.ipynb
├── first_observation.csv
├── observation.db
├── __pycache__/
└── .ipynb_checkpoints/
```

## How to Run

Make sure Python is installed on your computer.

Run the main program using:

```bash
python main.py
```

The program provides a menu that allows the user to add, search, analyze, save, and visualize astronomical observations.

## Database

The project uses SQLite to store observation data in:

```text
observation.db
```

## Author

Mohammadali Sahargahi
