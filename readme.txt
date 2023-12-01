# CSI-3500-Voice-to-Code
CSI 3500's Team 3's project known as Voice-to-Code. We're building a voice recognition application to assist with writing Python code.

# Speech-to-Text Recorder
This Python script utilizes the SpeechRecognition library to convert speech from a microphone into text using Google's speech recognition API. The recognized text is saved to "output.txt" file.

## Prerequisites
Make sure you have the required library installed. You can install it using the following commands:
Windows:
```bash
pip install SpeechRecognition
pip install pyaudio

MacOS:
pip3 install speechrecognition
brew install python3-pyaudio
pip3 install pyaudio

# VoiceToCode GUI
This is a basic graphical user interface (GUI) for speech recognition using Python's tkinter library and the speech_recognition module.

Features
Start Recording: Initiates the speech recognition process using your microphone.
Stop Recording: Stops the ongoing recording and speech recognition.
The recognized text will be displayed in a scrolled text widget in the GUI.

# How it Works
The GUI is built using the tkinter library.
The speech_recognition module is used for speech recognition.
The application captures audio from the microphone, adjusts for ambient noise, and uses Google's speech recognition to convert the audio to text.
The recognized text is displayed in a scrolled text widget.
The GUI provides buttons to start and stop the recording process.

