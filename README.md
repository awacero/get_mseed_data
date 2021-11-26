# get_mseed_data

This code allows to choose between different MSEED servers (ARCLINK, SEEDLINK, ARCHIVE, FDSN) and download MSEED data using either end_time or window_size in seconds. 

# Installation

```bash
$ pip install get_mseed_data
```

# How to call it

Define a json file with the information of the servers. Create a dictionary using get_mseed_utils. See the test_get_mseed.py for references. 
