import pandas as pd
from load_all_data import label_data, sensor_data


# This code is for getting the label and sensor data for task 20 (fall forward when trying to sit down), trial 3.
# There is one dataset for each of the 32 subjects.
# In the data folder, there are 2 subfolders: label_data and sensor_data.
# There is one folder for every subject in each.


def get_onset_impact_frame_numbers() -> list:
    """Collects the onset and impact frame numbers, stores them in a tuple and appends that tuple to a list"""

    frame_numbers = []
    for v in label_data.values():
        fall_onset_frame = int(v.at[2, "Fall_onset_frame"])
        fall_impact_frame = int(v.at[2, "Fall_impact_frame"])
        frame_numbers.append((fall_onset_frame, fall_impact_frame))
    return frame_numbers


frame_numbers = get_onset_impact_frame_numbers()


def get_datasets() -> list:
    """Retrieves the relevant datasets"""

    datasets = []
    for v in sensor_data.values():
        for name, dataset in v.items():
            if "T20R03" in name:
                datasets.append(dataset)
    return datasets


datasets = get_datasets()


class DataEngineering:
    """Creating my dataset"""

    def __init__(self, zipped):
        """Takes one argument, a datastructure containing the frame numbers and the datasets"""

        self.zipped = zipped
        self.lower_values = []
        self.upper_values = []
        self.datasets = []

    def unpack_zipped(self):
        """Iterates through the datastructure and sorts into three lists"""

        for item in self.zipped:
            lower = item[0][0]
            upper = item[0][1]
            dataset = item[1]

            self.lower_values.append(lower)
            self.upper_values.append(upper)
            self.datasets.append(dataset)

    def sort_into_class(self, x, i):
        """This is used to sort all entries in a pandas dataframe into classes"""

        lower = self.lower_values[i]
        upper = self.upper_values[i]
        number = x["FrameCounter"]

        if number < lower:
            return 0
        elif lower <= number <= upper:
            return 1
        elif number > upper:
            return 2

    def add_class_column(self):
        """Iterates through all the dataframes and creating a class column for each"""

        for i in range(32):
            self.datasets[i]["Class"] = self.datasets[i].apply(lambda x: self.sort_into_class(x, i), axis=1)

    def drop_columns(self):
        """Drop unnecessary columns"""

        for dataset in self.datasets:
            dataset.drop(["TimeStamp(s)", "FrameCounter"], inplace=True, axis=1)

    def create_dataset(self):
        """Make one dataset out of all the 32 datasets"""

        dataset = pd.concat(self.datasets)
        return dataset

    def run(self):
        """The main function that runs the other methods when called"""

        self.unpack_zipped()
        self.add_class_column()
        self.drop_columns()
        dataset = self.create_dataset()
        return dataset


zipped_frame_numbers_datasets = zip(frame_numbers, datasets)
instance = DataEngineering(zipped_frame_numbers_datasets)
data = instance.run()
