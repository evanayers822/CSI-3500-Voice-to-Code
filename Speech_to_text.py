import os
import speech_recognition as sr

# Initializing the recognizer
r = sr.Recognizer()

file = "output.txt"

def record_text():
    # while loop in case of errors

    while 1:
        try:

            # use the microphone as source for input
            with sr.Microphone() as source2:

                # prepare recognizer to recieve input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the users input
                audio2 = r.listen(source2)

                # Using Google to recognize the audio
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
            return ""  # Return an empty string in case of an unknown value error

def output_text(text, file):
    f = open("./files/" + file, 'a')
    f.write(text)
    f.write("\n")
    f.close()
    return

def undo_text(file):
    f = open("./files/" + file, 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    f.writelines(lines[:-1])
    f.close()
    return

print("Welcome to Voice-to-Code!\nSay \"help\" for a list of commands.\nDefault file = files/output.txt\n" +
      "Begin speaking...")
print(">", end="")
while (1):
    text = record_text()
    print(text)
    if text == "new file": #Create file
        print("Input name for new file: ")
        file = (record_text() + ".txt")
        f = open("./files/" + file, 'a')
        f.close()
        print("New file (" + file + ") created")
        print(">", end="")
    elif text == "open file": #Open existing file (or make new one if non-existant)
        print("Input name of file: ")
        file = (record_text() + ".txt")
        if os.path.isfile("./files/" + file):
            print("File " + file + " opened")
            print(">", end="")
        else:
            print("File " + file + " does not exist. \nWould you like create this file? ('yes' to create)")
            if record_text() == "yes" or "Yes":
                f = open("./files/" + file, 'a')
                f.close()
                print("New file (" + file + ") created")
                print(">", end="")
            else:
                print("No file created")
                print(">", end="")
    elif text == "delete file": #Delete file
        print("Input name of file: ")
        file = (record_text() + ".txt")
        if os.path.isfile("./files/" + file):
            print("Are you sure you would like to delete " + file + "? (Say 'yes' to confirm)")
            if record_text() == "yes" or "Yes":
                os.remove("./files/" + file)
                print("File " + file + " deleted. Opened output.txt")
                file = "output.txt"
                print(">", end="")
            else:
                file = "output.txt"
                print("No file deleted. Opened output.txt")
                print(">", end="")
        else:
            file = "output.txt"
            print("File " + file + " does not exist. Opened output.txt")
            print(">", end="")
    elif text == "undo text": #Delete last line written
        undo_text(file)
        print("Deleted last line of " + file)
        print(">", end="")
    elif text == "help":
        print("Here are the list of vocal commands:\n'help' - Display this list of commands\n" +
              "'new file' - create a txt file\n'open file' - open existing file\n" +
              "'delete file' - delete text file\n'undo text' - delete last line of current opened file")
        print(">", end="")
    else: #Write text to current file
        if text == "":
            print("Wrote nothing")
            print(">", end="")
        else:
            output_text(text, file)
            print("Wrote text to " + file)
            print(">", end="")
