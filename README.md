# Text Classification Model Comparison | Bachelor Thesis Source Code

This repository contains the code and data used for my bachelor thesis, which focuses on comparing three different text classification machine learning models (Decision Tree, Random Forest, and LSTM) across five criteria: performance, robustness, interpretability, computational cost, and ease of deployment. The primary metrics used to evaluate performance are accuracy and F1 score, while computational cost is assessed using training time in seconds.

![Python](https://img.shields.io/badge/Python-3.8-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-orange)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.4.1-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.2.3-green)
![NumPy](https://img.shields.io/badge/NumPy-1.19.5-blue)
![NLTK](https://img.shields.io/badge/NLTK-3.5-blue)

## Table of Contents

- [Repository Structure](#repository-structure)
  - [Data Folder](#data-folder)
  - [src Folder](#src-folder)
- [Project Overview](#project-overview)
  - [Objective](#objective)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Steps](#steps)
  - [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Repository Structure

```
.
├── LICENSE
├── README.md
├── data
│   ├── Sarcasm_Headlines_Dataset_v2.json
│   ├── bbc_data.csv
│   ├── clean_bbc_classification.csv
│   ├── clean_sarcasm_classification.csv
│   ├── data_link.txt
│   ├── evaluation_data.csv
│   ├── evaluation_data_2.csv
│   └── evaluation_data_final.csv
└── src
    ├── 1_DecisionTreeClassifier.ipynb
    ├── 2_RandomForestClassifier.ipynb
    ├── 3_LSTM.ipynb
    ├── 4_Evaluation.ipynb
    ├── preprocessing.ipynb
    ├── stat.ipynb
    └── time_counter.py
```

### Data Folder

The `data` folder contains all the datasets used in the project:

- `Sarcasm_Headlines_Dataset_v2.json`: Dataset from Kaggle used for sarcasm detection.
- `bbc_data.csv`: BBC news dataset.
- `clean_bbc_classification.csv`: Preprocessed BBC news dataset.
- `clean_sarcasm_classification.csv`: Preprocessed sarcasm dataset.
- `data_link.txt`: Contains links to the datasets.
- `evaluation_data.csv`, `evaluation_data_2.csv`, `evaluation_data_final.csv`: Various stages of evaluation data.

### src Folder

The `src` folder contains the Jupyter notebooks and Python scripts used in the analysis:

- `1_DecisionTreeClassifier.ipynb`: Notebook for training and evaluating the Decision Tree model.
- `2_RandomForestClassifier.ipynb`: Notebook for training and evaluating the Random Forest model.
- `3_LSTM.ipynb`: Notebook for training and evaluating the LSTM model.
- `4_Evaluation.ipynb`: Notebook for comparing the models and creating evaluation plots.
- `preprocessing.ipynb`: Notebook for data preprocessing.
- `stat.ipynb`: Notebook for exploring and analyzing dataset statistics.
- `time_counter.py`: Python script with a decorator function to measure runtime.

## Project Overview

### Objective

The objective of this project is to compare three text classification models (Decision Tree, Random Forest, and LSTM) across five different criteria:
1. Performance
2. Robustness
3. Interpretability
4. Computational Cost
5. Ease of Deployment

### Evaluation Metrics

- **Performance**: Measured using accuracy and F1 score.
- **Computational Cost**: Measured using training time in seconds.

### Steps

1. **Data Preprocessing**: Data cleaning and preprocessing are performed in `preprocessing.ipynb`.
2. **Model Training**: Training the Decision Tree, Random Forest, and LSTM models in their respective notebooks.
3. **Evaluation**: Evaluating the models and comparing their performance in `4_Evaluation.ipynb`.
4. **Statistical Analysis**: Analyzing the datasets' statistics in `stat.ipynb`.

### Results

The results of the model evaluations, including accuracy, F1 score, and training times, are saved in the `evaluation_data_final.csv` file. The `4_Evaluation.ipynb` notebook contains visualizations and comparative analysis of the models.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The datasets used in this project were obtained from [Kaggle](https://www.kaggle.com/).
- Special thanks to my thesis advisor and peers for their support and guidance.
