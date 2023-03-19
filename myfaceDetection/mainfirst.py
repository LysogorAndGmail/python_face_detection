#pip3 install cmake
#pip3 install dlib
#pip install face-recognition
#pip freeze (show all dependency in projeckts)

import face_recognition
from PIL import Image, ImageDraw

def face_dettect():
    geroj_img = face_recognition.load_image_file("origin_img/DSC_1156.JPG")
    face_location = face_recognition.face_locations(geroj_img)
    print(len(face_location))
    frame_img = Image.fromarray(geroj_img)
    drowImg = ImageDraw.Draw(frame_img)

    for(top, right, bottom, left) in face_location:
        drowImg.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=5)
    del drowImg

    frame_img.save("frame_img/first_frame_img.jpg")

def cut_faces_from_img(img_path):
    count_img = 0
    img = face_recognition.load_image_file(img_path)
    face_location = face_recognition.face_locations(img)

    for face_location in face_location:
        top, right, bottom, left = face_location
        face_img = img[top:bottom, left:right]

        pil_img = Image.fromarray(face_img)
        pil_img.save(f"only_faces_img/{count_img}_face.jpg")
        count_img += 1

    return f"Faces cuting {count_img}"


def compere_faces(img1_path, img2_path):
    img1 = face_recognition.load_image_file(img1_path)
    img1_cods = face_recognition.face_encodings(img1)[0] #take cods first face

    img2 = face_recognition.load_image_file(img2_path)
    img2_cods = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_cods],img2_cods)

    if result[0]:
        print("same")
    else:
        print("not same")


def main():
    #face_dettect() //created new img with frames of faces
    cut_faces_from_img("origin_img/DSC_1156.JPG")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
