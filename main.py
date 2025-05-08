from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    """Home page of the web application."""
    return render_template("index.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    """API endpoint to get temperature data for a specific station and date."""
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature
            }


@app.route("/api/v1/<station>")
def all_data(station):
    """API endpoint to get all temperature data for a specific station."""
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/annual/<station>/<year>")
def yearly_data(station, year):
    """API endpoint to get annual temperature data for a specific station and year."""
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20,)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)