# Image-quality-assessment

1. This repository contains code for "Full reference", "No reference" and "Text-based" Image quality assessment. 
2. Requirements.txt mentions the dependencies. 
3. Samples from KYC documents are provided for Full reference IQA. 
4. Full Reference IQA thresholds are also provided for KYC documents. 
5. No Reference IQA thresholds are mentioned in the code.
6. If an Image fails to pass even one of the No reference IQA critreria, then it is of bad quality. 
7. If an image fails in 3 criteria of Full reference IQA then it is of bad quality. 
8. Correct image sizes / aspect ratio for different documents must be used for Full Reference IQA. 
9. Text based IQA is also added to improve accuracy. Select the threshold for this on a case-by-case basis. If image fails, then it is of bad quality.
10. A config.yaml file has been added for making provision for configurable parameters for IQA.
11. The integrated quality.py file integrates Pytesseract text based and Full reference image base QA codes using heuristics.

Product owner : Dr. Avinash, Vivek M, Arvind N
