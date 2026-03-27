import os
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def selecionar_imagem():
    """Retorna o caminho da imagem selecionada pelo usuário."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    base = os.path.dirname(os.path.abspath(__file__))
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        initialdir=base,
        filetypes=[
            ("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
            ("Todos os arquivos", "*.*")
        ]
    )

    root.destroy()
    return caminho


def mostrar_imagem(caminho):
    if not caminho or not os.path.isfile(caminho):
        print("Arquivo inválido ou não selecionado.")
        return

    img = cv2.imread(caminho)
    if img is None:
        print("Falha ao carregar imagem (formato não suportado ou arquivo corrompido).")
        return

    # Exibir dimensões da imagem
    altura, largura, canais = img.shape
    print("Dimensões da imagem:")
    print(f"Altura: {altura} pixels")
    print(f"Largura: {largura} pixels")
    print(f"Canais: {canais}")

    # Exibir imagem
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(os.path.basename(caminho))
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    print("Selecionador simples de imagem")
    caminho = selecionar_imagem()
    if not caminho:
        print("Nenhuma imagem selecionada.")
    else:
        mostrar_imagem(caminho)