import torch
import librosa
import cv2
import mediapipe as mp
import speech_recognition as sr
import transformers
print("PyTorch:", torch.__version__, "CUDA:", torch.cuda.is_available())
print("Librosa:", librosa.__version__)
print("OpenCV:", cv2.__version__)
print("MediaPipe:", mp.__version__)
print("SpeechRecognition:", sr.__version__)
print("Transformers:", transformers.__version__)