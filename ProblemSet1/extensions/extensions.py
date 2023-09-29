name = input(str("File name: ")).lower()

if ".gif" in name:
    print("image/gif")

elif ".png" in name:
    print("image/png")

elif ".jpeg"in name:
    print("image/jpeg")

elif  ".jpg" in name:
    print("image/jpeg")

elif ".zip" in name:
    print("application/zip")

elif ".pdf" in name:
    print("application/pdf")

elif ".txt" in name:
    print("text/plain")

else:
    print("application/octet-stream")
