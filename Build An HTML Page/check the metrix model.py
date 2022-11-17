y_predict = regressor.predict(x_test)
print(r2_score(Y_test,y_pred))