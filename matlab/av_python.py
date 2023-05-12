import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

#===|ARQUIVO A SER CARREGADO|===%
filename = r'D:\Baja\Eletronica\22\Dados\Setup Susp\2022_04_02\file001.txt'
with open(filename, 'r') as f:
data = f.readlines()

alldata = []
for line in data:
values = line.split()
alldata.append(values)

alldata = np.array(alldata)
counter = alldata[:, 72].astype(int)
rpm = alldata[:, 0].astype(int)
vel = alldata[:, 4].astype(int)
fuel = alldata[:, 8].astype(int)
bat = alldata[:, 11].astype(int)
volante = alldata[:, 14].astype(int)
pedal = alldata[:, 17].astype(int)
acce_x = alldata[:, 20].astype(int)
acce_y = alldata[:, 24].astype(int)
acce_z = alldata[:, 28].astype(int)
gyro_x = alldata[:, 32].astype(int)
gyro_y = alldata[:, 36].astype(int)
gyro_z = alldata[:, 40].astype(int)
magn_x = alldata[:, 44].astype(int)
magn_y = alldata[:, 48].astype(int)
magn_z = alldata[:, 52].astype(int)
gps_lat = alldata[:, 56].astype(int)
gps_lon = alldata[:, 64].astype(int)

#===|Calculos Adicionais|===%
acce_x = (65535 - gyro_x)/1672.0
acce_y = (65535 - gyro_y)/1672.0
acce_z = (65535 - gyro_z)/1672.0
gyro_x = (65535 - gyro_x)/131.0
gyro_y = (65535 - gyro_y)/131.0
gyro_z = (65535 - gyro_z)/131.0

ff = 20
window = np.ones(ff)/ff
rpm = np.convolve(rpm, window, mode='same')
vel = np.convolve(vel, window, mode='same')
fuel = np.convolve(fuel, window5, mode='same')
bat = np.convolve(bat, window5, mode='same')
volante = np.convolve(volante, window, mode='same')
pedal = np.convolve(pedal, window, mode='same')

acce_x = convolve(acce_x, window, mode='same')
acce_y = convolve(acce_y, window, mode='same')
acce_z = convolve(acce_z, window, mode='same')
gyro_x = convolve(gyro_x, window, mode='same')
gyro_y = convolve(gyro_y, window, mode='same')
gyro_z = convolve(gyro_z, window, mode='same')

#===========================%

plt.figure('All Data')
plt.plot(counter)
plt.plot(rpm)
plt.plot(vel)
plt.plot(bat)
plt.plot(volante)
plt.plot(pedal)
plt.plot(acce_x)
plt.plot(acce_y)
plt.plot(acce_z)
plt.plot(gyro_x)
plt.plot(gyro_y)
plt.plot(gyro_z)
plt.plot(magn_x)
plt.plot(magn_y)
plt.plot(magn_z)

plt.figure('GPS')
plt.plot(gps_lon, gps_lat)

plt.figure('AV')
plt.plot(rpm, 'red')
plt.twinx()