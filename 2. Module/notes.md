### Notes for the module and HW

#### create a conda environment
```bash
conda create -p .env/mlops_moodule2 python=3.9
```

#### start mlflow server with the database
```bash
mlflow ui --backend-store-uri sqlite:///mlflow-files/mlflow.db   
```