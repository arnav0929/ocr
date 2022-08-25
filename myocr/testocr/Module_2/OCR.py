from PIL import Image
import cv2
import numpy as np
import sys
from playsound import playsound
from gtts import gTTS
import os
import time
import boto3


def voice(myText):

    # Language we want to use
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)
    t = time.time()
    nm = "output"+str(t)+".mp3"
    output.save(nm)
    playsound(nm)


def textRecognition(filename):
    s3BucketName = "godseye-image"
    image1 = "Testing1234.png"


    s3_client = boto3.client('s3')
    response = s3_client.upload_file(filename, s3BucketName, image1)

    # S3 Bucket Data

        

    # Amazon Textract client
    textractmodule = boto3.client('textract')

    #1. PLAINTEXT detection from documents:
    response = textractmodule.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': image1
            }
        }
    )

    str = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            str = str + '\033'+item["Text"]+'\033'
    text = str
    l = ''.join(text)
    l = l.split('\n')
    li = []
    for s in l:
        s1 = "".join(c for c in s if c.isalpha() or c.isdigit()
                     or c == " " or c in "!@#$%&*.?':;_")
        if s1 != "":
            li.append(s1)
    temp = " ".join(li)
    temp = temp.split('.')
    return temp


def ocr(img):
    sentences = textRecognition(img)
    for s in sentences:
        count = sum(len(x) for x in s.split())
        print("length:")
        print(count)
        if count <= 2:
            continue
        voice(s)

#ocr('David-Scan.jpg')