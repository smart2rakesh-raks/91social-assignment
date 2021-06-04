

import json 
     
dictionary ={ 
  "id": "04", 
  "name": "sunil", 
  "depatment": "HR"
}

d = {k: v for k,v in sorted(dictionary.items())}
json_object = json.dumps(d, indent =4) 
print(json_object)

