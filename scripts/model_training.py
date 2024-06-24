import pandas as pd
import numpy as np
from data_cleaning import HuggingFaceDatasetDownloader

loader = HuggingFaceDatasetDownloader(address="nvidia/HelpSteer", filename="HelpSteer", save_local=False)
train, test = loader.data

print(train.head)
print(test.head)

