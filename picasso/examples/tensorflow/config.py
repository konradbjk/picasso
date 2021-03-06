# Note: By default, Flask doesn't know that this file exists.  If you want
# Flask to load the settings you specify here, you must set the environment
# variable `PICASSO_SETTINGS` to point to this file.  E.g.:
#
#   export PICASSO_SETTINGS=/path/to/examples/tensorflow/config.py
#
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

MODEL_CLS_PATH = os.path.join(base_dir, 'model.py')
MODEL_CLS_NAME = 'TensorflowMNISTModel'
MODEL_LOAD_ARGS = {
    'data_dir': os.path.join(base_dir, 'data-volume'),
    'tf_input_var': 'convolution2d_input_1:0',
    'tf_predict_var': 'Softmax:0',
}
