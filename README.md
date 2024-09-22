# Guanto Aptico - Conversione del Parlato in Vibrazioni

## Descrizione del progetto
Questo progetto consiste nella creazione di un **guanto aptico** che converte il parlato umano in sequenze di vibrazioni. Utilizzando un **Raspberry Pi Zero 2W**, il sistema riceve input vocale tramite un microfono e traduce le parole in segnali tattili, attivando motori aptici in base alle lettere riconosciute.

Il sistema è stato progettato per persone con disabilità sensoriali (sordi e ciechi) che possono percepire vibrazioni specifiche associate a ogni lettera dell'alfabeto italiano.

## Struttura del progetto

Il progetto è composto dai seguenti file principali:

- **main.py**: Lo script Python che gestisce il riconoscimento vocale e l'attivazione dei motori aptici.
- **setup.sh**: script shell per configurare il sistema, installare le dipendenze necessarie, e configurare automaticamente la connessione Wi-Fi.
- **requirements.txt**: Elenco delle dipendenze Python necessarie per il funzionamento del progetto.
- **README.md**: Questo file, che contiene informazioni su come navigare e utilizzare il progetto.

## Prerequisiti

### Hardware
- **Raspberry Pi Zero 2W**
- **Microfono USB Push-to-Talk**
- **Motori aptici**

### Software
- **Raspberry Pi OS Lite** o un altro sistema operativo compatibile con Raspberry Pi.
- **Python 3.7+**

# Dipendenze
Le dipendenze sono elencate nel file requirements.txt. 


# Alcune possibili estensioni del progetto includono:

Potenziometro: Regolazione della velocità delle vibrazioni.
Schermo LCD: Visualizzazione del testo riconosciuto in tempo reale.
Microfono wireless: Sostituzione del microfono USB con un microfono wireless per maggiore flessibilità.

# Autori

**Progetto, Sviluppo Software e Documentazioni**: Kenneth Boldrini
**Ricerca Hardware, Elettrotecnica ed Assemblaggio**: Alessio Capenti

# Licenza
This repository is licensed. See the [LICENSE](./LICENSE) file for more details.
