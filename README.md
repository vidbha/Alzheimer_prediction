This is a Django-based web application that leverages a machine learning model to predict whether a person is likely to be "Demented" or "Nondemented" based on various input parameters. The app uses a pre-trained SVM model along with a numerical transformer, which are both stored as pickle files.

Features
User-Friendly Interface:
A clean, responsive HTML form that collects user data such as gender, age, years of education, SES, MMSE, CDR, eTIV, nWBV, and ASF.
Machine Learning Integration:
Processes input data through a pre-trained machine learning model (SVM) to classify the prediction outcome.
Easy Navigation:
Simple URL routing using Django to switch between the data input page and the prediction result page.
Technologies Used

Python & Django
NumPy
Scikit-Learn
Pickle (for model persistence)

Input Features
1. EDUC –Denotes the years of education of the person.
2. SES - It combines both economic and sociological factors to assess an individual's or family's access to financial resources and their social standing relative to others.
   1 – middle
   2 – middle
   3 – high
   4 – prestige
3. MMSE – A type of Brain activity Examination, introduced by Folstein in 1975, serves as a straightforward assessment of brain functions. This test has the highest score of 30 points and evaluates aspects such as time orientation, concentration, memory recall, language capabilities, visuospatial skills, and comprehension of instructions. A score below 23 points is considered a benchmark indicating the pre-sence of dementia.
4. CDR – It is a 5-point rating system that categorizes six domains of Brain abilities in AD on a 5-point scale. Those domains are Recall, judgment and problem-solving ability, public relations, lifestyles, and personal caring style. Rating is given based on the interview taken of the patient to gather reliable information related to brain performance. A score of 0.0 indicates no impairment, 0.5 suggests questionable im-pairment, 1.0 denotes moderate impairment, and 3 signifies severe impairment.
5. eTIV –Intracranial volume (ICV) is an important normalization measure that de-notes the total volume inside the cranial cavity, encompassing the brain, meninges, and cerebrospinal fluid It is usually measured with an MRI in milliliters.
6. nWBV – Represents the entirety of the brain structure volume.
7. ASF – Atlas Scaling Factor: Atlas scaling factor is an atlas normalization in which the whole brain is analyzed for its size, shape, and relation between shapes. Here atlas represents an appropriate target This calculation involves referencing the total intracranial volume measurement. The volume scaling factor should match each in-dividual's total intracranial volume to the atlas target calculate
