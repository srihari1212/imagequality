################################## IMPORT LIBRARIES ##########################################
import traceback
from IQA_text_based import get_image_quality_tesseract_new
from Full_Reference_IQA import final_check
from prediction import test
from flask import Flask, request, jsonify, make_response
# from Classification module import function

app = Flask(__name__)

############################  IMAGE QUALITY METHOD ########################################

# image path
#path = '/home/kirankumar/Desktop/samples_53-20201119T165726Z-001/samples_53/vf/voter_card15.jpeg'

@app.route('/imagequality',methods=['POST'])
def image_quality():
    quality = 0
    try:
        # pytesseract based quality check
        img = request.files.get('image')
        img.save('img.jpg')
        path='img.jpg'
        decision, _ = get_image_quality_tesseract_new(path)
        if decision == 'Good':
            print('Inside PYtes')
            quality = 1
        
        # go to full ref if pyt_quality == 0
        if quality == 0:
            # Identify given class using image classification
            print('Inside Full ref')
            res,result = test(path)
            print(result)
            if(result == 'Pan1' or result == 'Pan2' or result=='Pan3'):
                result='pan'
            src1 = './ref/' + result + '_ref.jpg'
            src2 = path
            quality = final_check(src1,src2,result)    
        return make_response(jsonify(
                {
                    'status' : 'success',
                    'desc' : '',
                    'result' : quality
                }
            ), 200)
    except:
        print(traceback.print_exc())
        return make_response(jsonify(
                {
                    'status' : 'fail',
                    'desc':'Error in uploading files',
                    'result' : '0'
                }
            ), 207)


#print(image_quality(path))
