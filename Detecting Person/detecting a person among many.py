import face_recognition as fr

import cv2

found=False

me=fr.load_image_file("sample.jpg")

me=cv2.resize(me,(500,800))

me=cv2.cvtColor(me,cv2.COLOR_RGB2BGR)

my_loc=fr.face_locations(me)[0]

my_enc=fr.face_encodings(me)[0]

frens=fr.load_image_file("test.jpg")

frens=cv2.resize(frens,(900,800))

frens=cv2.cvtColor(frens,cv2.COLOR_RGB2BGR)

fren_locs=fr.face_locations(frens)

fren_encs=fr.face_encodings(frens)

for (fren_enc,fren_loc) in zip(fren_encs,fren_locs):

    if fr.compare_faces([fren_enc],my_enc)[0]:

        print("I was found !")

        found=True

        up,right,bottom,left=fren_loc

        break
        
if found:

   cv2.rectangle(frens,(left,up),(right,bottom),(0,0,255),2)

   cv2.imshow("person to be found",me)

   cv2.imshow("among people",frens)

cv2.waitKey(0)
