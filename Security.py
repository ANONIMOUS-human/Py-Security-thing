import cv2
import time
import random
import dropbox

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "Login_Alert" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken, Intruder FOUND!!!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    accessToken = ""
    file = img_counter
    file_from = file
    file_to = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb")
    dbx.files_upload(f.read(),file_to)
def main():
    while(True):
        if(time.time()- start_time)>3:
            name = take_snapshot()
            upload_file(name)
    """access_token = "LsscTFe2OtQAAAAAAAAAAQFbXNmHLSJRFFIc8y5y5C84vki3SuMKDB6C8DGbZm5n"
    transferData = TransferData(access_token)
    file_from = input("Enter The File Path To Transfer:  ")
    file_to = input("Enter The Full Path To Upload To Drop Box:  ")
    transferData.upload_file(file_from, file_to)
    print("File Has Been Beamed")"""
main()

