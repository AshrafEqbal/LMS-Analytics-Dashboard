import pandas as pd

# ===================
# 1. Load the data
# ===================
df = pd.read_csv('xAPI-Edu-Data.csv')
print(df.head)
print(df.info())
print(df.describe())


# ===================
# 2. Clean column names
# ===================
print(df.isnull().sum())
df.columns=df.columns.str.strip()
df=df.dropna()
print(df.info())

# ===================
# 3. Encode Categorical Values
# ===================
df['performance_score'] = df['Class'].map({'L': 1, 'M': 2, 'H': 3})
df['ParentAnsweringSurvey'] = df['ParentAnsweringSurvey'].map({'Yes': 1, 'No': 0})
df['ParentschoolSatisfaction'] = df['ParentschoolSatisfaction'].map({'Good': 1, 'Bad': 0})

# ===================
# 4. Compute KPIs
# ===================
# Average performance by Stage
stage_kpi = df.groupby('StageID', as_index=False)['performance_score'].mean()

# Engagement metrics by Class
engagement_kpi = df.groupby('Class', as_index=False)[
    ['RaisedHands', 'VisITedResources', 'AnnouncementsView', 'Discussion']
].mean()

# Impact of absence on performance
absence_kpi = df.groupby('StudentAbsenceDays', as_index=False)['performance_score'].mean()

# Gender-wise performance
gender_kpi = df.groupby('gender', as_index=False)['performance_score'].mean()

# ===================
# 5. Save cleaned data & KPIs
# ===================
df.to_csv('clean_lms_data.csv', index=False)
stage_kpi.to_csv('stage_kpi.csv', index=False)
engagement_kpi.to_csv('engagement_kpi.csv', index=False)
absence_kpi.to_csv('absence_kpi.csv', index=False)
gender_kpi.to_csv('gender_kpi.csv', index=False)

print("Data cleaning and KPIs generated successfully!")
print("Created files:\n- clean_lms_data.csv\n- stage_kpi.csv\n- engagement_kpi.csv\n- absence_kpi.csv\n- gender_kpi.csv")
