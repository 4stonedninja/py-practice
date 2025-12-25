status_code = 200

if status_code == 200:
    print ("Success: Data received")
elif status_code == 404:
    print ("Error: Resourse not found")
else:
    print ("Unknown error occurred")

