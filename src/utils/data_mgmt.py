from PIL import Image
import shutil
import imghdr
import os
from src.utils.common import create_directories
import logging


def image_validation(config: dict) -> None:
    PARENT_DIR = os.path.join(config['data']['unzip_data_location'],config['data']['parent_data_dir'])
    BAD_DATA_DIR = os.path.join(config['data']['unzip_data_location'],config['data']['bad_data_dir'])

    create_directories([BAD_DATA_DIR])


    for dirs in os.listdir(PARENT_DIR):
        full_path_data_dir = os.path.join(PARENT_DIR, dirs)
        for imgs in os.listdir(full_path_data_dir):
            path_to_img = os.path.join(full_path_data_dir, imgs)
            try:
                img = Image.open(path_to_img)
                img.verify()

                if len(img.getbands()) != 3 or imghdr.what(path_to_img) not in ['jpeg', 'png']:
                    bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                    shutil.move(path_to_img, bad_data_path)
                    logging.info(f"{path_to_img} not of expected format")
                    continue


            except Exception as e:
                print(f"{path_to_img} is bad !")
                bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                shutil.move(path_to_img, bad_data_path)
                logging.exception(e)