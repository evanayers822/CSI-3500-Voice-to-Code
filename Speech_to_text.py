import speech_recognition as sr

# Initializing the recognizer
r = sr.Recognizer()


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
            print("could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
    return


def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return


def record_text():
    pass


while (1):
    text = record_text()
    output_text(text)

    print("wrote text")
