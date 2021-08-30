####################################################################################
# parse_observability_data.py to read event metric json file present inside audit zip
# and frame data according to the visualization need
# Please ensure test script is launched with Administrative privileges.
# Please note that this wrapper is meant and tested for Python 3.6.x(64-bit) version.
# File Name     : parse_observability_data.py
"""
Feature: Observability
"""

import os as _os
import json as _json
import glob as _glob
import zipfile as _zipfile


DCA_INSTALL_DIR = "C:\\Program Files\\Intel\\SUR"
DCA_SYSTEM_DATA_DIR = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Intel\\SUR"

def read_audit_zip_json_content(zip_file, json_file_str):
    """ Function name       : read_audit_zip_json_content
        Description         : Function to get read content of input json file
        Parameters          : zipfile, json_file_str
        Return value        : content dictionary of json file inside zip
    """
    # Get content list of file inside zip file and return
    zipObj = _zipfile.ZipFile(zip_file, 'r')
    file_name_list = [element.filename for element in zipObj.infolist()
                 if json_file_str in element.filename]
    for file_name in file_name_list:
        with zipObj.open(file_name) as target_file:
            file_content = target_file.read().strip()
            __dict__ = _json.loads(file_content)
    return __dict__

def get_latest_analysis_zipfile(customization):
    """ Function name       : get_latest_analysis_zipfile
        Description         : Function to get latest zip file
                            : created after analyze command
        Parameters          : customization, like queencreek etc
        Return value        : latest zip file name
    """
    latest_zip_file = None
    # Find latest analyze zip file and return
    if _glob.glob(_os.path.join(
            DCA_SYSTEM_DATA_DIR, customization, 'collected_data', 'intel*.zip')):
        latest_zip_file = max(_glob.glob(
            _os.path.join(DCA_SYSTEM_DATA_DIR, customization, 'collected_data', 'intel*.zip')),
            key=_os.path.getctime)
    return latest_zip_file

def run():
    _data_dict = {}

    event_metric_json_content = read_audit_zip_json_content(get_latest_analysis_zipfile("QUEENCREEK"), "V8_1_EventMetrics")
    events_data = event_metric_json_content['Events']
    for event in events_data:
        if event['meta']['func_name'] == 'RegisterTask':
            continue

        if event['meta']['func_name'] == 'DoExecute':
            key = event['meta']['name']
        else:
            key = event['meta']['func_name']

        if key not in _data_dict.keys():
            _data_dict.update({key: {}})

        _data_dict[key][event['instance']] = event['ts']
    return _data_dict

if __name__ == '__main__':
    _dict = run()

    for key, value in _dict.items():
        print(f'%{{"event" => "{key}", "start" => {value["enter"]}, "end" => {value["leave"]}}},')
