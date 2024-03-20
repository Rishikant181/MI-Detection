import pandas
import numpy
import wfdb
import ast

def load_raw_annotations(path):
    Y = pandas.read_csv(path + 'ptbxl_database.csv', index_col = 'ecg_id')
    Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

    return Y

def aggregate_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))

def load_raw_data(path, df, lead = 0):
    # If lead == 0, this means all leads are required (default behaviour)
    if (lead == 0):
        X = [wfdb.rdsamp(path+f) for f in df.filename_hr]    
        X = numpy.array([signal for signal, meta in X])

        return X
    # If lead > 12, this means wrong lead selected, throw error
    elif (lead < 0 or lead > 12):
        print("Invalid lead!")

        return None
    # Else, return the data from the selected lead
    else:
        X = numpy.zeros([5000, df.filename_hr.size])
        for i in range(df.filename_hr.size):
            signal = numpy.array(wfdb.rdsamp(path + df.filename_hr[i + 1])[0])[:, lead - 1]
            X[:, i] = signal

        return X

path = '/home/rishikant/Documents/Datasets/PTB-XL/'

# Loading and converting raw annotations data
Y = load_raw_annotations(path)

# Loading raw signal data
X = load_raw_data(path, Y, 1)

# Loading scp_statements.csv for diagnostic aggregation
agg_df = pandas.read_csv(path + 'scp_statements.csv', index_col = 0)
agg_df = agg_df[agg_df.diagnostic == 1]

# Applying diagnostic superclass
Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_diagnostic)


# Saving the data

# Waveforms
numpy.savetxt('waveforms.csv', X, delimiter=',')

# Annotations
Y['diagnostic_superclass'].to_csv('annotations.csv')

print("Done!")
