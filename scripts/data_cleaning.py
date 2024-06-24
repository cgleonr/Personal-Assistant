import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
import random
import json

class HuggingFaceDatasetDownloader:
    def __init__(self, address:str, filename:str, download = True, save_local = False):
        """This class is in charge of downloading datasets to store locally, for cleaning,
        prep, and any other reason why a dataset mey need to be stored locally. All files will be saved under the
        "/datasets" directory.

        Input:
            address: string, address of the dataset, found on HuggingFace, e.g. nvidia/HelpSteer
            filenaame: name to be given to the saved file, e.g. HelpSteer.
        """
        self.address = address
        self.filename = filename
        if download:
            self.ds = self.fetch_data_from_web()
            self.convert_to_dataframes(save_local)
        else:
            with open("varhholder/variables.json", "w") as fp:
                var = json.load(fp)
                var["download_from_web"] = False
                json.dump(var, fp)

    def fetch_data_from_web(self):
        """This function is directly in charge of fetching the data from HuggingFace and saving it
        to a local variable 'ds' in its original format.
        """
        return load_dataset(self.address, split=['train', 'validation'],
                cache_dir='/datasets') #Huggingface has good datasets unfortunately

    def convert_to_dataframes(self, save_local=False):
        """Used to convert the datasets object into a pd.DataFrame object"""
        sets = len(self.ds)
        if sets == 2:
            try:
                train = pd.DataFrame(self.ds[0])
                test = pd.DataFrame(self.ds[1])
            except:
                train = pd.DataFrame(self.ds['train'])
                test = pd.DataFrame(self.ds['validation'])
        
        else:
            print(f"Downloaded dataset has {sets} partitions. Please manually change code")
        if save_local:
            try:
                train.to_csv(f"datasets/{self.filename}_train.csv")
                test.to_csv(f"datasets/{self.filename}_test.csv")
            except:
                print("could not save data to files")

        self.data = (train, test)


if __name__ == "__main__":
    HuggingFaceDatasetDownloader(address="nvidia/HelpSteer", filename="HelpSteer", save_local=False)
    print("Class test run successfully")