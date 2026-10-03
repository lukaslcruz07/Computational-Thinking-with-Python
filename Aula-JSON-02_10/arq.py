nome = "./Aula-JSON-02_10/incidente.json"
import json

import json
def carregar_historico():
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON inválido. Confira o arquivo.")

print(carregar_historico())

import json
incidentes = []
for i in range(3):
servico = input("Serviço: ")
status = input("Status: ")
incidente = {
"servico": servico,
"status": status
}
incidentes.append(incidente)
nome = "incidentes.json"
with open(nome, "w", encoding="utf-8") as arq:
json.dump(incidentes, arq, indent=4)