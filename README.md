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
I use this repository to summarize my findings, any contribution is welcome.

# Under Review
* https://machinelearningmastery.com/deep-learning-for-time-series-forecasting/
