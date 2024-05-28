import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomeClass

# Define your mappings here
workclass_mapping = {'Federal-gov': 0,'Local-gov': 1,'Never-worked': 2,'Private': 3,
                     'Self-emp-inc':4,'Self-emp-not-inc':5,'State-gov': 6, 'Without-pay': 7, }

education_mapping = {'Preschool': 1,'1st-4th': 2,'5th-6th': 3,'7th-8th': 4,'9th': 5,
                     '10th': 6,'11th': 7,'12th': 8,'HS-grad': 9,'Some-college': 10,'Assoc-voc': 11,
                     'Assoc-acdm': 12,'Bachelors': 13,'Masters': 14,'Prof-school': 15,'Doctorate': 16}


marital_status_mapping={'Divorced':0,'Married-AF-spouse':1,'Married-civ-spouse':2,'Married-spouse-absent':3,
                        'Never-married':4,'Separated':5,'Widowed':6}


occupation_mapping={'Adm-clerical':0,'Armed-Forces':1,'Craft-repair':2,'Exec-managerial':3,'Farming-fishing':4,
                    'Handlers-cleaners':5,'Machine-op-inspct':6,'Other-service':7,'Priv-house-serv':8,
                    'Prof-specialty':9,'Protective-serv':10,'Sales':11,'Tech-support':12,'Transport-moving':13}

relation_mapping={'Husband':0,'Not-in-family':1,'Other-relative':2,'Own-child':3,'Unmarried':4,'Wife':5}

race_mapping = {'Amer-Indian-Eskimo':0,'Asian-Pac-Islander':1,'Black':2,'Other':3,'White':4}

sex_mapping = {'Female':0,'Male':1}

native_country_mapping={'Cambodia':0,'Canada':1,'China':2,'Columbia':3,'Cuba':4,'Dominican-Republic':5,
                        'Ecuador':6,'El-Salvador':7,'England':8,'France':9,'Germany':10,'Greece':11,
                        'Guatemala':12,'Haiti':13,'Holand-Netherlands':14,'Honduras':15,'Hong':16,
                        'Hungary':17,'India':18,'Iran':19,'Ireland':20,'Italy':21,'Jamaica':22,
                        'Japan':23,'Laos':24,'Mexico':25,'Nicaragua':26,'Outlying-US(Guam-USVI-etc)':27,'Peru':28,
                        'Philippines':29,'Poland':30,'Portugal':31,'Puerto-Rico':32,'Scotland':33,
                        'South':34,'Taiwan':35,'Thailand':36,'Trinadad-Tobago':37,'United-States':38,
                        'Vietnam':39,'Yugoslavia':40}


def main():
    st.title("Income Prediction")

    st.write("Please enter your details:")

    with st.form(key='prediction_form'):

        age = st.number_input("Age", min_value=0, step=1)

        workclass = st.selectbox("Workclass", options=list(workclass_mapping.keys()))
        education_num = st.selectbox("Education", options=list(education_mapping.keys()))
        marital_status = st.selectbox("Marital Status",options=list(marital_status_mapping.keys()))
        occupation = st.selectbox("Occupation", options=list(occupation_mapping.keys()))
        relationship = st.selectbox("Relationship",options=list(relation_mapping.keys()))
        race = st.selectbox("Race", options=list(race_mapping.keys()))
        sex = st.selectbox("Sex", options=list(sex_mapping.keys()))


        capital_gain = st.number_input("Capital Gain", min_value=0, step=1)
        capital_loss = st.number_input("Capital Loss", min_value=0, step=1)
        hours_per_week = st.number_input("Hours Per Week", min_value=0, step=1)

        native_country = st.selectbox("Native Country",options=list(native_country_mapping.keys()))

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        data = CustomeClass(
            age=int(age),

            workclass=workclass_mapping[workclass],
            education_num=education_mapping[education_num],
            marital_status=marital_status_mapping[marital_status],
            occupation=occupation_mapping[occupation],
            relationship=relation_mapping[relationship],
            race=race_mapping[race],
            sex=sex_mapping[sex],

            capital_gain=int(capital_gain),
            capital_loss=int(capital_loss),
            hours_per_week=int(hours_per_week),

            native_country=native_country_mapping[native_country]
        )

        final_data = data.get_data_to_dataframe()

        pipeline_prediction = PredictionPipeline()

        pred = pipeline_prediction.predict(final_data)

        result = pred[0]  # Assuming predict returns a list or array

        if result == 0:
            st.success("Your yearly income is less or equal to 50k")
        elif result == 1:
            st.success("Your yearly income is more than 50k")

if __name__ == "__main__":
    main()
