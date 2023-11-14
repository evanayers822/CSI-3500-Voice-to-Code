# CSI-3500-Voice-to-Code
CSI 3500's Team 3's project known as Voice-to-Code. We're building a voice recognition application to assist with writing Python code.

# Speech-to-Text Recorder
This Python script utilizes the SpeechRecognition library to convert speech from a microphone into text using Google's speech recognition API. The recognized text is saved to "output.txt" file.

## Prerequisites
Make sure you have the required library installed. You can install it using the following commands:
Windows:
```bash
pip install SpeechRecognition

MacOS:
pip3 install speechrecognition
brew install python3-pyaudio
pip3 install pyaudio

#Usage
Step 1. Run the script.
Step 2. The script will continuously listen to the microphone input.
Step 3. When speech is detected, it will use Google's speech recognition to convert it to text.
Step 4.The recognized text will be appended to the "output.txt" file.
Step 5. The process continues in a loop.
