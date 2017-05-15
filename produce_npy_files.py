import glob
import pickle
import numpy as np

for pickled_file in glob.glob('*.p'):
    print('pickled_file:', pickled_file)
    with open(pickled_file, 'rb') as input_file:
        numpy_data = pickle.load(input_file, encoding='latin1')
        print('numpy_data.shape:', numpy_data.shape)
        np.save(pickled_file.split('.')[0], arr=numpy_data,
                allow_pickle=False)
