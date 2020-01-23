# Uplift Modelling

Deciding whether a direct marketing campaign will produce favourable results for a particular customer is a causal inference problem where the result of not targeting a customer becomes a [counterfactual](https://en.wikipedia.org/wiki/Impact_evaluation). We can use ML to solve this problem by performing [uplift modelling](http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf) on data that is a result of randomized experiments. Such data is already extensively collected by companies that perform conversion rate optimization or A/B tests to decide whether to implement changes to the business. The literature for uplift modelling is established but not widely popular among the Data Science community whilst decent non-commercial packages are recently becoming available (e.g. [1](https://tech.wayfair.com/data-science/2018/10/pylift-a-fast-python-package-for-uplift-modeling/), [2](https://github.com/uber/causalml)).

In this project, I use Pylift to reproduce the methodology seen in a relatively recent [marketing paper](https://journals.sagepub.com/doi/full/10.1509/jmr.16.0163) on a well known [data mining dataset](https://blog.minethatdata.com/2008/05/best-answer-e-mail-analytics-challenge.html) in the uplift modelling community. Specifically the model is tasked with being able to predict which customer groups are most likely to visit the website of the company **as a result of** direct marketing efforts i.e. an E-Mail campaign. This is measured by the visit rate uplift of the E-Mail campaign for different customer deciles created by the model, where customers with the largest model predicted uplift should be targeted first by the E-Mail campaign. The model is trained on a training set and evaluated on a test set just like any other supervised ML setting.

Compared to building a model to predict customers who are likely to visit the website based on known information and directly marketing to those who are most likely to visit, the uplift model achieves a statistically significant increase in visit rate uplift by instead targeting customers who are predicted to have the largest visit rate uplift directly based on the same known information. More details on the train/test split and the methodology can be seen in the notebook and the reference paper.

**Notes/Future work**

- I am still in the process of reviewing the literature in order to gain a better understanding of how these models train and make predictions, my understanding of these models is still relatively rudimentary
- Non-clinical datasets are limited and are usually [heavily anonymized](http://ailab.criteo.com/criteo-uplift-prediction-dataset/) which makes experimenting with these models difficult

<p align="center"><img src="data/figures/cumulative_lift.png" width=750></p>
<p align="center"><img src="data/figures/visit_rate_by_model.png" width=750></p>
<p align="center"><img src="data/figures/cumulative_uplift.png" width=450></p>
