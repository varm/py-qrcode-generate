# -*- coding: utf-8 -*-
# !/usr/bin/python3

import module_myqr


def main():
    while True:
        option = input("""
        ***********************
        Please select the feature option:
        1. > Generate qr code
        2. > Read the qr code
        3. > Exit
        ***********************
        """)
        if option == '1':
            str_content = input('Please enter the content of qr code:')
            back_img_path = input(
                'If you want to generate a QR code with a background image, please enter the full path of the image('
                'eg.: D:\\custom_qrcode.png):')
            print("Start generate qr code...")
            module_myqr.generate_qrcode(str_content=str_content, pic_name=back_img_path)
        elif option == '2':
            pic_path = input('Please enter the full path of the qr code picture(eg.: D:\\custom_qrcode.png):')
            print("Start read the qr code...")
            module_myqr.parse_qrcode(pic_path)
        elif option == '3':
            print('Exit!')
            break
        else:
            print("Invalid selection!")


if __name__ == '__main__':
    main()
