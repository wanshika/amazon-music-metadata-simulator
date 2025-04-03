from flask import Blueprint, jsonify
import pandas as pd
from datetime import datetime
import os

catalog_routes = Blueprint('catalog', __name__)

try:
    tracks = pd.read_csv("data/tracks.csv")
    rights = pd.read_csv("data/rights.csv")

    rights["valid_from"] = pd.to_datetime(rights["valid_from"])
    rights["valid_to"] = pd.to_datetime(rights["valid_to"])
    today = pd.to_datetime(datetime.today().date())

except Exception as e:
    print("❌ Error loading data:", e)
    tracks, rights, today = None, None, None
