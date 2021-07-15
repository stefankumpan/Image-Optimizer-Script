from PIL import Image
import os
import eel


@eel.expose
def make_images(input_path, output_path, sizes):
    quality = 60
    if not os.path.exists(input_path):
        os.makedirs(input_path)
        print(f'{input_path} created')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f'{output_path} created')
    print('path', os.listdir(input_path))
    for file in os.listdir(input_path):
        print('!!!!!!!!!!!!!!!!!!!!!! ',file)
        if file.endswith('.jpg'):
            File_Extension = '.jpg'
            IMG = Image.open(input_path + file)
            Image_File_Name = IMG.filename.split(input_path)[1].split(File_Extension)[0]
            print(Image_File_Name)
            for single_size in sizes:
                if IMG.size[0] >= single_size:
                    IMG.thumbnail([single_size, single_size])
                    File_Save_Path = f"{output_path}{Image_File_Name}-{single_size}{File_Extension}"
                    IMG.save(File_Save_Path, optimize=True, quality=quality)
            print(f'Done {Image_File_Name}{File_Extension}')

        if file.endswith('.png'):
            File_Extension = '.png'
            IMG = Image.open(input_path + file)
            Image_File_Name = IMG.filename.split(input_path)[1].split(File_Extension)[0]
            print(Image_File_Name)
            for single_size in sizes:
                if IMG.size[0] >= single_size:
                    IMG.thumbnail([single_size, single_size])
                    File_Save_Path = f"{output_path}{Image_File_Name}-{single_size}{File_Extension}"
                    IMG.save(File_Save_Path, optimize=True, quality=quality)
            print(f'Done {Image_File_Name}{File_Extension}')

    return "done"




def Image_Generator(image, image_file_name, output_path, file_extention, sizes, quality):
    for single_size in sizes:
        if image.size[0] >= single_size:
            image.thumbnail([single_size, single_size])
            File_Save_Path = f"{output_path}{image_file_name}-{single_size}{file_extention}"
            image.save(File_Save_Path, optimize=True, quality=quality)
    print(f'Done {image_file_name}{file_extention}')
