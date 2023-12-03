import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr

class VoiceToCode:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice-to-Code")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.record_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.is_recording = False
        self.recording_thread = None

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
            self.record_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.recording_thread.join()

    def record_text(self):
        r = sr.Recognizer()
        while self.is_recording:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    if text == 'start print':
                        self.text_area.insert(tk.END, "print(\"")
                    elif text == 'stop print':
                        self.text_area.insert(tk.END, "\")")
                    elif text == 'new line':
                        self.text_area.insert(tk.END, "\n#\n")
                    else:
                        self.text_area.insert(tk.END, text + " ")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceToCode(root)
    root.mainloop()
