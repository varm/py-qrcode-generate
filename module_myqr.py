# -*- coding: utf-8 -*-

"""
1. 使用 MyQR 库生成二维码
2. 使用 zxing 解析二维码
"""

import os
from MyQR import myqr
import zxing
import module_os

'''myqr.run 参数说明

words：二维码内容，链接或者句子
version：二维码大小，范围为[1,40]
level：二维码纠错级别，范围为{L,M,Q,H}，H为最高级，默认
picture：自定义二维码背景图，支持格式为 .jpg，.png，.bmp，.gif
colorized：二维码背景颜色，默认为 False，黑白色
contrast：对比度，值越高对比度越高，默认为 1.0
brightness：亮度，值越高亮度越高，默认为 1.0，值常和对比度相同
save_name：二维码名称，默认为 qrcode.png
save_dir：二维码路径，默认为程序工作路径
'''


def generate_qrcode(str_content='', pic_name=''):
    """
    生成二维码
    Args:
        str_content: 内容
        pic_name: 背景图片
    Returns:
         打开二维码图片
    """
    pic_name = pic_name.lower()
    if not os.path.isfile(pic_name) and not os.path.isfile('background_dancer.gif'):
        print("""The image does not exist""")
        return
    # 二维码背景图
    if pic_name.strip() == '':
        pic_name = "background_dancer.gif"

    ext = os.path.splitext(pic_name)[1]
    if ext not in ['.jpg', '.png', '.bmp', '.gif']:
        print('The image format is not supported:' + ext)
        return

    # 二维码内容，不支持中文
    str_content = str_content.strip()
    if str_content.strip() == '':
        str_content = r"Hello, world"

    # 保存文件名
    if ext == '.jpg':
        ext = '.png'

    save_name = 'custom_qrcode' + ext
    version, level, qr_name = myqr.run(words=str_content, version=10, level='H', colorized=True, picture=pic_name,
                                       save_name=save_name, save_dir=os.getcwd())
    print(f'Version: {str(version)}\n', f'Level: {level}\n', f'Save path: {qr_name}')

    # 直接打开生成的二维码
    module_os.open_with_default_app(save_name)


def parse_qrcode(file_name):
    """
    解析二维码内容
    Args:
        file_name: 二维码图片文件

    Returns:
        二维码内容

    """
    reader = zxing.BarCodeReader()
    barcode = reader.decode(file_name)
    print('Qr code Content：' + barcode.parsed)
