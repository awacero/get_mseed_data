from get_mseed_data import get_mseed
from get_mseed_data import get_mseed_utils as gmutils
from obspy import UTCDateTime


#mseed_client_id="FDSN"
mseed_client_id = "ARCHIVE"
mseed_server_config_file = "./mseed_server_info.json"

start_time = UTCDateTime("2016-04-16 23:58:00" )
end_time = UTCDateTime("2016-04-17 00:04:00" )

#bref = {"network":"EC", ""}


mseed_server_param = gmutils.read_config_file(mseed_server_config_file)

cliente = get_mseed.choose_service(mseed_server_param[mseed_client_id])

print(cliente)


#data = get_mseed.get_stream(mseed_client_id, cliente, "EC","BREF","","BHZ",start_time,window_size=600)
data = get_mseed.get_stream(mseed_client_id, cliente, "EC","BREF","","BHZ",start_time,end_time=end_time)

print(data)

data.plot()



