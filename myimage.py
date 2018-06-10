from PIL import Image
import os
import time
import getpass


# 将图片转换为字符串并返回
def img_convert(img_name, x_size=300, y_size=120):
    img = Image.open(img_file_dir + img_name)  # 打开图片文件
    img = img.convert('L')  # 将图片转换为灰度图
    img = img.resize((300, 120))  # 将图片尺寸转换为指定尺寸
    img_size = img.size  # 获取图片尺寸

    txt = ''
    for i in range(img_size[1]):
        for j in range(img_size[0]):
            txt += txt_char(img, j, i)
        txt += '\n'
    return txt


# 获取图片像素灰度值并返回对应的字符
def txt_char(img, x, y):
    pixel_gray = img.getpixel((x, y))
    return asc_list[int(pixel_gray/256*len(asc_list))]


# 将转换好的图像保存到txt文件
def save_file(file_name, txt):
    with open(img_file_dir + file_name[:-4] + '.txt', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    asc_list = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    user_name = getpass.getuser()  # 获取计算机用户名
    img_file_dir = "C:/Users/" + user_name + "/Desktop/" + 'images/'  # 指定文件操作路径

    if os.path.exists(img_file_dir):
        img_name_list = os.listdir(img_file_dir)
        if len(img_name_list) == 0:
            print('images文件夹为空，请将图片放入重启应用！')
            time.sleep(5)
        else:
            print("正在转换...")
            for img_name in img_name_list:
                if ('.jpg' in img_name) or ('.png' in img_name) or ('.jpeg' in img_name):
                    img_txt = img_convert(img_name)
                    save_file(img_name, img_txt)
                    print(img_name)

            print("转换完成！")
            time.sleep(5)

    else:
        os.mkdir(img_file_dir)
        print('已为您在桌面创建images文件夹创建，请将图片放入重启应用！')
        time.sleep(5)


