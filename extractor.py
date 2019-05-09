import io
import pyocr
import pyocr.builders
import re
import urllib.request

from PIL import Image as PI
from trello import TrelloClient
from urllib.request import urlopen
from wand.image import Image


TOOL = pyocr.get_available_tools()[0]
LANG = TOOL.get_available_languages()[1]


def extract_infos_from_pdf(pdf_url):
    image_pdf = Image(file=urlopen(pdf_url), resolution=300)
    image_jpeg = image_pdf.convert('jpeg')
    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    final_text = []
    for img in req_image:
        txt = TOOL.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=LANG,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    email = re.search("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", final_text[0])
    raw_tel = re.search(
        "\([0-9]{2}\) (?:9[0-9]{1}|[1-5]{1})[0-9]{3}-[0-9]{4}", final_text[0])[0]
    numbers_list = re.findall(r'\d+', raw_tel)
    tel = '55' + ''.join(numbers_list)
    full_name = re.findall(r'Nome: (.+)', final_text[0])[0].split()[0]
    insurer = re.findall('Tipo: ([^\W\d_]+)', final_text[0])[0]
    return {'email': email.group(),
            'tel': ''.join([d for d in re.findall(r'\d+', tel)]),
            'full_name': full_name,
            'insurer': insurer}
