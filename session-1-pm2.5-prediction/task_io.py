import pandas as pd


class TaskIO():
    def __init__(self, train, test, result):
        self.train = train
        self.test = test
        self.result = result

    def import_training_data(self):
        return pd.read_csv(self.train, encoding="big5")

    def import_testing_data(self):
        return pd.read_csv(self.test, encoding="big5", header=None)

    def export_prediction(self, data):
        data.to_csv(self.result, index=False)
