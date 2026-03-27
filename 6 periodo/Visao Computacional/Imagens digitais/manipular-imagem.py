import os
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def selecionar_imagem():
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


def manipular_imagem(caminho):
    if not caminho or not os.path.isfile(caminho):
        print("Arquivo inválido ou não selecionado.")
        return

    img = cv2.imread(caminho)
    if img is None:
        print("Falha ao carregar imagem.")
        return

    # a) Converter para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mostrar dimensões antes e depois
    print("Imagem original (altura, largura, canais):", img.shape)
    print("Imagem em escala de cinza (altura, largura):", img_gray.shape)

    # b) Exibir imagem em escala de cinza
    plt.imshow(img_gray, cmap='gray')
    plt.title("Imagem em Escala de Cinza")
    plt.axis('off')
    plt.show()

    # c) Explicação
    print("\nExplicação:")
    print("A imagem original possui 3 canais de cor (BGR), ou seja, cada pixel é representado por três valores.")
    print("Ao converter para escala de cinza, a imagem passa a ter apenas 1 canal.")
    print("Assim, cada pixel é representado por um único valor de intensidade (luminosidade).")
    print("Por isso, a estrutura mudou de (altura, largura, 3) para (altura, largura).")


if __name__ == '__main__':
    print("Manipulação de imagem - escala de cinza")
    caminho = selecionar_imagem()

    if not caminho:
        print("Nenhuma imagem selecionada.")
    else:
        manipular_imagem(caminho)