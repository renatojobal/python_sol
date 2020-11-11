import pandas as pd  


# Lista de estudiantes colaboradores, periodo 2020-2021


colaborador_2020 = {}
colaborador_2020["1"] = {"Nombre":"Jose", "Email:": "jmabad2@utpl.edu.ec"}
colaborador_2020["1"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["2"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["3"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["4"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["5"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["6"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["7"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["8"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["9"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["10"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["11"] = {"Nombre":"...", "Email:": "..."}
colaborador_2020["12"] = {"Nombre":"...", "Email:": "..."}

df = pd.DataFrame.from_dict(colaborador_2020, orient='index')
print(df)