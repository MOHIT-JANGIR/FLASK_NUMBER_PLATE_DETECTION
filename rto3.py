import json,requests,xmltodict

def get_vehicle_info(plate_number):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=".format(str(plate_number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    data_final = json.loads(jdata)
    data_print = json.loads(data_final['Vehicle']['vehicleJson'])
    print(data_print)
    return data_print

get_vehicle_info("MH20EE7598")
