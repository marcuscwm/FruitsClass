import os
from PIL import Image, ImageEnhance

folder = 'train'
newfolder = 'train_new'
items = ['apple', 'banana', 'orange', 'mixed']
counts = []

if os.path.exists(newfolder) is False:
    os.makedirs(newfolder)
else:
    for files in os.listdir(newfolder):
        os.remove(newfolder + '/' + files)

for item in items:
    count = 0
    for file_name in os.listdir(folder):
        name = file_name.split('_')
        if name[0] == item:
            img_raw = Image.open(folder + '/' + file_name)

            img_ = img_raw.convert("RGB")
            destination0 = newfolder + '/' + file_name
            img_.save(destination0)
            print(f'created \'{destination0}\'')
            count += 1

            img_flipped_H = img_.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            destination1 = newfolder + '/' + \
                f'{item}_{name[1][-5::-1][::-1]}A.jpg'
            img_flipped_H.save(destination1)
            print(f'created \'{destination1}\'')
            count += 1

            img_flipped_V = img_.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            destination2 = newfolder + '/' + \
                f'{item}_{name[1][-5::-1][::-1]}B.jpg'
            img_flipped_V.save(destination2)
            print(f'created \'{destination2}\'')
            count += 1

            enh = ImageEnhance.Contrast(img_)
            img_Enhanced = enh.enhance(1.9)
            destination3 = newfolder + '/' + \
                f'{item}_{name[1][-5::-1][::-1]}C.jpg'
            img_Enhanced.save(destination3)
            print(f'created \'{destination3}\'')
            count += 1

            DarkGreen = (0, 53, 24)
            rotated_img = img_.rotate(125, expand=0, fillcolor=DarkGreen)
            destination4 = newfolder + '/' + \
                f'{item}_{name[1][-5::-1][::-1]}D.jpg'
            img_Enhanced.save(destination4)
            print(f'created \'{destination4}\'')
            count += 1

            enh = ImageEnhance.Contrast(img_)
            img_Enhanced = enh.enhance(0.8)
            destination5 = newfolder + '/' + \
                f'{item}_{name[1][-5::-1][::-1]}E.jpg'
            img_Enhanced.save(destination5)
            print(f'created \'{destination5}\'')
            count += 1

            if name[0] == 'mixed':
                rot_angle = 32
                enhancement = 1
                for i in range(7):
                    rotated_img = img_.rotate(
                        rot_angle, expand=0, fillcolor=DarkGreen)
                    destination6 = newfolder + '/' + \
                        f'{item}_{name[1][-5::-1][::-1]}F{i}.jpg'
                    img_Enhanced.save(destination6)
                    print(f'created \'{destination4}\'')
                    rot_angle += 32
                    count += 1

                    enhancement += 0.1
                    enh = ImageEnhance.Contrast(img_)
                    img_Enhanced = enh.enhance(enhancement)
                    destination7 = newfolder + '/' + \
                        f'{item}_{name[1][-5::-1][::-1]}G{i}.jpg'
                    img_Enhanced.save(destination7)
                    print(f'created \'{destination7}\'')
                    count += 1

    counts.append(count)

print(
    f' apple: {counts[0]} \n banana: {counts[1]} \n orange: {counts[2]} \n mixed: {counts[3]}')
