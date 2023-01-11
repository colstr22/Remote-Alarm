import sys
import simpleaudio
import socket

 
if len(sys.argv) != 2:
    print("To use this tool, you need to pass in the filepath of the target and the IP address of the caller.")
    sys.exit()
 
# Arguments passed
# ============================= Find File ========================================
path = sys.argv[0]
print(f"Sound Path : {path}")
print("Searching for file now ...")
try:
    file = simpleaudio.WaveObject.from_wave_file()
except:
    print("Unable to find sound file.")
print("Sound file located")
# ============================== Setup Listener ==================================
print(f"Caller IP : {sys.argv[1]}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())                           
port = 9999
s.bind((host, port))
# ============================== Listen ==========================================
s.listen(1)
print(f"Listening for a connection on {host}:{port}")
while True:
    client, address = s.accept()
    print(f'Got a connection from {address}')
    data = client.recv(1024)
    if data:
        break()
# ============================== Play Sound ======================================
play_sound = file.play()
play_sound.wait_done()
s.close()
