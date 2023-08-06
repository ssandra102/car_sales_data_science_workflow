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
git clone https://github.com/ssandra102/car_sales_data_science_workflow.git
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

Now, open up your local host and port



## MLflow
##### cmd
- mlflow ui

### dagshub
MLFLOW_TRACKING_URI=<https://dagshub.com/{USERNAME}/{REPO_NAME}.mlflow> \
MLFLOW_TRACKING_USERNAME=USERNAME \
MLFLOW_TRACKING_PASSWORD=PASSWORD \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=<https://dagshub.com/{USERNAME}/{REPO NAME}.mlflow>

export MLFLOW_TRACKING_USERNAME=<USERNAME>

export MLFLOW_TRACKING_PASSWORD=<PASSWORD>

```


## Flask Web App
<p align="left">
<img src ="https://github.com/ssandra102/car_sales_data_science_workflow/assets/72643907/51fb23aa-731f-48bf-9655-d3923bf1a82c">
&nbsp; &nbsp; &nbsp; &nbsp;
  

<p align="left">
<img src ="https://github.com/ssandra102/car_sales_data_science_workflow/assets/72643907/84c9b46c-20dc-4893-b552-980bc8b54e08">
&nbsp; &nbsp; &nbsp; &nbsp;

(note: the values entered in the form are random. The predicted car price is in Lakhs.)



