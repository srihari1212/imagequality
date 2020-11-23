# VGG-Image-classification
## **Building VGG-16 Model for Image Classification (99% accuracy)**

The _VGG-16_ is the CNN model trained on more than a million images of 1000 different categories.

Transfer learning refers to the technique of using knowledge of one domain to another domain.i.e. a NN model trained on one dataset can be used for other dataset by fine-tuning the former network.

No.of.classes: 11

Classes : Aadhaar_front | Aadhaar_back | Voter_id_front | Voter_id_back | passport_front | passport_back | driving_license_front | driving_license_back | Pan1 | Pan2 | Pan3 

## **Results**

   The accuracy of the training reached 99% in 50 epoch.
  
   The accuracy of the test reached 98%
  
   The accuracy of validation reached 99%
   
![Screenshot (195)](https://user-images.githubusercontent.com/68611045/99819350-5d373800-2b75-11eb-8dea-a3160189dc97.png)

## **prediction.py**

   Input : image 

   Output : (Class id, Class name)

  _KYC_Vgg_transfer_learning.h5_ 
    [Click here](https://drive.google.com/file/d/1nhcXBz-lzjmIlicDUBNHItbEBRX9bXfs/view?usp=sharing "weight file")

    Saved model with accuracy 99%
          
   _encoder.pkl_ 

    Saved LabelEncoder object while training

   Time taken testing : 1s per image

## **Versions**
   Keras : 2.4.3
   
   Tensorflow : 2.3.0
