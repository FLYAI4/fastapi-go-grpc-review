import os
from fastapi import UploadFile


def create_folder_if_not_exists(folder_path: str) -> str:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return "Success create folder."
    return "Already exist folder."


def make_file_name(image_file: UploadFile, username: str):
    file_extension = image_file.filename.split(".")[-1]
    return username + "." + file_extension


async def save_image_local(image_file: UploadFile, username: str) -> str:
    libs_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
    imgs_path = os.path.abspath(os.path.join(libs_path, "img"))
    create_folder_if_not_exists(imgs_path)

    file_name = make_file_name(image_file, username)
    user_file_path = os.path.abspath(os.path.join(imgs_path, file_name))

    with open(user_file_path, "wb") as f:
        f.write(image_file.file.read())

    return user_file_path


async def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return "Success delete file."
    return "There is no file."
