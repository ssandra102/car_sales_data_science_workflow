# car_sales_data_science_workflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ssandra102/car_sales_data_science_workflow.git
```
### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv mlproj
```

```bash
mlproj/Scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ssandra102/car_sales_data_science_workflow.mlflow \
MLFLOW_TRACKING_USERNAME=ssandra102 \
MLFLOW_TRACKING_PASSWORD=6b235e975826c50ab932e83ce1a719d24a7c439d \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ssandra102/car_sales_data_science_workflow.mlflow

export MLFLOW_TRACKING_USERNAME=ssandra102 

export MLFLOW_TRACKING_PASSWORD=6b235e975826c50ab932e83ce1a719d24a7c439d

```