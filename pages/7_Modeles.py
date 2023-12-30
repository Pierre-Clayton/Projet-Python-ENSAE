import dalex as dx
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import joblib 

# ==========================
# Set up data
# ==========================

file_path = "stackoverflow_full.csv"

df = pd.read_csv(file_path)

df = df.drop(columns=["Unnamed: 0"])
df = df.drop(columns="HaveWorkedWith")

n = len(df)

TO_DROP = [
    "Accessibility",
    "Country",
    "HaveWorkedWith"
]

VAL_COLS = [
    "PreviousSalary",
    "YearsCode",
    "YearsCodePro",
    "ComputerSkills"
]

TO_DUMMIES = [
    "Age",
    "EdLevel",
    "Gender",
    "MentalHealth",
    "MainBranch"
]

# ==========================
# Set up models from dumps dx.Explainer
# ==========================

X=df[['Age', 'Accessibility', 'EdLevel', 'Gender', 'MentalHealth', 'MainBranch','YearsCode', 'YearsCodePro', 'PreviousSalary', 'ComputerSkills']]
y=df['Employed']
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size = 0.25, random_state = 4)

exp1 = dx.Explainer(joblib.load("modeles/decision_tree_baseline.joblib"),X,y)
exp1_m = dx.Explainer(joblib.load("modeles/decision_tree.joblib"),X,y)
exp2 = dx.Explainer(joblib.load("modeles/random_forest_baseline.joblib"),X,y)
exp2_m = dx.Explainer(joblib.load("modeles/test_forest.joblib"),X,y)
exp3 = dx.Explainer(joblib.load("modeles/logistic_regression_baseline.joblib"),X,y)
exp3_m = dx.Explainer(joblib.load("modeles/test_lr.joblib"),X,y)
exp4 = dx.Explainer(joblib.load("modeles/xgboost_baseline.joblib"),X,y)
#exp4_m = dx.Explainer(joblib.load("modeles/xgboost.joblib"),X,y) # Fonctionne pas (pas le bon modèle)
exp4_m = dx.Explainer(joblib.load("modeles/test_xgb.joblib"),X,y) # Eureka ! 

 
# ==========================
# Utils functions
# ==========================

def get_data_linear_regression(parameters, difference):
    val_cols = list(set(VAL_COLS).intersection(parameters).difference(difference))
    to_dummies = list(set(TO_DUMMIES).intersection(parameters).difference(difference))
    if len(to_dummies) > 0:
        X = pd.get_dummies(df[to_dummies], drop_first=True, dtype=int)
    else:
        X = pd.DataFrame()
    X[val_cols] = df[val_cols]
    reg = LinearRegression().fit(X, df[difference])

    results = pd.DataFrame({"Variables": reg.feature_names_in_, "Coeff.": reg.coef_})
    return results, reg.score(X, df[difference])


def get_data_log_regression(parameters):
    val_cols = list(set(VAL_COLS).intersection(parameters))
    to_dummies = list(set(TO_DUMMIES).intersection(parameters))

    if len(to_dummies) > 0:
        X = pd.get_dummies(df[to_dummies], drop_first=True, dtype=int)
    else:
        X = pd.DataFrame()

    X[val_cols] = df[val_cols]
    reg = LogisticRegression(max_iter=10).fit(X, df["Employed"])

    prob = reg.predict_proba(X)[:, 0]
    delta_p = []

    for key in reg.feature_names_in_:
        X_mod = X.copy()

        if key in VAL_COLS:
            X_mod[key] = X_mod[key] - 1
            prob_mod = reg.predict_proba(X_mod)[:, 0]
            delta_p.append((prob_mod - prob).mean())
        else:  # To_dummies
            X_mod[key] = 0
            prob_mod = reg.predict_proba(X_mod)[:, 0]
            delta_p.append((prob_mod - prob)[X[key] == 1].mean())

    results = pd.DataFrame(
        {
            "Variables": reg.feature_names_in_,
            "Delta Prob.": [f"{round(x * 100, 2)} %" for x in delta_p],
            "Coeff.": reg.coef_[0],
        }
    )
    return results, reg.score(X, df["Employed"]), X, delta_p


def get_fairness_check(criteria, privileged):
    protected = df[criteria]
    f_object_dc = exp1.model_fairness(
        protected=protected, privileged=privileged, label="Decision Tree"
    )
    f_object_rf = exp2.model_fairness(
        protected=protected, privileged=privileged, label="Random Forest"
    )
    f_object_lr = exp3.model_fairness(
        protected=protected, privileged=privileged, label="Logistic Regression"
    )
    f_object_gb = exp4.model_fairness(
        protected=protected, privileged=privileged, label="Gradient Boosting"
    )
    return lambda t: f_object_dc.plot([f_object_rf, f_object_lr, f_object_gb], type=t, show=False)


def get_fairness_check_after_mitigation(criteria, privileged, model):
    protected = df[criteria]
    lookup = {
        "Random Forest": [exp2, exp2_m],
        "Gradient Boosting": [exp4, exp4_m],
        "Logistic Regression": [exp3, exp3_m]
    }

    f_object = lookup[model][0].model_fairness(
        protected=protected, privileged=privileged, label=model
    )
    f_object_mitigated = lookup[model][1].model_fairness(
        protected=protected, privileged=privileged, label=(model + " (Mitigated)")
    )
    return lambda t: f_object.plot([f_object_mitigated], type=t, show=False)


# ==========================
# User interface
# ==========================

