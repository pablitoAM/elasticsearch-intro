import csv
from datetime import datetime
import json

INPUT_FILE = './data/AccidentesBicicletas_2017.csv'
OUTPUT_FILE = './data/output.json'

FECHA    = "fecha"
HORA     = "hora"
VICTIMAS = "victimas"
DISTRITO = "distrito"
CALLE    = "calle"
NUMERO   = "numero"
TIPO     = "tipo"  

# Create dictionary from row
def toDictionary(row):
    obj = dict()
    obj[FECHA] = cleanDate(row[0].strip())
    obj[HORA] = cleanTime(row[1].strip())
    obj[VICTIMAS] = row[2].strip()
    obj[DISTRITO] = row[3].strip()
    obj[CALLE] = row[4].strip()
    obj[NUMERO] = parseNumber(row[5].strip())
    obj[TIPO] = row[6].strip()
    return obj

# Clean Date
def cleanDate(date):
    return datetime.strptime(date[:10], '%d/%m/%Y').date().isoformat()

def cleanTime(time):
    pattern = '%H:%M'
    obj = time[3:].split('A')
    obj[0] = datetime.strptime(obj[0].strip(), pattern).time().isoformat()
    obj[1] = datetime.strptime(obj[1].strip(), pattern).time().isoformat()
    return obj

def parseNumber(number):
    if not number:
        return 's/n'
    return number

def toJsonFile(data, fileName):
    with open(fileName, 'w+') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

with open(INPUT_FILE, encoding='latin-1') as f: # The source file is encoded with latin-1
    reader = csv.reader(f, delimiter=';')
    next(reader) 
    next(reader) # skip headers
    data = []
    for row in reader:
        data.append(toDictionary(row))
    toJsonFile(data, OUTPUT_FILE)