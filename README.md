# Uplift Modelling

<p align="center"><img src="data/figures/qini_curve.png" width=750></p>
<p align="center"><img src="data/figures/visit_rate_by_model.png" width=750></p>
<p align="center"><img src="data/figures/cumulative_uplift.png" width=450></p>

Understanding whether or not a direct marketing campaign will have a positive impact on a particular customer is a causal inference problem which involves anticipating [what would have happened if the customer was not marketed to](https://en.wikipedia.org/wiki/Impact_evaluation#Counterfactual_evaluation_designs). We can use ML to solve this problem by performing [uplift modelling](http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf) on randomized experimental data consisting of control and treatment group observations. Such data is already extensively collected by companies who perform conversion rate optimization or A/B testing to decide whether or not to implement changes to the business. The literature for uplift modelling is established but not widely popular among the Data Science community and decent non-commercial packages are recently becoming available (e.g. [1](https://tech.wayfair.com/data-science/2018/10/pylift-a-fast-python-package-for-uplift-modeling/), [2](https://github.com/uber/causalml)).

In this project, I used Pylift to reproduce the methodology from a recent [marketing paper](https://journals.sagepub.com/doi/full/10.1509/jmr.16.0163) to analyze a well known [uplift modelling dataset](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html). Specifically the model is tasked with being able to predict which customers are most likely to visit the website of a company **as a result of** direct marketing efforts i.e. an E-Mail campaign. This is measured by the visit rate uplift of the E-Mail campaign for different customers given their features, where customers assigned a high uplift score by the model should be targeted first by the E-Mail campaign. The uplift model is built on a training set containing treatment and control group customers (and evaluated on a separate test set).

Compared to marketing to customers who are assigned a high score by a standard "response" model (an ML classifier which predicts the probability of visting given customer features for those who receive the treatment), the uplift model achieves a statistically significant increase in visit rate uplift by instead targeting customers who are predicted to have a high uplift directly. More details on the train/test split, the methodology and the models can be seen in the notebook and the reference paper.

**Notes/Future work**

- Compare the performance of Pylift's transformed outcome method to the Two-Model-Approach
- Non-clinical datasets are limited and are usually [heavily anonymized](http://ailab.criteo.com/criteo-uplift-prediction-dataset/) which makes experimenting with these models difficult. Find more datasets to experiment with

## Installation

Simply clone the repo and install all dependencies listed in the requirements.txt file to an environment of your choice.

## Usage

All results and plots can be reproduced using the Uplift_Modelling.ipynb notebook.
