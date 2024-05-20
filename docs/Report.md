# Amazon UK Shoes Content-Based Recommendation System using Product Textual Features

- **Project Title:** Amazon UK Shoes Content-Based Recommendation System using Product Textual Features
- **Prepared for:** University Of Maryland, Baltimore County (UMBC)
- **Under:** Professor Dr. Chaojie (Jay) Wang
- **Author Name:** Harshith Molugu

[GitHub](https://github.com/Harshith078/UMBC-DATA606-Capstone)

[LinkedIn](www.linkedin.com/in/harshith-molugu)

[YouTube](https://youtu.be/mcBpTh3_peY)

[PPT](https://github.com/Harshith078/UMBC-DATA606-Capstone/blob/main/docs/606_Capstone_Final_Presentation.pptx)

## Dataset Background

The project leverages a dataset sourced from data.world, specifically tailored for the Amazon UK shoes market. The dataset comprises various product features, including textual descriptions, dimensions, materials, and more.

## Research Questions

1. How can textual data from product descriptions enhance the recommendation system for Amazon UK shoes?
2. What machine learning models and natural language processing techniques can be effectively used to develop a content-based recommendation system?
3. How can personalized recommendations improve user engagement and drive sales?

## Data Overview

- **Data Size:** 13,474 Kb
- **Data Shape:** (11605, 19)
- **Time Period:** Not applicable
- **Each row represents:** A unique shoe product.

### Data Dictionary

- **title:** Title of the shoe product
- **asin:** Amazon Standard Identification Number
- **price:** Price of the shoe product
- **brand:** Brand of the shoe product
- **package_dimensions:** Dimensions of the package containing the shoe product
- **date_first_available:** Date when the shoe product was first available on Amazon
- **manufacturer:** Manufacturer of the shoe product
- **asin_number:** ASIN number of the shoe product
- **item_model_number:** Model number of the shoe product
- **country_of_origin:** Country of origin of the shoe product
- **department:** Department/category of the shoe product
- **breadcrumbs:** Navigation path/category hierarchy of the shoe product
- **outer_material:** Material used for the outer part of the shoe
- **inner_material:** Material used for the inner part of the shoe
- **sole:** Material used for the sole of the shoe
- **closure:** Closure type of the shoe (e.g., lace-up, strap)
- **heel_height:** Height of the heel in centimeters
- **heel_type:** Type of heel (e.g., flat, no heel)
- **shoe_width:** Width of the shoe (e.g., medium, narrow)

## Features

- Extracted features from textual descriptions, such as material, dimensions, and product categories.
- Utilized TF-IDF (Term Frequency-Inverse Document Frequency) for textual data transformation.

## Exploratory Data Analysis (EDA)

![image](https://github.com/Harshith078/UMBC-DATA606-Capstone/assets/114626348/3450cc97-ccfd-4263-b26b-2aa58c00bc46)
- **Keyword Analysis from Product Descriptions:** The word cloud reveals the most prominent terms used in the shoe descriptions with "Shoes," "Sneaker," "Women," "Men," and "Running" standing out. This indicates a diverse product range with potential focus areas for further analysis or targeted marketing.

![image](https://github.com/Harshith078/UMBC-DATA606-Capstone/assets/114626348/dcde17c2-755b-41f6-bfdf-d5dc2813bac2)
- **Pricing Strategy by Top Brands:** The horizontal bar chart indicates that brands like MBT and Lottusse have higher price points on average, suggesting a positioning towards the premium market segment. This could inform stock selection or promotional strategies based on brand tiering.

![image](https://github.com/Harshith078/UMBC-DATA606-Capstone/assets/114626348/eab3a54a-c0f6-4f81-91c4-93d8c6bcfed6)
- **Feature Importance in Product Listings:** The bar chart showcases the relative importance of product features based on their TF-IDF scores. Features such as "Women," "Shoes," "Sneaker," and "Running" have the highest scores, implying these terms are crucial in distinguishing products. Such insights could drive the refinement of recommendation algorithms.


## Model Training

### Models for Analysis

- Singular Value Decomposition (SVD)

### Training and Development

- Implemented TF-IDF for feature extraction.
- Trained the SVD model on the dataset.
- Evaluated the model using RMSE (Root Mean Squared Error).


### Web App Development

![image](https://github.com/Harshith078/UMBC-DATA606-Capstone/assets/114626348/e75c1fe3-efd5-486e-82bf-37f579e7f70e)

- Developed a web application using Streamlit to showcase the recommendation system.
- Integrated the trained model to provide real-time shoe recommendations based on user input and preferences.

## Conclusion

- The content-based recommendation system effectively utilized textual features to enhance recommendation accuracy.
- Personalized recommendations led to increased user engagement and satisfaction.
- The project demonstrated the potential of natural language processing and machine learning in improving product recommendations and driving sales.
