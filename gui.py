import os
import textwrap
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import speech_recognition as sr

class VoiceToCode:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice-to-Code")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=100, height=25)
        self.text_area.pack(pady=10)

        self.record_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.info_button = tk.Button(master, text="Info", command=self.display_info)
        self.info_button.pack(pady=10)

        self.is_recording = False
        self.recording_thread = None

        self.stop_requested = False

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.recording_thread = threading.Thread(target=self.record_text)
            self.recording_thread.start()

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.stop_requested = True
            self.record_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def save_text(self, file):
        f = open("./files/" + file, 'r+')
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        f.writelines(self.text_area.get("1.0", tk.END))
        f.close()
        return

    def record_text(self):
        r = sr.Recognizer()
        file = "output.txt"
        fName = file
        while self.is_recording:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)
                    if not self.is_recording or self.stop_requested:
                        break
                    text = r.recognize_google(audio)
                    print(">" + text)
                    if text == 'start print':
                        self.text_area.insert(tk.END, "print(\"")
                        print("Print command started.")
                    elif text == 'stop print':
                        self.text_area.insert(tk.END, "\")")
                        print("Print command ended.")
                    elif text == 'new line':
                        self.text_area.insert(tk.END, "\n")
                        print("New line made.")
                    elif text == 'show shortcuts':
                        self.display_info()
                    elif text == 'open file':
                        self.save_text(fName)
                        print("Input name of file: ")
                        file = (r.recognize_google(r.listen(source)) + ".txt")
                        fName = file
                        if os.path.isfile("./files/" + file):
                            f = open("./files/" + file, 'r')
                            self.text_area.insert(tk.END, f.read())
                            f.close()
                            print("File " + file + " opened")
                        else:
                            print("File " + file + "does not exist. \nWould you like create this file? ('yes' to "
                                                   "create)")
                            if r.recognize_google(r.listen(source)) == "yes" or "Yes":
                                f = open("./files/" + file, 'a')
                                f.close()
                                file = (text + ".txt")
                                print("New file (" + fName + ") created and opened.")
                            else:
                                print("No file created.")
                    elif text == 'delete file':
                        self.save_text(fName)
                        print("Input name of file: ")
                        file = (r.recognize_google(r.listen(source)) + ".txt")
                        fName = file
                        if os.path.isfile("./files/" + file):
                            print("Are you sure you would like to delete " + file + "? (Say 'yes' to confirm)")
                            if r.recognize_google(r.listen(source)) == "yes" or "Yes":
                                os.remove("./files/" + file)
                                f = open("./files/output.txt", 'a')
                                f.close()
                                print("File " + fName + " deleted. Opened output.txt")
                                fName = "output.txt"
                            else:
                                fName = "output.txt"
                                print("No file deleted. Opened output.txt")
                    elif text == 'save file':
                        self.save_text(fName)
                        print("Text saved to " + file)
                    else:
                        if text == '':
                            print("Wrote nothing")
                        else:
                            self.text_area.insert(tk.END, text + " ")
                            print("Wrote text")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            finally:
                self.stop_requested = False
                print("Recording stopped.")
            
    def display_info(self):
        info_text = "Say 'start print' to insert a print statement in the text area\n"\
                    "Say 'stop print' to stop the inserted print statement\n"\
                    "Say 'new line' to go to a new line\n"\
                    "Say 'show shortcuts' to see the avaliable voice shortcuts\n"\
                    "Say 'open file' to open an existing file or create a new one\n"\
                    "Say 'delete file' to delete an existing file\n"\
                    "Say 'save file' to save current text displayed into file"
        tk.messagebox.showinfo("Command Information", info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceToCode(root)
    root.mainloop()
