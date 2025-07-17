from mfrc522 import SimpleMFRC522
from signal import pause
reader = SimpleMFRC522()

# try:
while True:
    print("Place your tag near the reader...")
    id, text = reader.read()
    print(f"ID: {id}")
    if id == 1074584027897:
        print("access granted")
    #     print(f"Text: {text}")
    else:
        print("acces denied")

# finally:
#     print("done")
