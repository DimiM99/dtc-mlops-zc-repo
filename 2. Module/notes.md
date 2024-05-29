### Notes for the module and HW

#### create a conda environment
```bash
conda create -p .env/mlops_moodule2 python=3.9
```

#### activate the environment (run inside the 2. Module)
```bash
conda activate .env/mlops_moodule2
```

#### install the required packages
```bash
pip install -r requirements.txt
```

#### start mlflow server with the database (run inside the 2. Module/mlflow-files)
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts   
```