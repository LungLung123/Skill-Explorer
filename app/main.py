from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


filename = "./resources/Australian_Skills_Classification.xlsx"


def job():
    sheet = "Occupation Descriptions"
    df = pd.read_excel(io=filename, sheet_name=sheet, engine="openpyxl")
    job = df["ANZSCO_Title"].tolist()
    return job


def industry_cluster():
    sheet = "Specialist tasks"
    df = pd.read_excel(io=filename, sheet_name=sheet, engine="openpyxl")
    industry = df["Cluster_Family"].tolist()
    industry = list(dict.fromkeys(industry))
    return industry


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/build_skill")
def build_skill():
    return render_template("build_skill.html")


@app.route("/skill_chart")
def skill_chart():
    return render_template("skill_chart.html")


@app.route("/learning")
def learning():
    industry = industry_cluster()
    job_list = job()
    return render_template("learning.html", jobs=job_list, ind_len=len(industry), industry=industry)


@app.route("/forecast")
def forecast():
    return render_template("forecast.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
