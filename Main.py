import http.client
import json
##########Initial Parameters ###########

#conn specifies the rest api url to connect
conn  = http.client.HTTPConnection("twitter.com/api")
url =   "/albums"
restMethod = "POST" 
payload = '{ "Name": "Afican Safari","Reference": "","Country": "Zambia","ISDCode": "+056", "Active": true}'
headers = {
	#Enter the OAuth Token , content-Type
    'authorization':"Bearer LOQNBXMSGuSWCrWYhOVFpKstsA22-lIOfcFcxQ03djnT4IhgWs82sT-_aCR3N9G_oYzf7dTi3e7fhbOjxNbKyV0wkXcXWYceSYclGYUK_Om4XpiivcPH7kwFU8OTZSVJmZuSi_6eBEu67DMw1pzR-TRnfUYuuK0E5bOGE5bGHkJCevarp73fz7mEoEu5N5zDothhwlvA1P5qfX0JwbZIMW34VcsdLtWQr-StXT_z5YUmyHURwrbGMcszg5xe6tgJGynRIKSaLRtjwPouLeUQlPtV-kEglihxKHq0ZB9TnUvfZB2KgtWsY1LaVWK1dxnG0HV__YbakOjdurkQxfFkq20Pe1iSBnRteHQMKt80bqHPyeZkHwQVc",
    'cache-control':"no-cache",
    'content-type': "application/json"
    }
#Specify the Folder to generate output test cases
outputFile = open("/Users/Downloads/testcases.txt" , "w")

#######################################

def main():
    ProperInput()
    if restMethod not in ['GET']:
        NoneInput()
        EmptyInput()
        EmptyObjectInput()
        EmptyArrayInput()
        makeJsonValueNull()

def ProperInput():
    conn.request(restMethod,url,payload ,headers)
    res = conn.getresponse()
    #print("\nTest Case with Correct Input")
    #print(res.status)
    data = res.read()
    #print(data.decode("utf-8"))
    outputFile.write("\n\nTest Case with Correct Input")
    outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))

def NoneInput():
    payload = None
    conn.request(restMethod,url,payload ,headers)
    res = conn.getresponse()
    #print("\nTest Case with Null Input")
    #print(res.status)
    data = res.read()
    #print(data.decode("utf-8"))
    outputFile.write("\n\nTest Case with Null Input")
    outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))

def EmptyInput():
    payload = ""
    conn.request(restMethod,url,payload ,headers)
    res = conn.getresponse()
    #print("\nTest Case with Empty String Input")
    #print(res.status)
    data = res.read()
    #print(data.decode("utf-8"))
    outputFile.write("\n\nTest Case with Empty String  Input")
    outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))

def EmptyObjectInput():
    payload = {}
    conn.request(restMethod,url,payload ,headers)
    res = conn.getresponse()
    #print("\nTest Case with Empty Object {} Input")
    #print(res.status)
    data = res.read()
    #print(data.decode("utf-8"))
    outputFile.write("\n\nTest Case with Empty Object {} Input")
    outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))

def EmptyArrayInput():
    payload = []
    conn.request(restMethod,url,payload ,headers)
    res = conn.getresponse()
    #print("\nTest Case with Empty Array [] Input")
    #print(res.status)
    data = res.read()
    #print(data.decode("utf-8"))
    outputFile.write("\n\nTest Case with Empty Array [] Input")
    outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))



def makeJsonValueNull():
    i = 0
    inputJson =  json.loads(payload)
    for attrribute , value in  inputJson.items():
        i += 1
        testJson =  dict()
        testJson[attrribute] = value
        testJson = json.dumps(testJson)
        #print("Test Case " + str(i) + " While Removing Each JSON KEY Values")
        #print("\n Input Json: " +str(testJson))
        conn.request(restMethod , url , testJson ,headers)
        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
        outputFile.write("\n\nTest Case " + str(i) + " While Removing Each JSON KEY Values")
        outputFile.write("\n Input Json: " +str(testJson))
        outputFile.write("\n"+ "HTTP Response: "+str(res.status) +"\n"+ str(data.decode("utf-8")))





if __name__ == '__main__':
    #execute only if run as script
    main()
