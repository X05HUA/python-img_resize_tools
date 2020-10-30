from PIL import Image
import os


def resize_pics(img_width, img_height, input_dir, output_dir):
    size_out = (int(img_width), int(img_height))

    if img_width <= 1920 and img_height <= 1080:
        # Resize images and place in the 300 & 700 folder
        os.mkdir(f"{output_dir}/{img_width}x{img_height}")
        os.chdir(f"{input_dir}")
        # os.chdir(f"{output_dir}/{img_width}x{img_height}")

        for f in os.listdir(input_dir):
            if f.endswith('.jpg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)

                i.thumbnail(size_out)
                i.save(f'{output_dir}/{img_width}x{img_height}/{fn}_{img_width}x{img_height}{fext}')
    else:
        print("resize image not in range")
        print("Only resize images up to 1920 x 1080")


# testing line
# resize_pics(10, 20, "/run/media/chaos/850 evo/arch0.old", "/run/media/chaos/850 evo/Images")