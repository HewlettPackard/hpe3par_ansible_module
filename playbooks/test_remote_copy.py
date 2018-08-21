from hpe3par_sdk import client
#from hpe3parclient import client
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
storage_system_ip_1 = '192.168.67.7'
wsapi_url_1 = 'https://%s:8080/api/v1' % storage_system_ip_1
storage_system_ip_2 = '192.168.67.5'
wsapi_url_2 = 'https://%s:8080/api/v1' % storage_system_ip_2

client_obj_1 = client.HPE3ParClient(wsapi_url_1)
client_obj_2 = client.HPE3ParClient(wsapi_url_2)

client_obj_1.login('3paradm', '3pardata')
client_obj_2.login('3paradm', '3pardata')

client_obj_1.createVolume('demo_volume_1', 'FC_r1', 1024)
client_obj_2.createVolume('demo_volume_1', 'FC_r1', 1024)
client_obj_1.createVolume('demo_volume_2', 'FC_r1', 1024)
client_obj_2.createVolume('demo_volume_2', 'FC_r1', 1024)


client_obj_1.createRemoteCopyGroup('farhan_rcg', [{'targetName': 'CSSOS-SSA04','mode': 1}])
client_obj_1.addVolumeToRemoteCopyGroup('farhan_rcg', 'demo_volume_1', [{"targetName": "CSSOS-SSA04", "secVolumeName": "demo_volume_1"}], True)
client_obj_1.addVolumeToRemoteCopyGroup('farhan_rcg', 'demo_volume_2', [{"targetName": "CSSOS-SSA04", "secVolumeName": "demo_volume_2"}], True)


#client_obj.removeVolumeFromRemoteCopyGroup('farhan_rcg', 'rcp_vol1')
#print client_obj.getRemoteCopyGroupVolume('farhan_rcg', 'rcp_vol1').localVolumeName
#print client_obj.getRemoteCopyGroupVolume('farhan_rcg', 'rcp_vol1')
