# Define diseases and their associated symptoms
diseases = {
    'flu': ['fever', 'cough', 'sore throat', 'headache', 'muscle pain', 'fatigue'],
    'common cold': ['runny nose', 'sneezing', 'cough', 'sore throat'],
    'allergies': ['runny nose', 'sneezing', 'itchy eyes', 'skin rash'],
    'pneumonia': ['fever', 'cough', 'chest pain', 'shortness of breath', 'fatigue'],
    'bronchitis': ['cough', 'shortness of breath', 'fatigue'],
    'sinusitis': ['nasal congestion', 'facial pain', 'headache', 'sore throat'],
    'ear infection': ['ear pain', 'hearing loss', 'fever', 'dizziness'],
    'strep throat': ['sore throat', 'fever', 'swollen lymph nodes', 'headache'],
    'mononucleosis': ['fatigue', 'fever', 'swollen lymph nodes', 'sore throat'],
    'asthma': ['cough', 'shortness of breath', 'wheezing', 'chest tightness'],
}

# Define symptoms and their corresponding points
symptoms_points = {
    'fever': 1,
    'cough': 2,
    'sore throat': 3,
    'headache': 4,
    'runny nose': 5,
    'sneezing': 6,
    'itchy eyes': 7,
    'skin rash': 8,
    'chest pain': 9,
    'shortness of breath': 10,
    'fatigue': 11,
    'muscle pain': 12,
    'nasal congestion': 13,
    'facial pain': 14,
    'ear pain': 15,
    'hearing loss': 16,
    'dizziness': 17,
    'swollen lymph nodes': 18,
    'wheezing': 19,
    'chest tightness': 20
}

# Define a function to calculate the score for a given set of symptoms
def calculate_score(symptoms):
    total_points = 0
    for symptom in symptoms:
        if symptom in symptoms_points:
            total_points += symptoms_points[symptom]
    return total_points

# Define a function to suggest diseases based on the score
def suggest_diseases(score):
    suggested_diseases = []
    for disease, points in diseases.items():
        if score >= sum(symptoms_points[symptom] for symptom in points):
            suggested_diseases.append(disease)
    return suggested_diseases

# Get user input for symptoms
user_symptoms = []
while True:
    symptom = input('Enter a symptom (or "done" to finish): ')
    if symptom.lower() == 'done':
        break
    if      symptom in symptoms_points:
        user_symptoms.append(symptom)
    else:
        print(f'Sorry, "{symptom}" is not a valid symptom.')

# Calculate the score for the user's symptoms
score = calculate_score(user_symptoms)

# Suggest diseases based on the score
suggested_diseases = suggest_diseases(score)

# Display the results
if suggested_diseases:
    print(f'Based on your symptoms, you may have one or more of the following diseases: {", ".join(suggested_diseases)}')
else:
    print('Based on your symptoms, we could not suggest any possible solution as it is a serious issue. Please consult a healthcare professional immediately.')
