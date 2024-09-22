#!/bin/bash

WPA_SUPPLICANT_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"

# Configurazione della connessione Wi-Fi
echo "Configurazione della connessione Wi-Fi..."
SSID="personal-hotspot"  
PASSWORD="password" 

# Verifica se il file wpa_supplicant.conf esiste e fai un backup
if [ -f "$WPA_SUPPLICANT_FILE" ]; then
    echo "File wpa_supplicant.conf esistente. Creazione di un backup."
    sudo cp $WPA_SUPPLICANT_FILE "${WPA_SUPPLICANT_FILE}.bak"
fi

sudo bash -c "cat > $WPA_SUPPLICANT_FILE <<EOF
country=IT  # Imposta il paese
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid=\"$SSID\"
    psk=\"$PASSWORD\"
    key_mgmt=WPA-PSK
}
EOF"
if [ $? -ne 0 ]; then
    echo "Errore durante la configurazione del Wi-Fi."
    read -p "Premi invio per uscire..."
    exit 1
fi

echo "Wi-Fi configurato con successo."

# Aggiorna i pacchetti di sistema e installa PyAudio e dipendenze di sistema
echo "Updating system packages and installing PyAudio dependencies..."
sudo apt-get update
# Installa Python3 e pip3 se non sono già presenti
sudo apt-get install -y python3 python3-pip > /dev/null 2>&1
# Installa PyAudio e le sue dipendenze di sistema
sudo apt-get install -y python3-pyaudio portaudio19-dev > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error during system dependencies installation (PyAudio)."
    read -p "Press enter to exit..."
    exit 1
fi

# Aggiorna pip e installa le dipendenze globali
echo "Installing Python dependencies globally..."
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip3 install -r requirements.txt > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error during dependency setup."
    read -p "Press enter to exit..."
    exit 1
fi

# Scarica e decomprimi il modello di Vosk
echo "Scaricando il modello di Vosk per il riconoscimento vocale offline..."
wget https://alphacephei.com/vosk/models/vosk-model-it-0.22.zip
unzip vosk-model-it-0.22.zip -d vosk-model
if [ $? -ne 0 ]; then
    echo "Errore durante il download o la decompressione del modello Vosk."
    read -p "Premi invio per uscire..."
    exit 1
fi

echo "Modello di Vosk scaricato e configurato con successo."

echo "Setup completed successfully."
