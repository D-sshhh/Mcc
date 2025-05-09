import xarray as xr
import numpy as np
import os
import sys
from netCDF4 import Dataset
# 读取两个NetCDF文件

current_dir = os.getcwd()  # 返回当前工作目录的绝对路径（字符串）
print(f"当前路径: {current_dir}")

dir0=current_dir + '/fore202302_benchmark'+  '/ocn/hist/'
dir1=current_dir + '/fore202302_1'+ '/ocn/hist/'

print(dir0)
print(dir1)

with Dataset(dir0 + 'fore202302_benchmark.pop.h.nday1.2023-03-01.nc','r') as fin:
  eta1=fin.variables['SST'][:]
  print(eta1[1,0:200,0:100])
  print("============================")
with Dataset(dir1 + 'fore202302_1.pop.h.nday1.2023-03-01.nc','r') as fin:
  eta2=fin.variables['SST'][:]
  print(eta2[1,0:200,0:100])
  print("============================")
#print('MAE:', np.nanmean(np.abs(eta1-eta2)))

# 计算RMSE
def calculate_rmse(obs, sim):
    # 计算均方根误差（忽略NaN值）
    squared_error = (obs - sim) ** 2
    mse = squared_error.mean()  # 均方误差
    rmse = np.sqrt(mse)         # 均方根误差
    return rmse

rmse = calculate_rmse(eta1, eta2)
print(f'RMSE:{rmse}')
