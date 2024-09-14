import pandas as pd
import os


def load_label_data() -> dict:
    """Loads all label data from an excel file"""

    label_data = {}
    for item in os.listdir("data/label_data"):
        path = f"data/label_data/{item}"
        df = pd.read_excel(path)
        label_data[item] = df
    return label_data


def load_sensor_data() -> dict:
    """Loads all sensor data from a csv file"""

    sensor_data = {}
    for folder in os.listdir("data/sensor_data"):
        datasets = {}
        path_to_folder = f"data/sensor_data/{folder}"
        for item in os.listdir(path_to_folder):
            path_to_item = f"{path_to_folder}/{item}"
            df = pd.read_csv(path_to_item)
            datasets[item] = df
        sensor_data[folder] = datasets
    return sensor_data


label_data = load_label_data()
sensor_data = load_sensor_data()
