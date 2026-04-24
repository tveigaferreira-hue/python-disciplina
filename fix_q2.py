import json

path = r'C:\Users\tveig\python-disciplina\Exercícios\16-Medidas_Resumo_2_2026-04-01.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

for cell in d['cells']:
    if cell['id'] == 'c2' and cell['cell_type'] == 'code':
        for i, line in enumerate(cell['source']):
            if 'df_aa = pd.DataFrame(index=aminoacidos)' in line:
                cell['source'][i] = 'df_aa = pd.DataFrame(index=aminoacidos, columns=arquivos_fasta)'
                print(f"Fixed line {i}")
            elif 'contagem[aa] = seq.count(aa)' in line:
                cell['source'][i] = '        contagem.append(seq.count(aa))'
                print(f"Fixed line {i}")
            elif 'contagem = {}' in line:
                cell['source'][i] = '    contagem = []'
                print(f"Fixed line {i}")
        break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)

print("Done!")