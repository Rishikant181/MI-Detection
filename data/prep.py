import pandas
import numpy
import wfdb
import ast

def load_raw_annotations(path):
    Y = pandas.read_csv(path+'ptbxl_database.csv', index_col='ecg_id')
    Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

    return Y

def load_raw_data(path, df):
    data = [wfdb.rdsamp(path+f) for f in df.filename_hr]    
    data = numpy.array([signal for signal, meta in data])

    return data

def aggregate_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))

path = 'path/to/ptbxl/'

# Loading and converting raw annotations data
Y = load_raw_annotations(path)

# Loading raw signal data
X = load_raw_data(path, Y)

# Loading scp_statements.csv for diagnostic aggregation
agg_df = pandas.read_csv(path+'scp_statements.csv', index_col=0)
agg_df = agg_df[agg_df.diagnostic == 1]

# Applying diagnostic superclass
Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_diagnostic)

# Split data into train and test
test_fold = 10

# Training set
X_train = X[numpy.where(Y.strat_fold != test_fold)]
Y_train = Y[(Y.strat_fold != test_fold)].diagnostic_superclass

# Testing set
X_test = X[numpy.where(Y.strat_fold == test_fold)]
Y_test = Y[Y.strat_fold == test_fold].diagnostic_superclass
