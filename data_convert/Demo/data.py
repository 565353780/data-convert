import torch
import numpy as np
import jittor as jt

from data_convert.Method.data import toData

def demo():
    list_data = list(range(100))
    print('list data:', len(list_data), type(list_data[0]))

    np_data = toData(list_data, 'numpy', np.float64)
    print('list->np data:', np_data.shape, np_data.dtype)
    torch_data = toData(list_data, 'torch', torch.float64)
    print('list->torch data:', torch_data.shape, torch_data.dtype)
    jt_data = toData(list_data, 'jittor', jt.float64)
    print('list->jt data:', jt_data.shape, jt_data.dtype)
    return True
