# Time Series Forecast Studies
## Motivation
While neural network have gain a lot of success in NLP and computer vision, there are relatively less changes for traditional time series forecasting.
This repository aims to study the lastest practical technique for time series prediction, with either statistical method, machine learning or deep neural network. I will also try to summarize practical solution from Kaggles.
- [Time Series Forecast Studies](#time-series-forecast-studies)
  - [Motivation](#motivation)
- [Summary of Kaggle Competition Results](#summary-of-kaggle-competition-results)
- [Forecasting Methods](#forecasting-methods)
  - [Statistical Method](#statistical-method)
  - [Machine Learning](#machine-learning)
  - [Deep Neural Network](#deep-neural-network)
- [Prediction Interval](#prediction-interval)
- [Python Time Series Forecasting Library](#python-time-series-forecasting-library)
- [Contribution](#contribution)
- [Under Review](#under-review)

# Summary of Kaggle Competition Results
Result are store at data/competition_results.csv
Run these two command to generate table markdown from csv.
`pip install fire`
`generate_table_pandas.py generate-table`

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Competition Name</th>
      <th>Type</th>
      <th>Date</th>
      <th>Model</th>
      <th>Rank</th>
      <th>Model Link</th>
      <th>Metrics</th>
      <th>Metrics Link</th>
      <th>Public Score</th>
      <th>Private Score</th>
      <th>Remark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>stat + lgbm + lstm</td>
      <td>1</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.509</td>
      <td>https://www.kaggle.com/shixw125/1st-place-lgb-...</td>
    </tr>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>cnn + lstm + gru</td>
      <td>2</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.512</td>
      <td></td>
    </tr>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>cnn + lstm + gru</td>
      <td>3</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.513</td>
      <td></td>
    </tr>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>dilated cnn + bi-lstm</td>
      <td>4</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.513</td>
      <td></td>
    </tr>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>lgbm + cnn/mlp + seq2seq</td>
      <td>5</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.513</td>
      <td>https://github.com/LenzDu/Kaggle-Competition-F...</td>
    </tr>
    <tr>
      <td>Corporaci?n Favorita Grocery Sales Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>lgbm</td>
      <td>6</td>
      <td>https://www.kaggle.com/c/favorita-grocery-sale...</td>
      <td>Normalized Weighted RMSLE</td>
      <td></td>
      <td></td>
      <td>0.514</td>
      <td></td>
    </tr>
    <tr>
      <td>M4 Competition</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td>es-rnn</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M4 Competition</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td></td>
      <td>2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M4 Competition</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td></td>
      <td>3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M4 Competition</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td></td>
      <td>4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M4 Competition</td>
      <td>Time Series</td>
      <td>2018-01-01 00:00:00</td>
      <td></td>
      <td>5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recruit Restaurant Visitor Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-02 00:00:00</td>
      <td>lgbm</td>
      <td>1</td>
      <td>https://www.kaggle.com/pureheart/1st-place-lgb...</td>
      <td>RMSLE</td>
      <td>https://www.kaggle.com/c/recruit-restaurant-vi...</td>
      <td>0.47</td>
      <td>0.502</td>
      <td>1st Place LGB Model(public:0.470, private:0.502)</td>
    </tr>
    <tr>
      <td>Recruit Restaurant Visitor Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-02 00:00:00</td>
      <td>xgboost + lgb + nn</td>
      <td>1</td>
      <td>https://www.kaggle.com/c/recruit-restaurant-vi...</td>
      <td>RMSLE</td>
      <td></td>
      <td></td>
      <td>0.501</td>
      <td></td>
    </tr>
    <tr>
      <td>Recruit Restaurant Visitor Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-02 00:00:00</td>
      <td>lgbm + xgboost</td>
      <td>7</td>
      <td>https://www.kaggle.com/c/recruit-restaurant-vi...</td>
      <td>RMSLE</td>
      <td></td>
      <td></td>
      <td>0.507</td>
      <td>Private  up 549 rank, from 556 --&gt; 7</td>
    </tr>
    <tr>
      <td>Recruit Restaurant Visitor Forecasting</td>
      <td>Time Series</td>
      <td>2018-01-02 00:00:00</td>
      <td>lgbm</td>
      <td>8</td>
      <td>https://github.com/MaxHalford/kaggle-recruit-r...</td>
      <td>RMSLE</td>
      <td></td>
      <td></td>
      <td>0.512</td>
      <td></td>
    </tr>
    <tr>
      <td>Web Traffic Time Series Forecasting</td>
      <td>Time Series</td>
      <td>2017-01-11 00:00:00</td>
      <td>seq2seq</td>
      <td>1</td>
      <td>https://www.kaggle.com/c/web-traffic-time-seri...</td>
      <td>SMAPE</td>
      <td>https://en.wikipedia.org/wiki/Symmetric_mean_a...</td>
      <td></td>
      <td>35.4806</td>
      <td></td>
    </tr>
    <tr>
      <td>Web Traffic Time Series Forecasting</td>
      <td>Time Series</td>
      <td>2017-01-11 00:00:00</td>
      <td>linear regression + xgboost + MLP</td>
      <td>2</td>
      <td>https://www.kaggle.com/c/web-traffic-time-seri...</td>
      <td>SMAPE</td>
      <td>https://en.wikipedia.org/wiki/Symmetric_mean_a...</td>
      <td></td>
      <td>36.785</td>
      <td></td>
    </tr>
    <tr>
      <td>Web Traffic Time Series Forecasting</td>
      <td>Time Series</td>
      <td>2017-01-11 00:00:00</td>
      <td>knn</td>
      <td>3</td>
      <td>https://www.kaggle.com/c/web-traffic-time-seri...</td>
      <td>SMAPE</td>
      <td>https://en.wikipedia.org/wiki/Symmetric_mean_a...</td>
      <td></td>
      <td>36.853</td>
      <td></td>
    </tr>
    <tr>
      <td>Web Traffic Time Series Forecasting</td>
      <td>Time Series</td>
      <td>2017-01-11 00:00:00</td>
      <td>simple stat + autoregression</td>
      <td>5</td>
      <td>https://www.kaggle.com/c/web-traffic-time-seri...</td>
      <td>SMAPE</td>
      <td>https://en.wikipedia.org/wiki/Symmetric_mean_a...</td>
      <td></td>
      <td>37.1324</td>
      <td></td>
    </tr>
    <tr>
      <td>Web Traffic Time Series Forecasting</td>
      <td>Time Series</td>
      <td>2017-01-11 00:00:00</td>
      <td>lgbm</td>
      <td>7</td>
      <td>https://www.kaggle.com/c/web-traffic-time-seri...</td>
      <td>SMAPE</td>
      <td>https://en.wikipedia.org/wiki/Symmetric_mean_a...</td>
      <td></td>
      <td>37.5747</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

# Forecasting Methods
## Statistical Method

## Machine Learning

## Deep Neural Network
[Gramian Angular Field ](https://forums.fast.ai/t/time-series-sequential-data-study-group/29686/2?u=nok): Transform time series into an image and use transfer learning with CNN

# Prediction Interval
While forecasting accuracy is important, the prediction interval is also important and it is an area that the machine learning world has less focus on.

* Traditional statistical forecast (ARIMA, ETS etc)
* Bayesian Neural Network (Use Dropout at inference time as variation inference)
* Random Forest jackknife approximation

# Python Time Series Forecasting Library

[Prophet (Facebook)](https://github.com/facebook/prophet): Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth. It has build-in modelling for Holiday effect.

[pyts](https://johannfaouzi.github.io/pyts/) : state-of-the-art algorithms for time series transformation and classification

# Contribution
I use this repository to summarize my findings, any discussion are welcome.

# Under Review
* https://machinelearningmastery.com/deep-learning-for-time-series-forecasting/
