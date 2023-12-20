from PIL import Image, ImageFont, ImageDraw

def eboldfont(fontsize=50):
	ttf = './Pretendard-ExtraBold.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)
def boldfont(fontsize=50):
	ttf = './Pretendard-Bold.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)
def mediumfont(fontsize=50):
	ttf = './Pretendard-Medium.ttf'
	return ImageFont.truetype(font=ttf, size=fontsize)

namesize = 280
jobsize = 55
schoolsize = 60

target_img = Image.open("./nametag.png")
width, height = target_img.size

out_img = ImageDraw.Draw(target_img)

_, _, nw, nh = out_img.textbbox(xy=(0,0), text='주자훈', font=eboldfont(fontsize=namesize))
out_img.text(xy=((width-nw)/2, 650), text='주자훈', fill=(255,255,255), font=eboldfont(fontsize=namesize))

_, _, jw, jh = out_img.textbbox(xy=(0,0), text='FE-DEVELOPER', font=mediumfont(fontsize=jobsize))
out_img.text(xy=((width-jw)/2, 650+nh+70), text='FE-DEVELOPER', fill=(255,255,255), font=mediumfont(fontsize=jobsize))

_, _, sw, sh = out_img.textbbox(xy=(0,0), text='한국디지털미디어고등학교', font=boldfont(fontsize=schoolsize))
out_img.text(xy=((width-sw)/2, 650+nh+70+jh+20), text='한국디지털미디어고등학교', fill=(255,255,255), font=boldfont(fontsize=schoolsize))

target_img.save('./result.png')
  