import numpy as np
import pandas as pd

# Number of samples
n_samples = 10000

# Demographic data
age = np.random.randint(18, 65, n_samples)  # Ages between 18 and 65
gender = np.random.choice(['Male', 'Female', 'Non-binary'], n_samples)
ethnicity = np.random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'], n_samples)

# Family history
family_history_bipolar = np.random.choice([0, 1], n_samples)  # Binary: 1 for Yes, 0 for No
family_history_depression = np.random.choice([0, 1], n_samples)

# Behavioral features
sleep_patterns = np.random.normal(7, 1.5, n_samples)  # Normally distributed sleep hours (mean 7, std dev 1.5)
mood_swings_frequency = np.random.poisson(2, n_samples)  # Poisson distribution for frequency of mood swings
substance_use = np.random.choice(['Never', 'Occasionally', 'Frequently'], n_samples)
risk_taking_behavior = np.random.choice(['No', 'Moderate', 'High'], n_samples)

# Clinical features
manic_episodes = np.random.choice([0, 1], n_samples)  # Binary: 1 for Yes, 0 for No
depressive_episodes = np.random.choice([0, 1], n_samples)
medication_adherence = np.random.choice(['Never', 'Sometimes', 'Always'], n_samples)
treatment_history = np.random.choice(['No treatment', 'Psychotherapy', 'Medication', 'Both'], n_samples)

# Psychological assessments
mood_stability_score = np.random.uniform(0, 100, n_samples)  # Score between 0 and 100
anxiety_levels = np.random.randint(0, 11, n_samples)  # Score between 0 and 10
depression_levels = np.random.randint(0, 11, n_samples)

# Environmental factors
stress_levels = np.random.randint(0, 11, n_samples)  # Stress levels between 0 and 10
traumatic_life_events = np.random.choice(['None', '1-2', '3+'], n_samples)
social_support = np.random.choice(['Low', 'Medium', 'High'], n_samples)

# Genetic predisposition
genetic_risk_score = np.random.normal(50, 10, n_samples)  # Genetic risk score with mean 50 and std dev 10

# Combine all the data into a DataFrame
df = pd.DataFrame({
    'Age': age,
    'Gender': gender,
    'Ethnicity': ethnicity,
    'Family_History_Bipolar': family_history_bipolar,
    'Family_History_Depression': family_history_depression,
    'Sleep_Patterns': sleep_patterns,
    'Mood_Swings_Frequency': mood_swings_frequency,
    'Substance_Use': substance_use,
    'Risk_Taking_Behavior': risk_taking_behavior,
    'Manic_Episodes': manic_episodes,
    'Depressive_Episodes': depressive_episodes,
    'Medication_Adherence': medication_adherence,
    'Treatment_History': treatment_history,
    'Mood_Stability_Score': mood_stability_score,
    'Anxiety_Levels': anxiety_levels,
    'Depression_Levels': depression_levels,
    'Stress_Levels': stress_levels,
    'Traumatic_Life_Events': traumatic_life_events,
    'Social_Support': social_support,
    'Genetic_Risk_Score': genetic_risk_score
})

# Display the first few rows of the generated data
print(df.head())

# Optionally, save the synthetic dataset to a CSV file
df.to_csv('synthetic_bipolar_disorder_data.csv', index=False)
