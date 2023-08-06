import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import (DataTransformationConfig)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        
        self.config = config
        self.data = pd.read_csv(self.config.data_path)

    
    def cleaning_data(self):

        df = self.data.drop(['Order','Sales_in_thousands','Order Date','dealership','color','Vehicle_type'], axis=1)
        #remove letters from strings in "Price_in_lakhs" column
        df['Price_in_lakhs'] = df['Price_in_lakhs'].str.replace('L', '', regex=True)   
        logger.info("Removed unrelated columns")
        logger.info(df.shape)
        print(df.shape)

        df.to_csv(os.path.join(self.config.root_dir, "transformed_data.csv"),index = False)
        logger.info("Transformed data created")

    def train_test_spliting(self):
        data = pd.read_csv(self.config.transformed_data)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)