import cv2
from google.cloud import vision_v1p3beta1 as vision

# Carrega a imagem
imagem = cv2.imread("banner.png")

# Converte a imagem para o formato necessário para a API do Google Cloud Vision
_, encoded_imagem = cv2.imencode('.png', imagem)
imagem_bytes = encoded_imagem.tobytes()

# Cria um cliente da API do Google Cloud Vision
cliente_vision = vision.ImageAnnotatorClient()

# Envia a imagem para a API do Google Cloud Vision para detecção de objetos
resultado = cliente_vision.object_localization(
    image={"content": imagem_bytes})

# Extrai as informações do resultado
objetos = resultado.localized_object_annotations

# Gera o texto alternativo para a imagem
texto_alternativo = "A imagem contém: "
for objeto in objetos:
    texto_alternativo += objeto.name + ", "

# Remove a última vírgula e exibe o texto alternativo gerado
texto_alternativo = texto_alternativo[:-2]
print("Texto alternativo: " + texto_alternativo)
