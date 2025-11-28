import os
import subprocess
import re
import json

EXIFTOOL_PATH = r"C:\My way\my path to\exiftool.exe"  # Chemin vers exiftool.exe

def clean_json_string(json_str):
    json_str = re.sub(r',\s*\.', ',', json_str)
    json_str = re.sub(r'\{\s*\.', '{', json_str)
    json_str = re.sub(r'\}\s*\.', '}', json_str)
    json_str = re.sub(r'\[\s*\.', '[', json_str)
    json_str = re.sub(r'\]\s*\.', ']', json_str)
    return json_str

def get_positive_prompt(image_path):
    try:
        result = subprocess.run(
            [EXIFTOOL_PATH, '-parameters', image_path],
            capture_output=True,
            text=True
        )
        for line in result.stdout.splitlines():
            if line.startswith("Parameters"):
                json_raw = line.partition(":")[2].strip()
                json_clean = clean_json_string(json_raw)
                try:
                    data = json.loads(json_clean)
                    prompt = data.get("sui_image_params", {}).get("prompt")
                    return prompt
                except Exception:
                    # fallback regex si JSON mal formé
                    match = re.search(
                        r'"sui_image_params"\s*:\s*\{[^}]*"prompt"\s*:\s*"([^"]+)"',
                        json_clean,
                        re.DOTALL
                    )
                    if match:
                        return match.group(1)
    except Exception:
        pass
    return None

def extract_prompts_from_root(root_folder):
    prompts = []
    for current_path, _, files in os.walk(root_folder):
        for filename in files:
            if filename.lower().endswith('.png'):
                img_path = os.path.join(current_path, filename)
                prompt = get_positive_prompt(img_path)
                if prompt:
                    prompts.append(prompt)
    return prompts

# Utilisation automatique du dossier courant
folder = os.getcwd()
output_txt = "positive_prompts.txt"

all_prompts = extract_prompts_from_root(folder)

with open(output_txt, "w", encoding="utf-8") as fp:
    for prompt in all_prompts:
        fp.write(prompt + "\n")


print(f"Export terminé : {len(all_prompts)} prompts positifs trouvés dans {output_txt} (dossier : {folder})")
