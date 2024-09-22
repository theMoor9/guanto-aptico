import os
import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import json
from vosk import Model, KaldiRecognizer

# Mappatura dei pin GPIO per ogni lettera dell'alfabeto italiano
LETTER_TO_PIN = {
    'a': [21], 'b': [20], 'c': [16], 'd': [12], 'e': [25], 'f': [24], 'g': [23], 'h': [18],
    'i': [26], 'l': [19], 'm': [13], 'n': [6], 'o': [22], 'p': [24, 21, 27],
    'q': [19, 23, 20, 17], 'r': [13, 18, 16], 's': [6, 26, 12],
    't': [22, 5, 25, 11], 'u': [27], 'v': [17], 'z': [11], '+': [5]
}
# specifica il modo di numerazione dei pin BCM (Broadcom SOC Channel)
GPIO.setmode(GPIO.BCM)

# Configurazione dei pin GPIO per i motori aptici
for pin in LETTER_TO_PIN.values():
    for p in pin:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

# Configurazione del riconoscimento vocale
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Carica il modello Vosk
vosk_model_path = "vosk-model"  # Mantieni il percorso in cui hai estratto il modello
model = Model(vosk_model_path)


# Funzione per attivare i motori aptici
def activate_motor_for_letter(letter):
    """Attiva i motori corrispondenti alla lettera."""
    pins = LETTER_TO_PIN.get(letter.lower(), [])
    if pins:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.33)
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.53)

# Funzione per convertire il testo in vibrazioni
def convert_text_to_haptic(text):
    """Converte il testo in segnali aptici, una vibrazione per ogni lettera."""
    for char in text:
        if char.lower() in LETTER_TO_PIN:
            activate_motor_for_letter(char)
        elif char.isspace():
            time.sleep(3.3)

# Funzione per verificare la connessione a Internet
def is_connected():
    try:
        # Ping verso Google per verificare la connessione a Internet
        return os.system("ping -c 1 google.com") == 0
    except Exception:
        return False

# Funzione di ascolto con opzione online/offline
def listen_and_convert():
    """Ascolta tramite il microfono e converte continuamente le frasi in segnali aptici."""
    print("In ascolto continuo...")

    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Registrazione in corso...")
                audio = recognizer.listen(source)

            # Controlla se c'è connessione a Internet
            if is_connected():
                # Usa Google Speech Recognition se c'è connessione
                print("Connessione trovata, utilizzo Google Speech Recognition...")
                text = recognizer.recognize_google(audio, language="it-IT")
            else:
                # Usa Vosk per il riconoscimento offline se non c'è connessione
                print("Nessuna connessione trovata, utilizzo Vosk per il riconoscimento offline...")
                rec = KaldiRecognizer(model, 16000)
                rec.AcceptWaveform(audio.get_wav_data())
                result = rec.Result()
                text = json.loads(result)["text"]

            print(f"Frase rilevata: {text}")
            convert_text_to_haptic(text)
        
        except sr.UnknownValueError:
            print("Non ho capito la frase.")
        except sr.RequestError as e:
            print(f"Errore: {e}")

try:
    listen_and_convert()
except KeyboardInterrupt:
    GPIO.cleanup()