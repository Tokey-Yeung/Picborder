# -*- coding: UTF-8 -*-
import exifread
import time
from PIL import Image, ImageFont, ImageDraw


def get_exif(file_path):  # 获取照片的拍摄信息
    f = open(file_path, 'rb')
    tags = exifread.process_file(f, details=False)
    Make = tags.get('Image Make')  # 获取相机品牌
    Model = str(tags.get('Image Model')).rstrip()  # 获取相机型号
    DateTime = tags.get('Image DateTime')  # 获取拍摄时间
    DateTime = time.strftime("%Y-%m-%d", time.strptime(str(DateTime), "%Y:%m:%d %H:%M:%S"))  # 将拍摄时间转换为标准时间格式
    Artist = tags.get('Image Artist')  # 获取拍摄者
    ExposureTime = tags.get('EXIF ExposureTime')  # 获取曝光时间
    shutter=eval(str(tags.get('EXIF ExposureTime')))    #将大于1s的快门变成小数显示
    if shutter>=1:
        ExposureTime=str(shutter)
    else:
        ExposureTime = tags.get('EXIF ExposureTime')
    Number = str(eval(str(tags.get('EXIF FNumber'))))  # 获取光圈,因其和曝光补偿显示为x/y形式，需要将其转换为数字
    FocalLength = tags.get('EXIF FocalLength')  # 获取焦距
    ExposureBiasValue = str(eval(str(tags.get('EXIF ExposureBiasValue'))))  # 获取曝光补偿
    LensModel = tags.get('EXIF LensModel')  # 获取镜头型号
    if LensModel==None:
        LensModel = "曝光补偿:{}".format(ExposureBiasValue)
    ISO = tags.get('EXIF ISOSpeedRatings')  # 获取ISO
    exif_dict = {'品牌': Make, '型号': Model, '拍摄时间': DateTime, '拍摄者': Artist, '曝光时间': ExposureTime, '光圈': Number,
                 '焦距': FocalLength, '镜头型号': LensModel, 'ISO': ISO, '曝光补偿': ExposureBiasValue}
    f.close()
    return exif_dict


def image_borde(exif_dict, qlity,file_path,outputname):  #outputname为输出的目录+文件名
    # 给图片加边框，并添加信息
    img_ori = Image.open(file_path)
    w = img_ori.size[0]
    h = img_ori.size[1]
    orange_size = w     #orange_size和blankcoefficient两参数一起控制空白大小
    scale = 0.58 * (w * h) / (3500 * 6000)      #缩放比例，原图像素除以参考图像素而来，0.58为logo为2000x578时的比例系数，根据我在PS中的感觉来的
    if w >= h:          #照片为横版
        blankcoefficient_w=0.03             #设置不同的空白比例系数
        blankcoefficient_h=0.2
    else:                 #照片为竖版
        blankcoefficient_w = 0.03
        blankcoefficient_h = 0.16
    # 比较照片的宽高，竖版时高小一点，这样好看一点
    width=w*(1+blankcoefficient_w)
    hight=h*(1+blankcoefficient_h)
    img_new = Image.new('RGB', (int(width), int(hight)), color='white')
    img_new.paste(img_ori, (int(orange_size* 0.015), int(orange_size * 0.024)))
    logo = Image.open("Source/Logo/Pentax.png")  # 打开logo图片,并根据原始比例缩放
    logo_w = logo.size[0]
    logo_h = logo.size[1]
    logo = logo.resize((int(logo_w * scale), int(logo_h * scale)))
    # 0.58*w/6000为缩放比例系数，
    img_new.paste(logo, (int(width * 0.09), int(h * (1+blankcoefficient_h/2) + orange_size * 0.012 - logo_h*scale/2)), logo)
    # 根据相对位置粘贴logo图片，h*1.1 + orange_size * 0.012为底部空白的中心位置
    # logo_h *scale/2为logo缩放的高度一半
    font = ImageFont.truetype("Source/Font/MiSans-Demibold.ttf", size=int(120 * w / 6000))  # 打开字体文件，并设置字体大小
    draw = ImageDraw.Draw(img_new)
    #####添加型号和镜头信息，x轴为剩余空间的中心位置，y轴与logo顶部平齐#####
    text = "{0}   {1}".format(exif_dict['型号'], exif_dict['镜头型号'])
    text_w, text_h = draw.textsize(text, font=font)  # 获取文字的宽高,以便居中对齐
    draw.text((int(width * 0.09 + logo_w *scale + (
                width - width * 0.09 - logo_w * scale) / 2 - text_w / 2),
               int(h * (1+blankcoefficient_h/2) + orange_size * 0.012 - logo_h * scale/2)), text, (0, 0, 0), font)
    #####添加品牌和拍摄时间信息，x轴为剩余空间的中心位置，y轴为logo底部#####
    text = "光圈:f{0}  快门:{1}S  ISO:{2}  焦距:{3}  时间:{4}".format(exif_dict['光圈'], exif_dict['曝光时间'], exif_dict['ISO'],
                                                            exif_dict['焦距'], exif_dict['拍摄时间'])
    text_w, text_h = draw.textsize(text, font=font)  # 获取文字的宽高,以便居中对齐
    draw.text((int(width * 0.09 + logo_w *scale+ (
            width - width * 0.09 - logo_w *scale) / 2 - text_w / 2),
               int(h * (1+blankcoefficient_h/2) + orange_size * 0.012 + logo_h *scale/2 - text_h * 1)), text, (0, 0, 0), font)

    img_new.save("{}".format(outputname), quality=95*qlity, subsampling=0, dpi=(300.0, 300.0))



if __name__ == '__main__':
    file_path = r"D:\备份\合影\端午合影\6寸\1.jpg"
    exif_dict = get_exif(file_path)

    #image_borde(exif_dict,file_path,outputname=r"C:\Users\Tokey\PycharmProjects\Picframe\完成.jpg")

