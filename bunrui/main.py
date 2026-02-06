from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS


def load_exif(path):
    ifd_dict = {}
    with Image.open(path) as im:
        exif = im.getexif()
    # {タグID: 値}の辞書を{タグ名: 値}の辞書に変換
    ifd_dict["Zeroth"] =  {TAGS[tag_id]: value for tag_id, value in exif.items() }
    ifd_dict["Exif"] =    {TAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8769).items()}
    ifd_dict["GPSInfo"] = {GPSTAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8825).items()}
    return ifd_dict,exif

path = 'hoge.jpg'
ifd_dict = load_exif(path)
