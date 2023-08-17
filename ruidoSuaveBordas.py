# Autor do código original: Hemerson Pistori (pistori@ucdb.br)
# Alterado por Bruno Machado Ferreira e Ernani Neto para a atividade de Ruídos no Classroom
#
# Exemplo de uso:
# $ python ruidoSuaveBordas.py -i exemplo.jpg -r poisson -pr 20 -s mediana -ps 200 -b robert


# Bibliotecas utilizadas
from argparse import ArgumentParser
from skimage import io
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte, random_noise
from skimage import data
from skimage import filters
import cv2
import numpy as np
import cv2 as cv
from scipy import ndimage
from matplotlib import pyplot as plt
import os


# Lê os parâmetros passados na linha de comando
parser = ArgumentParser()
parser.add_argument("-i", "--imagem", default="exemplo.jpg",
                    help="Imagem a ser processada")
parser.add_argument("-r", "--ruido", default="poisson",
                    help="Tipo de ruído. Pode ser gaussian, speckle e poisson")
parser.add_argument("-pr", "--pruido", default=20,type=int,
                    help="Parâmetro do ruído. Depende do tipo do ruído")
parser.add_argument("-s", "--suavizador", default="mediana",
                    help="Tipo de suavizador. Pode ser mediana, gauss ou bilateral")
parser.add_argument("-ps", "--psuavizador", default=201,type=int,
                    help="Parâmetro do suavizador. Depende do tipo do ruído")
parser.add_argument("-b", "--borda", default="robert",
                    help="Tipo de detector de borda. Pode ser robert, canny ou sobel")
parser.add_argument("-pb", "--pborda", default=5,type=int,
                    help="Parâmetro do detector de borda. Depende do tipo de detector")
parser.add_argument("-ig", "--interface", default="sim",
                    help="Parâmetro do suavizador. Depende do tipo do ruído")

args = parser.parse_args()

# Mostra os parâmetros lidos
print("Executando sequência com")
print("Ruído = ",args.ruido)
print("Suavizador = ",args.suavizador)
print("Imagem  = ",args.imagem)
print("Interface Gráfica = ",args.interface)

# Abre a imagem de entrada
original = io.imread(args.imagem)

# Converte imagem colorida para cinza
cinza = rgb2gray(original)

# Aplica ruído  (Concluído: Ruídos extraídos da lib random_noise)
comruido = random_noise(cinza, mode=args.ruido)

# Aplica suavizações(Concluído: Gauss, Mediana e Bilateral)
suavizada=comruido
if args.suavizador == "gauss":
   tamNucleo = args.psuavizador
   print(tamNucleo)
   suavizada = cv2.GaussianBlur(comruido,(tamNucleo,tamNucleo),cv2.BORDER_DEFAULT)
   
elif args.suavizador == "mediana":
   img = cv2.imread(args.imagem)
   suavizada = cv2.medianBlur(img,-ps)
   
elif args.suavizador == "bilateral":
   img = cv2.imread(args.imagem)
   blur = cv2.bilateralFilter(img,-ps)
   
# Aplica detecção de borda (Concluído: Sobel, Canny e Robert)
borda=suavizada
if args.borda == "sobel":
   borda = filters.sobel(suavizada)
   
elif args.borda == "canny":
   img = cv.imread(args.imagem,0)
   borda = cv.Canny(img,--pborda)
   
elif args.borda == "robert":
   roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
   roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )
  
   img = cv2.imread(args.imagem,0).astype('float64')
   img/=255.0
   vertical = ndimage.convolve( img, roberts_cross_v )
   horizontal = ndimage.convolve( img, roberts_cross_h )
  
   borda = np.sqrt( np.square(horizontal) + np.square(vertical))
   borda*=255
   cv2.imwrite("borda.jpg",borda)
   
# Mostra as imagens finais
if args.interface == "sim":

  fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 4),sharex=False, sharey=False)

  ax = axes.ravel()

  ax[0].imshow(original)
  ax[0].axis('off')
  ax[0].set_title('Original')

  ax[1].imshow(comruido,cmap='gray')
  ax[1].axis('off')
  ax[1].set_title('Com Ruído')

  ax[2].imshow(suavizada,cmap='gray')
  ax[2].axis('off')
  ax[2].set_title('Suavizada')

  ax[3].imshow(borda,cmap='gray')
  ax[3].axis('off')
  ax[3].set_title('Borda')

  fig.tight_layout()

  fig.canvas.manager.set_window_title('Resultados para imagem '+args.imagem)
  plt.show()


# Salva no disco as imagens resultantes, na pasta postprocessing
io.imsave('./postprocessing/'+args.imagem.split('.')[0]+"_ruido.jpg",comruido)
io.imsave('./postprocessing/'+args.imagem.split('.')[0]+"_suavizada.jpg",suavizada)
io.imsave('./postprocessing/'+args.imagem.split('.')[0]+"_borda.jpg",borda)



