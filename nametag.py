from PIL import Image, ImageFont, ImageDraw
from tqdm import tqdm
import pandas as pd
import os

namesize = 280
jobsize = 55
schoolsize = 60

smallname = 'BaronChang'
smallername = 'KHAIRUL AMMAR HAKIMI'

def eboldfont(fontsize=50):
  ttf = './Pretendard-ExtraBold.ttf'
  return ImageFont.truetype(font=ttf, size=fontsize)
def boldfont(fontsize=50):
  ttf = './Pretendard-Bold.ttf'
  return ImageFont.truetype(font=ttf, size=fontsize)
def mediumfont(fontsize=50):
  ttf = './Pretendard-Medium.ttf'
  return ImageFont.truetype(font=ttf, size=fontsize)

print('\nMaking members name tag..\n')
members = pd.read_excel('./LOUNGE23.xlsx', engine='openpyxl', sheet_name='LOUNGE23')

if os.path.exists('./output') == False:
  os.mkdir('./output')

for i in tqdm(range(len(members))):
  target_img = Image.open("./nametag.png")
  width, height = target_img.size

  out_img = ImageDraw.Draw(target_img)

  _, _, nw, nh = out_img.textbbox(xy=(0,0), text=members['이름'][i], font=eboldfont(fontsize=namesize if (members['이름'][i] != smallname and members['이름'][i] != smallername) else (namesize - 80 if members['이름'][i] == smallname else namesize - 180)))
  out_img.text(xy=((width-nw)/2, 650 if (members['이름'][i] != smallname and members['이름'][i] != smallername) else (680 if members['이름'][i] == smallname else 750)), text=members['이름'][i], fill=(255,255,255), font=eboldfont(fontsize=namesize if (members['이름'][i] != smallname and members['이름'][i] != smallername) else (namesize - 80 if members['이름'][i] == smallname else namesize - 180)))

  _, _, jw, jh = out_img.textbbox(xy=(0,0), text=members['직무'][i], font=mediumfont(fontsize=jobsize))
  out_img.text(xy=((width-jw)/2, 1014), text=members['직무'][i], fill=(255,255,255), font=mediumfont(fontsize=jobsize))

  _, _, sw, sh = out_img.textbbox(xy=(0,0), text=members['학교'][i], font=boldfont(fontsize=schoolsize))
  out_img.text(xy=((width-sw)/2, 1092), text=members['학교'][i], fill=(255,255,255), font=boldfont(fontsize=schoolsize))

  target_img.save('./output/{0}.png'.format(members['이름'][i]))


print('\n\nMaking Staff\'s name tag..\n')
staffs = pd.read_excel('./LOUNGE23.xlsx', engine='openpyxl', sheet_name='Staff')

if os.path.exists('./staff') == False:
  os.mkdir('./staff')

for i in tqdm(range(len(staffs))):
  target_img = Image.open("./staff.png")
  width, height = target_img.size

  out_img = ImageDraw.Draw(target_img)

  _, _, nw, nh = out_img.textbbox(xy=(0,0), text=staffs['이름'][i], font=eboldfont(fontsize=namesize))
  out_img.text(xy=((width-nw)/2, 650), text=staffs['이름'][i], fill=(0,0,0), font=eboldfont(fontsize=namesize))

  _, _, jw, jh = out_img.textbbox(xy=(0,0), text=staffs['직무'][i], font=mediumfont(fontsize=jobsize))
  out_img.text(xy=((width-jw)/2, 650+nh+70), text=staffs['직무'][i], fill=(0,0,0), font=mediumfont(fontsize=jobsize))

  _, _, sw, sh = out_img.textbbox(xy=(0,0), text=staffs['학교'][i], font=boldfont(fontsize=schoolsize))
  out_img.text(xy=((width-sw)/2, 650+nh+70+jh+20), text=staffs['학교'][i], fill=(0,0,0), font=boldfont(fontsize=schoolsize))

  target_img.save('./staff/{0}.png'.format(staffs['이름'][i]))
