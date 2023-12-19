from PIL import Image, ImageFont, ImageDraw
from tqdm import tqdm

def boldfont(fontsize=50):
	ttf = './Pretendard-ExtraBold.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)
def mediumfont(fontsize=50):
	ttf = './Pretendard-Medium.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)

import pandas as pd

df = pd.read_excel('./LOUNGE23.xlsx', engine='openpyxl')

for i in tqdm(range(len(df))):
  target_img = Image.open("./nametag.png")
  out_img = ImageDraw.Draw(target_img)
  out_img.text(xy=(550, 270), text=df['이름'][i], fill=(255,255,255), font=boldfont(fontsize=300))
  out_img.text(xy=(100, 777), text=df['직무'][i], fill=(255,255,255), font=boldfont(fontsize=67))
  out_img.text(xy=(100, 887), text=df['학교'][i], fill=(255,255,255), font=mediumfont(fontsize=50))

  target_img.save('./output/{0}.png'.format(df['이름'][i]))
  
