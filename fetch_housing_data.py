import os
import pandas
from six.moves import urllib
import sys
import tarfile

def get_data(data_name):
    root_path = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
    data_path = 'datasets/{}/'.format(data_name)
    data_url = os.path.join(root_path, data_path, '{}.tgz'.format(data_name))
    tgz_path = os.path.join(data_path, '{}.tgz'.format(data_name))
    
    if not os.path.isdir(data_path): #Return true if the data_path refers to an existing directory
        os.makedirs(data_path) 
    urllib.request.urlretrieve(data_url, tgz_path)
    tgz_file = tarfile.open(tgz_path)
    tgz_file.extractall(data_path)
    tgz_file.close()
    
    #assuming .csv file will be extracted from the .tgz file
    csv_path = os.path.join(data_path, '{}.csv'.format(data_name))
    data = pandas.read_csv(csv_path)
    return data
