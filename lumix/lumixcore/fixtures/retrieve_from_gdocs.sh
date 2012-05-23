#!/bin/bash

wget "https://docs.google.com/spreadsheet/pub?key=0Al-75kwoq2dwdHI0RzNreFVoRmVfTk5QeGVUcnhXT0E&single=true&gid=1&range=A2%3AO&output=csv" -O os2011.csv
wget "https://docs.google.com/spreadsheet/pub?key=0ArMoGLD8vGVxdDBqMHF2U1BGZDUzOU1ORUc3cEdRWmc&single=true&gid=0&range=A2%3AO&output=csv" -O os2012.csv
python csv_to_json.py