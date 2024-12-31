# IPL Match Winner Prediction Project 🏏

## Overview
This project predicts the winning probabilities of the teams playing in an IPL (Indian Premier League) match using key match parameters. It leverages **Logistic Regression**, achieving an accuracy of **81.2%**.

## Features
The model takes the following inputs to generate predictions:
1. **Batting Team**: The team currently batting.
2. **Bowling Team**: The team currently bowling.
3. **Host City**: The city where the match is being played.
4. **Target Score**: The total runs the batting team needs to win.
5. **Current Score**: Runs scored by the batting team so far.
6. **Overs Completed**: Number of overs bowled in the innings.
7. **Wickets Out**: Number of wickets lost by the batting team.

## Dataset
The dataset used for this project was sourced from Kaggle:  
[IPL 2008 to 2021 All Match Dataset](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset).  

It contains detailed match data spanning IPL seasons from 2008 to 2021. The dataset was cleaned and preprocessed before being used to train the model.

## Approach
1. **Data Preprocessing**:
   - Cleaned and prepared the dataset.
   - Applied feature engineering to extract useful attributes like runs left, balls left, and current/required run rates.
   - One-hot encoded categorical features (Batting Team, Bowling Team, and Host City).

2. **Model Training**:
   - Utilized **Logistic Regression** for classification.
   - Split the data into training and testing sets.
   - Evaluated the model's performance using metrics like accuracy.

3. **Prediction**:
   - The model predicts probabilities for each team:
     - **Batting Team Winning Probability**
     - **Bowling Team Winning Probability**

## Results
- **Model Accuracy**: 81.2% on the test dataset.
- The model effectively predicts match outcomes based on the given inputs, providing insights into match scenarios.

## Website 🌐
Explore the live version of this project and predict match outcomes directly on the website:  
**[IPL Match Winner Prediction](https://github.com/SimranS22/IMWPWebsite)**  

## Repository Contents
This repository includes:
1. **Jupyter Notebook**: Contains the entire codebase for data processing, model training, and evaluation.
2. **CSV Files**: Datasets used to train and test the model.

## How to Use
Open the project in **GitHub Codespaces** for a seamless development experience:
- Navigate to your repository on GitHub.
- Click the **Code** button and select **Codespaces**.
- Use the pre-configured environment to run the Jupyter Notebook and analyze the results.
