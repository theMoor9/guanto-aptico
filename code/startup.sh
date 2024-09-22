#!/bin/bash

# Verifica del microfono
echo "Checking microphone..."
# Implementa il controllo del microfono


# Esegui il tuo script Python
echo "Running the application..."
python3 main.py
if [ $? -ne 0 ]; then
    echo "Error during application execution."
    read -p "Press enter to exit..."
    exit 1
fi

echo "Application finished successfully."

