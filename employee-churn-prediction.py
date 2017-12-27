import pandas as pd
from h2o import h2o

# Removing existing data from H2O Cluster

h2o.init(ip="localhost", port=54321)
h2o.remove_all()

# Loading HR Analytics Data from CSV File
full_data_frame = h2o.H2OFrame(pd.read_csv("dataset/HR_comma_sep.csv", index_col=None, header=0))

# Defining categorical features
feature_columns = [
    'left',
    'Work_accident',
    'promotion_last_5years',
    'sales'
]

# Defining continuous features
continuous_feature_columns = [
    'satisfaction_level',
    'last_evaluation',
    'number_project',
    'average_montly_hours',
    'time_spend_company',
    'salary'
]

training_data_frame, test_data_frame = full_data_frame.split_frame(ratios=[.8])
training_data_frame[feature_columns] = training_data_frame[feature_columns].asfactor()
test_data_frame[feature_columns] = test_data_frame[feature_columns].asfactor()

print(training_data_frame[0, :])
print(test_data_frame[0, :])

feature_columns.extend(continuous_feature_columns)
training_data_frame = training_data_frame[feature_columns]
test_data_frame = test_data_frame[feature_columns]

# Initialize RandomForestModel

random_forest_model = h2o.H2ORandomForestEstimator(
    model_id="HREmployeeChurnPrediction",
    ntrees=10,
    max_depth=10,
    min_rows=4,
    nfolds=10,
    seed=12345
)

random_forest_model.train(y='left', training_frame=training_data_frame)
performance = random_forest_model.model_performance(test_data=test_data_frame)
print(performance)
