import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to load the CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS
load_css('style.css')

# A dictionary to store user credentials temporarily
USER_CREDENTIALS = {
    "admin": "password123"
}

# Function to display the home page
def home_page():
    st.title("Health Prediction System")
    # st.image("home_image.jpg", use_column_width=True)
    st.write("Welcome to the Health Prediction System!")
    st.write("Please choose an option from the menu to get started.")

# Function to display the about us page
def about_us_page():
    st.title("About Us")
    # st.image("about_us_image.jpg", use_column_width=True)
    st.write("We are a team of dedicated professionals committed to providing accurate health predictions using machine learning.")

# Function to display the signup page
def signup_page():
    st.title("Signup")
    # st.image("signup_image.jpg", use_column_width=True)
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    if st.button("Signup"):
        if username in USER_CREDENTIALS:
            st.error("Username already exists")
        elif password != confirm_password:
            st.error("Passwords do not match")
        else:
            USER_CREDENTIALS[username] = password
            st.success("Signup successful! Please login.")
            st.session_state["page"] = "login"

# Function to display the login page
def login_page():
    st.title("Login")
    # st.image("login_image.jpg", use_column_width=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if username in USER_CREDENTIALS and password == USER_CREDENTIALS[username]:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to display the disease prediction page
def prediction_page():
    # loading the saved models
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

    # sidebar for navigation
    with st.sidebar:
        selected = option_menu('Disease Prediction System',
                               ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                               icons=['activity', 'heart', 'person'],
                               default_index=0)

    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        with col2:
            Glucose = st.text_input('Glucose Level')
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        with col2:
            Insulin = st.text_input('Insulin Level')
        with col3:
            BMI = st.text_input('BMI value')
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        with col2:
            Age = st.text_input('Age of the Person')
        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            try:
                # Convert input values to float
                Pregnancies = float(Pregnancies)
                Glucose = float(Glucose)
                BloodPressure = float(BloodPressure)
                SkinThickness = float(SkinThickness)
                Insulin = float(Insulin)
                BMI = float(BMI)
                DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
                Age = float(Age)
                
                diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            except ValueError:
                st.error("Please enter valid numeric values.")
        st.success(diab_diagnosis)

    # Heart Disease Prediction Page
    elif selected == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Sex')
        with col3:
            cp = st.text_input('Chest Pain types')
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
        with col2:
            chol = st.text_input('Serum Cholesterol in mg/dl')
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
            ca = st.text_input('Major vessels colored by fluoroscopy')
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
        heart_diagnosis = ''
        if st.button('Heart Disease Test Result'):
            try:
                # Convert input values to float
                age = float(age)
                sex = float(sex)
                cp = float(cp)
                trestbps = float(trestbps)
                chol = float(chol)
                fbs = float(fbs)
                restecg = float(restecg)
                thalach = float(thalach)
                exang = float(exang)
                oldpeak = float(oldpeak)
                slope = float(slope)
                ca = float(ca)
                thal = float(thal)
                
                heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            except ValueError:
                st.error("Please enter valid numeric values.")
        st.success(heart_diagnosis)

    # Parkinson's Prediction Page
    elif selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')
        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')
        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')
        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')
        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        with col1:
            RAP = st.text_input('MDVP:RAP')
        with col2:
            PPQ = st.text_input('MDVP:PPQ')
        with col3:
            DDP = st.text_input('Jitter:DDP')
        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')
        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')
        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')
        with col3:
            APQ = st.text_input('MDVP:APQ')
        with col4:
            DDA = st.text_input('Shimmer:DDA')
        with col5:
            NHR = st.text_input('NHR')
        with col1:
            HNR = st.text_input('HNR')
        with col2:
            RPDE = st.text_input('RPDE')
        with col3:
            DFA = st.text_input('DFA')
        with col4:
            spread1 = st.text_input('spread1')
        with col5:
            spread2 = st.text_input('spread2')
        with col1:
            D2 = st.text_input('D2')
        with col2:
            PPE = st.text_input('PPE')
        parkinsons_diagnosis = ''
        if st.button("Parkinson's Test Result"):
            try:
                # Convert input values to float
                fo = float(fo)
                fhi = float(fhi)
                flo = float(flo)
                Jitter_percent = float(Jitter_percent)
                Jitter_Abs = float(Jitter_Abs)
                RAP = float(RAP)
                PPQ = float(PPQ)
                DDP = float(DDP)
                Shimmer = float(Shimmer)
                Shimmer_dB = float(Shimmer_dB)
                APQ3 = float(APQ3)
                APQ5 = float(APQ5)
                APQ = float(APQ)
                DDA = float(DDA)
                NHR = float(NHR)
                HNR = float(HNR)
                RPDE = float(RPDE)
                DFA = float(DFA)
                spread1 = float(spread1)
                spread2 = float(spread2)
                D2 = float(D2)
                PPE = float(PPE)
                
                parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
                parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            except ValueError:
                st.error("Please enter valid numeric values.")
        st.success(parkinsons_diagnosis)

# Check if the user is logged in
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Check which page to show
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Main navigation
if st.session_state["logged_in"]:
    prediction_page()
else:
    selected = option_menu(
        None, ["Home", "About Us", "Login", "Signup"],
        icons=["house", "info-circle", "box-arrow-in-right", "person-plus"],
        menu_icon="cast", default_index=0, orientation="horizontal"
    )
    if selected == "Home":
        st.session_state["page"] = "home"
    elif selected == "About Us":
        st.session_state["page"] = "about_us"
    elif selected == "Login":
        st.session_state["page"] = "login"
    elif selected == "Signup":
        st.session_state["page"] = "signup"

    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "about_us":
        about_us_page()
    elif st.session_state["page"] == "login":
        login_page()
    elif st.session_state["page"] == "signup":
        signup_page()