with st.sidebar:
    st.title("Projet Python pour la Data Science")
    st.subheader("Pierre CLAYTON")
    st.subheader("Clément DE LARDEMELLE")
    st.subheader("Louise LIGONNIERE")

(tab_linear_regression,
 tab_logistic_regression,
 tab_fairness_test,
 tab_bias_mitigation) = st.tabs(
    [
        "Linear Regression",
        "Logistic Regression",
        "Fairness Test",
        "Bias Mitigation",
    ]
)

# ==========================
# Linear Regression
# ==========================

tab_linear_regression.header("Regression Linéaire")
list_col3 = tab_linear_regression.multiselect(
    "Sélectionner les variables pour la regression linéaire: ",
    VAL_COLS + TO_DUMMIES + ["Employed"],
    default=VAL_COLS[1:] + TO_DUMMIES + ["Employed"],
)

y_col3 = tab_linear_regression.selectbox("Select", VAL_COLS)
result_df3, score3 = get_data_linear_regression(list_col3, y_col3)
tab_linear_regression.subheader(f"Le R2 du modèle est : {round(score3 * 100, 2)}%")
tab_linear_regression.table(result_df3)

# ==========================
# Logistic Regression
# ==========================

tab_logistic_regression.header("Regression Logistique")
list_col = tab_logistic_regression.multiselect(
    "Sélectionner les variables pour la regression logistique: ",
    VAL_COLS + TO_DUMMIES,
    default=VAL_COLS[1:] + TO_DUMMIES,
)
result_df, score, X, delta_prob = get_data_log_regression(parameters=list_col)
tab_logistic_regression.subheader(f"Le R2 du modèle est : {round(score * 100, 2)}%")
tab_logistic_regression.table(result_df)

# ==========================
# Fairness test
# ==========================

tab_fairness_test.header("Modèles baseline:")

tab_fairness_test.subheader("Decision Tree performance")
tab_fairness_test.table(exp1.model_performance().result)

tab_fairness_test.subheader("Random Forest performance")
tab_fairness_test.table(exp2.model_performance().result)

tab_fairness_test.subheader("Logistic Regression performance")
tab_fairness_test.table(exp3.model_performance().result)

tab_fairness_test.subheader("Gradient Boosting performance")
tab_fairness_test.table(exp4.model_performance().result)

tab_fairness_test.header("Test d'équité")

criteria_selector_3 = tab_fairness_test.selectbox(
    "Sur quel critère tester l'équité ?",
    ["Age", "Gender", "MentalHealth", "Accessibility"],
)

criteria_selector_4 = tab_fairness_test.selectbox(
    'Quelle catégorie considérer comme "privileged" ?',
    set(df[criteria_selector_3])
)

plot = get_fairness_check(criteria_selector_3, criteria_selector_4)

(
    t5_fairness_check,
    t5_metric_scores,
    t5_stacked,
    t5_radar,
    t5_performance_and_fairness,
    t5_heatmap,
) = tab_fairness_test.tabs(
    [
        "Fairness Check",
        "Metric Scores",
        "Cumulated parity loss",
        "Radar",
        "Performance And Fairness",
        "Heatmap",
    ]
)

t5_fairness_check.plotly_chart(
    plot("fairness_check"), theme=None, use_container_width=True
)
t5_metric_scores.plotly_chart(
    plot("metric_scores"), theme=None, use_container_width=True
)
t5_stacked.plotly_chart(
    plot("stacked"), theme=None, use_container_width=True
)
t5_radar.plotly_chart(
    plot("radar"), theme=None, use_container_width=True
)
t5_performance_and_fairness.plotly_chart(
    plot("performance_and_fairness"), theme=None, use_container_width=True
)
t5_heatmap.plotly_chart(
    plot("heatmap"), theme=None, use_container_width=True
)

# ==========================
# Bias mitigation
# ==========================

tab_bias_mitigation.header("Mitigation des biais avec Dalex")

model_selector = tab_bias_mitigation.selectbox(
    "Quel modèle devrait avoir ses biais mitigés ?",
    ["Random Forest", "Gradient Boosting", "Logistic Regression"],
    key="bias6_model_selectbox",
)

criteria_selector_5 = tab_bias_mitigation.selectbox(
    "Sur quel critère tester l'équité ?", ["Gender"], key="bias6_1_selectbox"
)

criteria_selector_6 = tab_bias_mitigation.selectbox(
    'Quelle catégorie considérer comme "privileged" ?', ["Woman","Man"], key="bias6_2_selectbox"
)

plot = get_fairness_check_after_mitigation(criteria_selector_5, criteria_selector_6, model_selector)

(
    t6_fairness_check,
    t6_metric_scores,
    t6_stacked,
    t6_radar,
    t6_performance_and_fairness,
    t6_heatmap,
) = tab_bias_mitigation.tabs(
    [
        "Fairness Check",
        "Metric Scores",
        "Cumulated parity loss",
        "Radar",
        "Performance And Fairness",
        "Heatmap",
    ]
)

t6_fairness_check.plotly_chart(
    plot("fairness_check"), theme=None, use_container_width=True
)
t6_metric_scores.plotly_chart(
    plot("metric_scores"), theme=None, use_container_width=True
)
t6_stacked.plotly_chart(
    plot("stacked"), theme=None, use_container_width=True
)
t6_radar.plotly_chart(
    plot("radar"), theme=None, use_container_width=True
)
t6_performance_and_fairness.plotly_chart(
    plot("performance_and_fairness"), theme=None, use_container_width=True
)
t6_heatmap.plotly_chart(
    plot("heatmap"), theme=None, use_container_width=True
)