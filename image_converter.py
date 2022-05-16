import base64

path_to_image = 'icon.png'
save_name = 'bytes_icon'


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('images.py', 'a') as f:
        f.write(content)


def pic2ico(file):
    from PIL import Image
    file_out = file.split('.')[0]
    filename = file
    img = Image.open(filename)
    img.save(f'{file_out}.ico')


if __name__ == '__main__':
    pic2str(path_to_image, save_name)
    pic2ico(path_to_image)
