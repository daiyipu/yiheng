from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
import pandas as pd
train1 = pd.read_csv('./train1.csv')
test1 = pd.read_csv('./test1.csv')
train = pd.DataFrame(train1, columns=['T', 'S', 'Q', 'V','G'])
# head = next(train1)
model = BayesianModel([('T', 'S'), ('T', 'G'), ('Q', 'G'), ('S', 'V'),('V', 'G'),('S', 'G')])
model.fit(train , estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
for cpd in model.get_cpds():
    print(cpd)
predict_data = pd.DataFrame(test1, columns=['T', 'S', 'Q', 'V'])
y_pred = model.predict(predict_data)
i=0
print("预测结果：")
while i <len(y_pred['G']):
      print(y_pred['G'][i],' ',end='')
      i=i+1