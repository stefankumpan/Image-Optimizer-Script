from PIL import Image
import os



Input_Path = './input/'
Output_Path = './output/'
Quality = 60
# Sizes = [
#     1920,1440, 1200, 1024, 800, 600,300
# ]
Sizes = [
    1024, 800, 600, 300
]

if not os.path.exists(Input_Path):
    os.makedirs(Input_Path)
    print(f'{Input_Path} created')
if not os.path.exists(Output_Path):
    os.makedirs(Output_Path)
    print(f'{Output_Path} created')


def Get_Image_Name(image, input_path, file_extension):
    result = image.filename.split(input_path)[1].split(file_extension)[0]
    return result


def Image_Generator(image, image_file_name, output_path, file_extention):
    for single_size in Sizes:
        if image.size[0] >= single_size:
            image.thumbnail([single_size, single_size])
            File_Save_Path = f"{output_path}{image_file_name}-{single_size}{file_extention}"
            IMG.save(File_Save_Path, optimize=True, quality=Quality)
    print(f'Done {image_file_name}{file_extention}')


for file in os.listdir(Input_Path):
    if file.endswith('.jpg'):
        File_Extension = '.jpg'
        IMG = Image.open(Input_Path + file)
        Image_File_Name = Get_Image_Name(image=IMG, input_path=Input_Path, file_extension=File_Extension)
        print(Image_File_Name)
        Image_Generator(image=IMG, image_file_name=Image_File_Name, output_path=Output_Path,
                        file_extention=File_Extension)

    if file.endswith('.png'):
        File_Extension = '.png'
        IMG = Image.open(Input_Path + file)
        Image_File_Name = Get_Image_Name(image=IMG, input_path=Input_Path, file_extension=File_Extension)
        print(Image_File_Name)
        Image_Generator(image=IMG, image_file_name=Image_File_Name, output_path=Output_Path,
                        file_extention=File_Extension)
