# employee churn prediction

GSU - Machine Learning Lesson Project

# Dataset
HR Analytics Data is published [here](https://www.kaggle.com/ludobenistant/hr-analytics/downloads/HR_comma_sep.csv) to resolve employee churn prediction.
Dataset is also exist in project under <b>dataset folder</b>, you can access easily.

# Environment setup
    * Conda (4.4.4)
    * Python (3.5.3)
    * H2O.ai (3.16.0.2)
    * Conda & H2O.ai connection

## Conda
Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux.

You can access detailed installation guide from [here](https://conda.io/docs/user-guide/install/index.html)

## Python
Conda supports Python by default even if Python is already installed in your computer.

You can access detailed installation guide from [here](https://conda.io/docs/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages)

## H2O.ai
H2O is an open source, in-memory, distributed, fast, and scalable machine learning and predictive analytics platform.

You can find detailed installation guide and download latest H2O release from [here](http://h2o-release.s3.amazonaws.com/h2o/rel-wheeler/2/index.html)

After starting H20 cluster in your machine, H2O will be point your browser to http://localhost:54321 where H2O works.

## Conda & H2O.ai connection
Before running <b>employee-churn-prediction.py</b> which is execution file to create randomForestModel, you need to install H2O.ai with conda.

From terminal, please run:

<code>
    conda install -c h2oai h2o=3.16.0.2
</code>

# code execution
In order to create RandomForestModel with default parameters, you only need to run employee-churn-prediction.py.However, H20 cluster should be running at localhost and default port 54321 before execution.
After execution model performance will be written to logs like:

<code>
                
    MSE: 0.015226097527886655
    RMSE: 0.12339407411981604
    LogLoss: 0.0657476990661764
    Mean Per-Class Error: 0.024314773392581035
    AUC: 0.9932409589719724
    Gini: 0.9864819179439448
    Confusion Matrix (Act/Pred) for max f1 @ threshold = 0.34526066333055494: 
           0     1    Error    Rate
    -----  ----  ---  -------  -------------
    0      2284  13   0.0057   (13.0/2297.0)
    1      36    689  0.0497   (36.0/725.0)
    Total  2320  702  0.0162   (49.0/3022.0)
    
    metric                       threshold    value     idx
    ---------------------------  -----------  --------  -----
    max f1                       0.345261     0.965662  127
    max f2                       0.216413     0.964335  160
    max f0point5                 0.678677     0.978929  101
    max accuracy                 0.350082     0.983786  125
    max precision                1            1         0
    max recall                   0.000342523  1         398
    max specificity              1            1         0
    max absolute_mcc             0.345261     0.955266  127
    max min_per_class_accuracy   0.167209     0.971267  178
    max mean_per_class_accuracy  0.216413     0.975685  160
    Gains/Lift Table: Avg response rate: 23.99 %
</code>

In addition to detailed performance result,if you need to see detailed information about dataset and model, you point your browser to http://localhost:54321, you will see H20 Flow GUI.
employee-churn-prediction.py removes all H2O datasets before creating models due to prevent data duplication.

 

