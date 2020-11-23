########################################### IMPORT LIBRARIES ############################
from sewar import full_ref
import cv2
import traceback
import yaml
        
##################################### FULL REFERENCE IQA #####################################

def full_reference(src1,src2,l,b):
    
    try:
        img1 = cv2.imread(src1)
        img2 = cv2.imread(src2)

        img1 = cv2.resize(img1,(l,b))
        img2 = cv2.resize(img2,(l,b))

        ergas = full_ref.ergas(img1,img2) 
        psnr = full_ref.psnr(img1,img2)
        rase = full_ref.rase(img1,img2)
        rmse = full_ref.rmse(img1,img2)
        ssim = full_ref.ssim(img1,img2)
        uqi = full_ref.uqi(img1,img2)      
    except:
        print(traceback.print_exc()) 

    return ergas,psnr,rase,rmse,ssim[0],uqi

####################################  FINAL FUNCTION ####################################

def final_check(src1,src2,given_class):

    with open('config.yaml') as f: 
        docs = yaml.load_all(f, Loader=yaml.FullLoader)

        for doc in docs:
            for k, v in doc.items():
                if k == given_class:
                    ergas_gt = v[0]['ergas']
                    psnr_gt = v[1]['psnr']
                    rase_gt = v[2]['rase']
                    rmse_gt = v[3]['rmse']
                    ssim_gt = v[4]['ssim']
                    uqi_gt = v[5]['uqi']
                    l_gt = v[6]['l']
                    b_gt = v[7]['b']

    cnt = 0
    ergas,psnr,rase,rmse,ssim,uqi = full_reference(src1,src2,l_gt,b_gt)

    if ergas>ergas_gt:
        cnt+=1
    if psnr<psnr_gt:
        cnt+=1
    if rase >rase_gt:
        cnt+=1
    if rmse>rmse_gt:
        cnt+=1
    if ssim<ssim_gt:
        cnt+=1
    if uqi<uqi_gt:
        cnt+=1
        
    if cnt>=3:
        return 0
    else:
        return 1
##################################### IMAGE SIZES ##########################################

# PAN(1011,639); ADHB(1011,639); ADHF(1011,639); DL(1011,639); PASSPT(984,692); VIDB(639,1011), VIDF(639,1011)

###################################### IMAGE PATHS ( REFERENCE AND TEST )#####################
given_class = 'pan'
src1 = './ref/' + given_class + '_ref.jpg'
src2 = './testing/apdv_1.jpg'

# print(final_check(src1,src2,given_class))