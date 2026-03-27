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


def histograma_imagem(caminho):
    if not caminho or not os.path.isfile(caminho):
        print("Arquivo inválido ou não selecionado.")
        return

    img = cv2.imread(caminho)
    if img is None:
        print("Falha ao carregar imagem.")
        return

    # a) Converter para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # b) Gerar histograma
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

    # c) Exibir imagem e histograma
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title("Imagem em Escala de Cinza")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.plot(hist)
    plt.title("Histograma")
    plt.xlabel("Intensidade (0-255)")
    plt.ylabel("Quantidade de pixels")

    plt.show()

    # d) Análise automática simples
    media = img_gray.mean()

    print("\nAnálise do Histograma:")

    if media > 127:
        print("• A imagem tende a ser mais clara.")
    else:
        print("• A imagem tende a ser mais escura.")

    print("• Verifique o gráfico: picos indicam concentração de pixels em determinadas intensidades.")

    if hist.std() > 1000:
        print("• O contraste parece ser alto (distribuição mais espalhada).")
    else:
        print("• O contraste parece ser baixo (valores mais concentrados).")


if __name__ == '__main__':
    print("Histograma de imagem")
    caminho = selecionar_imagem()

    if not caminho:
        print("Nenhuma imagem selecionada.")
    else:
        histograma_imagem(caminho)