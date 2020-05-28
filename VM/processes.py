import os
import subprocess
import time
from multiprocessing import Process
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from redis import Redis
import pexpect
import wget
import datetime
from rq import Queue
from firebase_admin import storage
import shutil
import urllib.request
import json
import boto3
import logging
from botocore.exceptions import ClientError
import flask 
import os
import sys
import base64
import json
from PIL import Image
import io
from runall import reset 
from runall import once
from runall import check
from runall import v3,mrcnn,text
reset()
yolo = 0
rcnn = 0
textp = 0
redis_conn = Redis()
q = Queue(connection=redis_conn)
p7 = Process(target=once)
p7.start()
p8 = Process(target=check)
p8.start()

while(True):
    job = q.enqueue(v3, yolo)
    while(job.result is None):
        pass
    yolo = job.result
    job = q.enqueue(mrcnn, rcnn)
    while(job.result is None):
        pass
    rcnn = job.result
    job = q.enqueue(text, textp)
    while(job.result is None):
        pass
    textp = job.result