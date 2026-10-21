from pathlib import Path
import shutil

pasta_do_programa = Path(__file__).parent
pasta_teste = pasta_do_programa / "pasta_teste"
pasta_teste.mkdir(exist_ok=True)


arquivos_teste = [
    "foto.jpg",
    "documento.pdf",
    "video.mp4",
    "anotacoes.txt",
    "programa.py",
    "arquivo_desconhecido.xyz",
]

for nome in arquivos_teste:
    arquivo = pasta_teste / nome

    if not arquivo.exists():
        arquivo.write_text("Arquivo criado para teste.", encoding="utf-8")


categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Codigos": [".py", ".html", ".css", ".js"],
}


for arquivo in pasta_teste.iterdir():
    if arquivo.is_dir():
        continue

    pasta_destino = "Outros"

    for categoria, extensoes in categorias.items():
        if arquivo.suffix.lower() in extensoes:
            pasta_destino = categoria
            break

    destino = pasta_teste / pasta_destino
    destino.mkdir(exist_ok=True)

    novo_caminho = destino / arquivo.name

    if not novo_caminho.exists():
        shutil.move(str(arquivo), str(novo_caminho))
        print(f"{arquivo.name} movido para {pasta_destino}")


print("\nOrganização concluída!")
print(f"Confira a pasta: {pasta_teste}")
