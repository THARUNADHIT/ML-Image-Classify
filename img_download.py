import os
os.chdir('C:\\Users\\ELCOT\\PycharmProjects\\Image classify\\simple_images\\tonystark')
i = 1
for file in os.listdir():
    scr = file
    dst = "Iron_man" + str(i)+ ".jpg"
    os.rename(scr, dst)
    i += 1