from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
import easyocr
from PIL import Image
import io
import numpy as np
import shutil
import os

router = APIRouter()

# Inicializa o leitor EasyOCR para o idioma português
reader = easyocr.Reader(['pt'])

# Define o diretório onde as imagens serão salvas
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_image(image: Image.Image, color: str) -> str:
    if image.mode != 'RGB':
        image = image.convert('RGB')

    file_path = os.path.join(UPLOAD_DIR, f"imagem_{color}.jpg")
    image.save(file_path, format='JPEG')
    return file_path

def convert_to_color(image: Image.Image, color: str) -> Image.Image:
    img_array = np.array(image)
    if color == 'red':
        mask = np.zeros_like(img_array)
        mask[..., 0] = img_array[..., 0]  # Red
    elif color == 'green':
        mask = np.zeros_like(img_array)
        mask[..., 1] = img_array[..., 1]  # Green
    elif color == 'blue':
        mask = np.zeros_like(img_array)
        mask[..., 2] = img_array[..., 2]  # Blue
    else:
        raise ValueError("Color must be 'red', 'green', or 'blue'")
    colored_img_array = np.where(mask > 0, mask, 0)
    return Image.fromarray(colored_img_array)

@router.post("/verifica_documento/")
async def verifica_documento(imagem: UploadFile = File(...)):
    # Lê a imagem enviada
    conteudo_imagem = await imagem.read()
    
    # Converte o conteúdo da imagem em um objeto PIL Image
    img = Image.open(io.BytesIO(conteudo_imagem))
    
    # Converte a imagem para preto e branco
    img_preto_branco = img.convert('L')
    
    # Converte a imagem para um array numpy
    img_array = np.array(img_preto_branco)
    
    # Realiza OCR na imagem em preto e branco
    resultados = reader.readtext(img_array)
    
    # Cria uma resposta com o texto extraído
    textos_extraidos = [{"texto": resultado[1], "confiança": resultado[2]} for resultado in resultados]
    
    # Salva a imagem em preto e branco
    img_path_preto_branco = save_image(img_preto_branco, 'preto_branco')
    
    # Gera e salva imagens com cores isoladas
    img_verde = convert_to_color(img, 'green')
    img_vermelho = convert_to_color(img, 'red')
    img_azul = convert_to_color(img, 'blue')
    
    img_path_verde = save_image(img_verde, 'verde')
    img_path_vermelho = save_image(img_vermelho, 'vermelho')
    img_path_azul = save_image(img_azul, 'azul')
    
    # Cria URLs para as imagens
    base_url = "http://localhost:8000"  # Ajuste para o URL base do seu servidor
    image_urls = {
        "imagem_preto_branco": f"{base_url}/files/{os.path.basename(img_path_preto_branco)}",
        "imagem_verde": f"{base_url}/files/{os.path.basename(img_path_verde)}",
        "imagem_vermelho": f"{base_url}/files/{os.path.basename(img_path_vermelho)}",
        "imagem_azul": f"{base_url}/files/{os.path.basename(img_path_azul)}",
    }
    
    return JSONResponse(content={
        "textos_extraidos": textos_extraidos,
        "imagens": image_urls
    })

@router.get("/files/{filename}")
async def get_image(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return StreamingResponse(open(file_path, "rb"), media_type="image/jpeg")
    return JSONResponse(content={"error": "File not found"}, status_code=404)




