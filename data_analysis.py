"""
These are my data analysis functions ueed to download and process some temperature time series from Berkeley Earth.
"""

import numpy as np
import requests

def generate_url(location):
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-TAVG-Trend.txt'
    return url
	
def download_data(location):
    url = generate_url(location)
    # Download the content of the URL
    response = requests.get(url)
          
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data

def moving_average(data, window_size):
    "Calculate a moving average over 1D data using the given window size"
    average = np.full(data.size, np.nan)
    half_window = window_size // 2
    for i in range(half_window, data.size - half_window):
        average[i] = np.mean(data[i - half_window : i + half_window])
    return average

def test_moving_avg():
	avg = moving_average(np.ones(1000), 2)
	assert np.all(np.isnan(avg[0:2]))
	assert np.all(np.isnan(avg[-2:]))
	assert np.allclose(avg[2:-2], 1)	
	