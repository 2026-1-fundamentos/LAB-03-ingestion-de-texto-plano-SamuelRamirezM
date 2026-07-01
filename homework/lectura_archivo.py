import glob

def leer_datos(input_folder):
    sequence = []
    files = glob.glob(f"{input_folder}*")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                sequence.append(line)
    return sequence