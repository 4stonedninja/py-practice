status_code = 200

if status_code == 200:
    print ("success: Data received")
elif status_code == 404:
    print ("Error: ReSourse not found")
else:
    print ("Unknown error occurred")

