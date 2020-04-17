
from flask import Blueprint, request, jsonify, Response
import face_recognition
import numpy as np
import math
from pathlib import Path

_face_recognition = Blueprint('face_recognition', __name__)

@_face_recognition.route('/encoding/<string:employee_id>', methods=['POST'])
def encoding(employee_id):
    try:
        data_encoding = my_face_encoding(employee_id)
        data = list(map(str, data_encoding))

        return jsonify(
            data=data
        )
    except Exception as ex:
        res = Response(ex)
        res.status_code = 500
        return res
    
@_face_recognition.route('/recognition/<employee_id>', methods=['PUT'])
def recognition(employee_id):
    data_encoding = request.get_json().get('data_encoding')
    time_tracking_id = request.get_json().get('time_tracking_id')
    
    try:
        percent = my_face_recognition(employee_id, time_tracking_id, data_encoding)

        return jsonify(
            percent=percent
        )
    except Exception as ex:
        res = Response(ex)
        res.status_code = 500
        return res

#dataset_id=1 because just have 1 dataset image for earch employee
def my_face_encoding(employee_id, dataset_id='1'):
    img_dataset_url = Path('face_recognition_images/datasets/' + employee_id + '/' + dataset_id + '.png');

    img_dataset = face_recognition.load_image_file(img_dataset_url)

    #face detection
    img_dataset_location = face_detection(img_dataset)

    #face encoding
    #return the 128-dimension face encoding
    img_dataset_encoding = face_recognition.face_encodings(img_dataset, [img_dataset_location])[0]

    return img_dataset_encoding;

def my_face_recognition(employee_id, time_tracking_id, data_encoding):
    data_encoding_convert = np.array([]);

    for value in data_encoding:
        data_encoding_convert = np.append(data_encoding_convert, float(value))
    
    img_time_tracking_url = Path('face_recognition_images/time_trackings/' + employee_id + '/' + time_tracking_id + '.png');
    
    img_time_tracking = face_recognition.load_image_file(img_time_tracking_url)

    percent = face_recognition_percent(img_time_tracking, data_encoding_convert);

    return percent

def face_recognition_percent(image, data_encoding):
    "return exactly percent when compare image with dataset-image"

    #face detection
    img_location = face_detection(image)

    #face encoding
    img_encoding = face_recognition.face_encodings(image, [img_location])[0]

    #face caculate percent match
    percent = face_distance_to_conf(face_distance(img_encoding, data_encoding), 0.3)

    return percent

def face_distance_to_conf(face_distance, face_match_threshold = 0.6): #default = 0.6
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

def face_distance(unknown_image_encoding, known_image_encoding):
    face_distances = face_recognition.face_distance([unknown_image_encoding], known_image_encoding)
    return face_distances[0]

#face detection
def face_detection(image):
    """only get face position in image"""
    face_locations = face_recognition.face_locations(image)

    acreages = []
    for(top, right, bottom, left) in face_locations:
      acreages.append(acreage_caculator(top, right, bottom, left))

    return face_locations[get_max_acreage_index(acreages)]

def acreage_caculator(top, right, bottom, left):
    """caculator acreage rectangle from 
    left top right bottom get from face_location"""
    width = right - left
    height = bottom - top
    return width * height

def get_max_acreage_index(acreages):
    return acreages.index(max(acreages))