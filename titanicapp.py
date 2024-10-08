import streamlit as st
import pickle

st.title('Welcome to My Titanic Prediction App!')
st.image('image.png')

pickle_in = open('titanicpickle.pkl', 'rb')
classifier = pickle.load(pickle_in)

#Defining the function which will make the prediction using the data user will input
def Prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = classifier.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction)
    return prediction

def main():
    st.title('Titani Prediction App')
    #offish
    #The following code creates the text boxes in which the user can enter the data required to make prediction 
    Pclass = st.text_input('Passenger Class')
    Sex = st.text_input('Sex')
    Age = st.text_input('Age')
    SibSp = st.text_input('Sibling/Spouse')
    Parch = st.text_input('Parent/Child')
    Fare = st.text_input('Fare')
    Embarked = st.text_input('Embarked')
    result = ''
    if st.button('Predict'):
        #Convert the inputs to appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)
        result = Prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f'The output is: {result}')
main()