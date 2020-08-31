import json

complex_json = {
   "firstName":"John",
   "lastName":"Smith",
   "isAlive":"true",
   "age":27,
   "address":{
      "streetAddress":"21 2nd Street",
      "city":"New York",
      "state":"NY",
      "postalCode":"10021-3100"
   },
   "phoneNumbers":[
      {
         "type":"home",
         "number":"212 555-1234"
      },
      {
         "type":"office",
         "number":"646 555-4567"
      }
   ],
   "children":[

   ],
   "spouse":"null"
}

for key in complex_json.keys():
    print(complex_json[key])
    if isinstance(complex_json[key],list) and complex_json[key]:
       for lkey in complex_json[key]:
          print(lkey)
          if isinstance(lkey, dict) and lkey:
             for lkey1 in lkey.keys():
                print(lkey[lkey1])
