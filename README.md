# 🌦️ Weather Data API

A Flask web app providing easy access to historical temperature data from various weather stations. Users can interact with both a web interface and RESTful API to query daily or annual temperature data.

---

## 📑 Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Page Structure](#page-structure)
  - [Color Scheme & Typography](#color-scheme--typography)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Libraries Used](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [How to Run](#how-to-run)
  - [Modifying the Input File](#modifying-the-input-file)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

---

## 🧠 User Experience (UX)

### User Stories

- As a user, I want to see a list of available weather stations so I know which codes I can query.
- As a user, I want to input a date and station to get the exact temperature reading.
- As a developer, I want a JSON API I can query with dates and station codes for integration into my own tools.
- As a user, I want a clean and simple front-end to help me use the app without technical knowledge.

---

## 🎨 Design

### Page Structure

- `index.html`: Displays instructions and a rendered list of station codes with descriptions.
- `about.html`: Describes the purpose of the API and how to use it.

### Color Scheme & Typography

- **Colors**: Clean white background, dark text for high readability.
- **Fonts**: Default browser sans-serif fonts for speed and clarity.
- Responsive layout using basic HTML/CSS for accessibility and mobile-friendliness.

---

## 🚀 Features

### Implemented Features

- Web interface to list all stations and explain how to use the API.
- RESTful endpoints to:
  - Get data by station and specific date.
  - Get all data from a station.
  - Get all annual temperature data for a station and year.
- Clean and readable code using Flask and pandas.
- Project structure following Flask best practices.

### Planned Improvements

- Add charts and data visualizations (e.g., line graph of annual temperatures).
- Add filtering by min/max/average temperature.
- Improve frontend with Bootstrap or Tailwind.
- Add error handling for invalid station codes or missing dates.

---

## 🧰 Technologies Used

### Languages Used

- Python (Flask backend)
- HTML (Frontend templates)
- CSS (Basic styling)

### Libraries Used

- **Flask** – for the web framework and API routing
- **pandas** – for data manipulation and CSV parsing
- **Jinja2** – for HTML templating
- **Werkzeug** – for development server
- (See `requirements.txt` for full list)

---

## 📁 Project Files

```bash
weather-data-api/
├── data_small/ # Contains weather station data files
├── static/
│ ├── styles.css # CSS styles for the frontend
│ └── script.js # (Optional) JS functionality
├── templates/
│ ├── index.html # Homepage
│ └── about.html # About page
├── main.py # Flask backend and API endpoints
├── requirements.txt # Python dependencies
└── README.md # This file
```

---

## 💻 Installation & Usage

### How to Run

1. Clone the repository:

```bash
   git clone https://github.com/your-username/weather-data-api.git
   cd weather-data-api
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt

```

Run the app:

```bash
python main.py

```

Open your browser and go to:

```bash
http://127.0.0.1:5000/
```

### Modifying the Input File

You can replace or update files in the data_small/ directory to include new or more recent station data.

Each file should be named using the station code and contain columns for DATE, TAVG, TMIN, and TMAX.

---

## ✅ Testing

Manual testing performed by querying each API endpoint with valid and invalid parameters.

Example valid API calls:

```bash
/api/v1/010010/2010-01-01
/api/v1/010010
/api/v1/annual/010010/2010
```

Planned: Pytest unit tests for route responses and data parsing.

## 🙏 Credits

### 👨‍💻 Development

- **Project Lead & Developer**: [Mahmudur Mahid]  
  Designed, developed, and documented the entire project using Flask and pandas.

### 📊 Data Sources

- **Weather Data**:  
  Sample weather station data used in this project is fictional or adapted from publicly available formats (e.g., from **NOAA**, **UK Met Office**, or educational datasets).
  > Data sourced from the [NOAA National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov/) under open data license.

### 🧰 Tools & Frameworks

- **Flask** – Micro web framework for Python
- **pandas** – Powerful data analysis and manipulation library
- **Jinja2** – Template engine for generating dynamic HTML
- **Python** – Primary programming language
- **HTML & CSS** – Basic frontend structure and styling

### 📚 Learning Resources & Documentation

- [Flask Documentation](https://flask.palletsprojects.com/) – for web app and API routing
- [pandas Documentation](https://pandas.pydata.org/docs/) – for data manipulation
- [MDN Web Docs](https://developer.mozilla.org/) – for frontend references (HTML/CSS)
