import dalex as dx
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression, LogisticRegression
from joblib import load

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
# Set up models from joblib
# ==========================
y = df['Employed']
cv_lr1 = load('modeles/logistic_regression_baseline.joblib')
cv_tree1 = load('modeles/decision_tree_baseline.joblib')
cv_forest1 = load('modeles/random_forest_baseline.joblib')
cv_xg1 = load('modeles/xgboost_baseline.joblib')
cv_lr = load('modeles/logistic_regression.joblib')
cv_tree = load('modeles/decision_tree.joblib')
cv_forest = load('modeles/random_forest.joblib')
cv_xg = load('modeles/xgboost.joblib')
explainer_lr1 = dx.Explainer(cv_lr1, df, y)
explainer_tree1 = dx.Explainer(cv_tree1, df, y)
explainer_forest1 = dx.Explainer(cv_forest1, df, y)
explainer_xg1 = dx.Explainer(cv_xg1, df, y)
explainer_lr = dx.Explainer(cv_lr, df, y)
explainer_tree = dx.Explainer(cv_tree, df, y)
explainer_forest = dx.Explainer(cv_forest, df, y)
explainer_xg = dx.Explainer(cv_xg, df, y)

# ==========================
# Utils functions
# ==========================

def get_employed_bias_bar_figure(bias):
    df_bias = df.groupby([bias, "Employed"]).size().reset_index(name="Number")
    df_bias.Employed = (df_bias.Employed == 1)
    fig = px.bar(
        df_bias,
        x=bias,
        y="Number",
        color="Employed",
        title=f"Number of employed by : {bias}",
        color_discrete_sequence=["grey", "darkred"],
    )
    return fig


def get_employed_bias_pie_figure(bias):
    df_bias = df.groupby([bias, "Employed"]).size().reset_index(name="Number")
    fig_1 = px.pie(
        df_bias, values="Number", names=bias, title="Analysis among the population"
    )
    df_bias = (
        df[df.Employed == 1]
        .groupby([bias, "Employed"])
        .size()
        .reset_index(name="Number")
    )
    fig_2 = px.pie(
        df_bias, values="Number", names=bias, title="Analysis among the Employed"
    )
    return fig_1, fig_2


def get_salary_bias_box_figure(bias):
    fig = px.box(df, x=bias, y="PreviousSalary")
    return fig

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
    f_object_dc = explainer_tree1.model_fairness(
        protected=protected, privileged=privileged, label="Decision Tree"
    )
    f_object_rf = explainer_forest1.model_fairness(
        protected=protected, privileged=privileged, label="Random Forest"
    )
    f_object_gb = explainer_xg1.model_fairness(
        protected=protected, privileged=privileged, label="Gradient Boosting"
    )
    return lambda t: f_object_dc.plot([f_object_rf, f_object_gb], type=t, show=False)


def get_fairness_check_after_mitigation(criteria, privileged, model):
    protected = df[criteria]
    lookup = {
        "Random Forest": [explainer_forest1, explainer_forest],
        "Gradient Boosting": [explainer_xg1, explainer_xg]
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
    st.image("LOGO-ENSAE.png")
    st.subheader("Pierre CLAYTON")
    st.subheader("Clément DE LARDEMELLE")
    st.subheader("Louise LIGONNIERE")

(tab_analysis_employment,
 tab_analysis_salary,
 tab_linear_regression,
 tab_logistic_regression,
 tab_fairness_test,
 tab_bias_mitigation) = st.tabs(
    [
        "Analysis: employment",
        "Analysis: salary",
        "Linear Regression",
        "Logistic Regression",
        "Fairness Test",
        "Bias Mitigation",
    ]
)

# ==========================
# Analysis: employment
# ==========================

tab_analysis_employment.header("Data analysis by employment")
criteria_selector_1 = tab_analysis_employment.selectbox(
    "Which criteria to analyse with employment ?",
    ["Age", "Gender", "Country", "MentalHealth", "Accessibility"],
)

tab_analysis_employment.plotly_chart(get_employed_bias_bar_figure(criteria_selector_1))

figure_1, figure_2 = get_employed_bias_pie_figure(criteria_selector_1)
tab_analysis_employment.plotly_chart(figure_1)
tab_analysis_employment.plotly_chart(figure_2)

# ==========================
# Analysis : salary
# ==========================

tab_analysis_salary.header("Data analysis by Salary")
criteria_selection_2 = tab_analysis_salary.selectbox(
    "Which criteria to analyse with salary ?",
    ["Age", "Gender", "Country", "MentalHealth", "Accessibility"],
)

figure_3 = get_salary_bias_box_figure(criteria_selection_2)
tab_analysis_salary.plotly_chart(figure_3)

# ==========================
# Logistic Regression
# ==========================

tab_logistic_regression.header("Logistic Regression")
list_col = tab_logistic_regression.multiselect(
    "Select variable for Logistic Regress: ",
    VAL_COLS + TO_DUMMIES,
    default=VAL_COLS[1:] + TO_DUMMIES,
)
result_df, score, X, delta_prob = get_data_log_regression(parameters=list_col)
tab_logistic_regression.subheader(f"The score is: {round(score * 100, 2)}%")
tab_logistic_regression.table(result_df)

# ==========================
# Fairness test
# ==========================

tab_fairness_test.header("Models on biased dataset performance:")

tab_fairness_test.subheader("Decision Tree performance")
tab_fairness_test.table(cv_tree1.model_performance().result)

tab_fairness_test.subheader("Random Forest performance")
tab_fairness_test.table(cv_forest1.model_performance().result)

tab_fairness_test.subheader("Gradient Boosting performance")
tab_fairness_test.table(cv_xg1.model_performance().result)

tab_fairness_test.header("Fairness check")

criteria_selector_3 = tab_fairness_test.selectbox(
    "Which criteria to check fairness on ?",
    ["Age", "Gender", "MentalHealth", "Accessibility"],
)

criteria_selector_4 = tab_fairness_test.selectbox(
    'Which value to be considered as "privileged" ?',
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

tab_bias_mitigation.header("Bias mitigation with Dalex")

model_selector = tab_bias_mitigation.selectbox(
    "Which model should have its biases mitigated ?",
    ["Random Forest", "Gradient Boosting"],
    key="bias6_model_selectbox",
)

criteria_selector_5 = tab_bias_mitigation.selectbox(
    "Which criteria to check fairness on ?", ["Gender"], key="bias6_1_selectbox"
)

criteria_selector_6 = tab_bias_mitigation.selectbox(
    'Which value to be considered as "privileged" ?', ["Man"], key="bias6_2_selectbox"
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