#  python code to remove element from json file
import json
def json_method(ele1, ele2):
    o = json.load(open('test_payload.json'))    
    del o['inParams'][ele1]
    del o[ele2]
                      
    open("test_payload_update.json", "w").write(
        json.dumps(o, sort_keys=True, indent=4, separators=(',', ': '))
    )
json_method("appdate","outParams")