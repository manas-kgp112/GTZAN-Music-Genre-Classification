# stores configuration and parameters yaml files

from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("config/params.yaml")





# Model dictionary
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier, XGBRFClassifier

models_dict = {
    "Naive Bayes" : GaussianNB(),
    "Stochastic Gradient Descent" : SGDClassifier(max_iter=5000, random_state=0),
    "KNN" : KNeighborsClassifier(n_neighbors=19),
    "Decision Tree" : DecisionTreeClassifier(),
    "Random Forest" : RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0),
    "Support Vector Machine" : SVC(),
    "Logistic Regression" : LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial'),
    "Neural Nets" : MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5000, 10), random_state=1),
    "AdaBoost" : AdaBoostClassifier(n_estimators=1000),
    "XGBoost" : XGBClassifier(n_estimators=1000),
    "XGBRF Classifier" : XGBRFClassifier()
}