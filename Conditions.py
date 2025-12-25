status_code = 200

if status_code == 200:
    print ("sucess: Data received")
elif status_code == 404:
    print ("error: Recourse not found")
else:
    print ("unknown error occurred")

