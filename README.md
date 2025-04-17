# Discovering Next-Gen Battery Materials

## Project Overview
This project was completed as part of the requirements for the Spring 2025 Data Science Boot Camp organized by the Erdős Institute.

#### Background
The goal of this project is to use machine learning to reliably predict the **band gaps** (regression task) of metal-organic frameworks (MOFs) based on different physical and chemical features. The target property—**band gaps**—is obtained from the QMOF database, which is built upon high-level quantum chemical calculations (_i. e._, DFT: Density Functional Theory) that are computationally expensive. By applying data-driven approaches to bypass the traditional DFT pipeline, we aim to accelerate the discovery of MOFs with desirable electronic properties for energy storage applications, such as next-generation batteries.

#### KPIs
1. Prediction accuracy of band gaps
2. Increased throughput of MOF screening compared to DFT
#### Stakeholders
1. Energy storage industry 
2. Battery manufacturers
3. Experimental chemists and computational researchers in novel materials design and discovery
## Datasets
We use the [QMOF database](https://www.nature.com/articles/s41524-022-00796-6#data-availability) available at [Materials Project](https://materialsproject.org/mofs). This consists of ~20k theoretical MOF structures and their DFT-derived properties, including the target property **band gap**. Our machine learning models are trained on a subset of ~10k data from this dataset, selected for having the most accurately computed band gaps.
## Feature Engineering
We explored chemical composition-based _Stoich45 fingerprints_ (He _et al_., _J. Phys. Chem. Lett_. 2018) as our featureset, which has 45 material descriptors (elemental properties and their statistical quantities). 

We refined _Stoich45 fingerprints_ using:
* Recursive Feature Elimination (RFE)
* Random Forest Feature Importance
* Lasso (L1) Regularization
* Principal component analysis (PCA) to retain ≥90% variance

The intersection of first three methods gave us a reduced **23-feature set**, while PCA reduction yielded an alternative 8-feature set. Considering early regression results, computational efficiency, and interpretability, we retained the **23-feature set** as our final feature set.

## Modeling Approach
For band gap prediction, we focus on supervised regression models, the following models were considered:

*	Linear Regression
*	Random Forest Regressor
*	XGBoost / LightGBM
*	Support Vector Regression
*	Bayesian Methods
*	Ensemble Models

We used 80% of the data to train the models, reserving the remaining 20% as a test set for evaluating the best-performing model. Cross-validation mean squared error (MSE) was used to evaluate model performance. Hyperparameter tuning was performed for all models using grid search with cross-validation.

## Results
The XGBoost model achieved a MSE of 0.51 for band gap prediction, representing a 55% improvement over the baseline constant mean model. Using SHAP feature importance, we identified several key features for band gap prediction. In terms of throughput, the ML model enables band gap prediction in seconds per MOF, compared to hours or days with traditional DFT calculations, significantly accelerating the screening process.
## Conclusions and Future Work
There is still room for improvement in our models. In future work, we plan to explore:
* Feature sets that encode structural properties of MOFs, going beyond compositional information.
* Deep learning approaches, such as Crystal Graph Convolutional Neural Networks (CGCNN), to better capture complex structure-property relationships.

### Our team:

* Avinash Karamchandani - [avijka@gmail.com](https://www.linkedin.com/in/avinash-k-055865347/)
* Dorisa Tabaku - [dorisa.tabaku@gmail.com](https://www.linkedin.com/in/dorisa-tabaku92/)
* Qinying Chen - [cqyzxy@udel.edu](https://www.linkedin.com/in/qinying-chen/)
* Simran Kaur - [simrankj@umich.edu](https://www.linkedin.com/in/simran-kaur22/)
* Sadisha Nanayakkara - [manendri@gmail.com](https://www.linkedin.com/in/sadisha-nanayakkara/)
