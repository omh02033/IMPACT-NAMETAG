from PIL import Image, ImageFont, ImageDraw
from tqdm import tqdm
import pandas as pd

namesize = 280
jobsize = 55
schoolsize = 60

def eboldfont(fontsize=50):
	ttf = './Pretendard-ExtraBold.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)
def boldfont(fontsize=50):
	ttf = './Pretendard-Bold.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)
def mediumfont(fontsize=50):
	ttf = './Pretendard-Medium.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)

df = pd.read_excel('./LOUNGE23.xlsx', engine='openpyxl')

for i in tqdm(range(len(df))):
  target_img = Image.open("./nametag.png")
  width, height = target_img.size

  out_img = ImageDraw.Draw(target_img)

  _, _, nw, nh = out_img.textbbox(xy=(0,0), text=df['이름'][i], font=eboldfont(fontsize=namesize))
  out_img.text(xy=((width-nw)/2, 650), text=df['이름'][i], fill=(255,255,255), font=eboldfont(fontsize=namesize))

  _, _, jw, jh = out_img.textbbox(xy=(0,0), text=df['직무'][i], font=mediumfont(fontsize=jobsize))
  out_img.text(xy=((width-jw)/2, 650+nh+70), text=df['직무'][i], fill=(255,255,255), font=mediumfont(fontsize=jobsize))

  _, _, sw, sh = out_img.textbbox(xy=(0,0), text=df['학교'][i], font=boldfont(fontsize=schoolsize))
  out_img.text(xy=((width-sw)/2, 650+nh+70+jh+20), text=df['학교'][i], fill=(255,255,255), font=boldfont(fontsize=schoolsize))

  target_img.save('./output/{0}.png'.format(df['이름'][i]))
  
