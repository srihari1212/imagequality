####################################### IMPORT LIBRARIES ############################
import re
import pytesseract
from PIL import Image
import cv2
import traceback
import yaml
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
####################################################################################

with open('config.yaml') as f: 
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        for k, v in doc.items():
            if k == 'pytesseract':
                conf_1 = v[0]['conf_1']
                thres_1 = v[1]['thres_1']
                conf_2 = v[2]['conf_2']
                thres_2 = v[3]['thres_2']
                len_txts_1 = v[4]['len_txts_1']
                len_txts_2 = v[5]['len_txts_2']
################################## NO TEXT IQA ######################################
def get_image_quality_tesseract(filename):
    try:
        filename = cv2.imread(filename)
        text = pytesseract.image_to_string(filename)
        
        return "Good",text
    except:
        print(traceback.print_exc())

################################# IQA Original ######################################

def get_image_quality_tesseract_first(filename):
    try:
        confCollection=[];counter=0;decision="Bad#Good"
        output=pytesseract.image_to_data(Image.open(filename))
        output=output.split("\n")
        txts=[]
        for d in output:
            cellInfo=[cell for cell in d.split("\t")]
            cellData=cellInfo[-1].strip("\n").strip(" ")
            cellConf=(cellInfo[-2]).strip("\n").strip("\t").strip()
            if cellConf!="-1" and cellData!="" and len(cellData)>0 and cellData!="text":
                T=0
                txts.append(cellData)
                if len(cellConf)==1:
                    T=int(cellConf[0])
                if len(cellConf)==2:
                    T=int(cellConf[0])*10+int(cellConf[1])
                confCollection.append(T)
                if T>=conf_1:
                    counter=counter+1

        tesseract_text=" ".join(txts)
        coverage = counter*100/len(confCollection)
        if len(txts)> len_txts_1:
            if coverage >= thres_1:
                decision="Good"
            else:
                decision="Bad"
        else:
            decision="Bad"
        # print(">>>>>>>>>>>>>>>>   Teseeract  Coverage >>>>>>>>>>>>>>>>>>>>>>>>>>>>",coverage)
        # print("Decision::::::::::::::",decision)

        return decision,tesseract_text
    except:
        print(traceback.print_exc())

########################################## IQA new #############################################
def get_image_quality_tesseract_new(filename):
    try:
        confCollection=[];counter=0;decision="Bad#Good"
        output=pytesseract.image_to_data(Image.open(filename))
        output=output.split("\n")
        txts=[]
        for d in output:
            cellInfo=[cell for cell in d.split("\t")]
            cellData=cellInfo[-1].strip("\n").strip(" ")
            cellConf=(cellInfo[-2]).strip("\n").strip("\t").strip()
            if cellConf!="-1" and cellData!="" and len(cellData)>0 and cellData!="text":
                T=0
                txts.append(cellData)
                if len(cellConf)==1:
                    T=int(cellConf[0])
                if len(cellConf)==2:
                    T=int(cellConf[0])*10+int(cellConf[1])
                confCollection.append(T)
                if T>=conf_2:
                    counter=counter+1

        tesseract_text=" ".join(txts)
        coverage = counter*100/len(confCollection)
        if len(txts)> len_txts_2:
            if coverage >= thres_2:
                decision="Good"
            else:
                decision="Bad"
        else:
            decision="Bad"
            
        # print(">>>>>>>>>>>>>>>>   Tesseract  Coverage >>>>>>>>>>>>>>>>>>>>>>>>>>>>",coverage)
        # print("Decision::::::::::::::",decision)

        return decision,tesseract_text
    except:
        print(traceback.print_exc())

##########################################################################
# if __name__ == "__main__":
#     #print(get_image_quality_tesseract('./21_1.jpg'))
#     #print(get_image_quality_tesseract_first('./21_1.jpg'))
#     print(get_image_quality_tesseract_new('./samples53/voter_card130.jpg'))