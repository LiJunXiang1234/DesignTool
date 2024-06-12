# 导入抠图依赖库
from PIL import Image
import rembg
import os


# 定义抠图函数
def remove_bg(my_img_path):
    my_img_path = get_img_path(my_img_path)
    img = Image.open(my_img_path)
    img_bg_remove = rembg.remove(img)
    img_bg_remove.save(img_path.replace('.png', '_remove.png'))


def get_img_path(original_img_path):
    # 如果传入的路径以 .png 结尾，则直接返回原始路径
    if original_img_path.endswith('.png'):
        return original_img_path

    # 如果传入的路径以 .jpg 结尾，则将原文件的后缀直接改为 .png
    elif original_img_path.endswith('.jpg'):
        # 使用 os 模块获取文件名和文件后缀
        file_name, file_extension = os.path.splitext(original_img_path)
        # 将 .jpg 后缀改为 .png
        new_img_path = file_name + '.png'
        # 重命名文件
        os.rename(original_img_path, new_img_path)
        return new_img_path

    # 如果传入的路径不是 .png 或 .jpg 结尾，则返回空字符串或者做其他错误处理
    else:
        print("传入的图片格式不受支持")
        return ""


if __name__ == "__main__":
    print("欢迎使用抠图程序！\n"
          "直接右键图片复制路径再粘贴就可以抠图了。\n"
          "注意，使用程序会将jpg自动改为png，请留意\n"
          "生成的图片会添加后缀\n"
          "输入q退出程序\n")
    img_path = input("请输入图片路径: ")
    img_path = img_path.strip('\'"')
    img_path = get_img_path(img_path)
    while img_path != "q":
        img_path = img_path.strip('\'"')
        remove_bg(img_path)
        print("抠图完成")
        img_path = input("请输入图片路径: ")
    # remove_bg(r"C:\Users\27618\Desktop\图片\行李箱\1-Rimowa-Branding-Art-Direction-Commission-UK-BPO_remove.png")
    print("已退出抠图程序！")
