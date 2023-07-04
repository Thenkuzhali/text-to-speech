 import pyttsx3

try:
    file_name = input("Enter file name:")
    speaker = pyttsx3.init()
    sound = speaker.getProperty('voices')
    speaker.setProperty('voice', sound[1].id)
    speaker.setProperty('rate', 120)
    speaker.setProperty('volume', 1)
    f = open(f"C:\\Users\\ELCOT\\Desktop\\{file_name}", 'r')
    ip = f.read()
    speaker.say(ip)
    speaker.runAndWait()
except:
    print("make sure your file is in the path:\n C:\\Users\\ELCOT\\Desktop")
