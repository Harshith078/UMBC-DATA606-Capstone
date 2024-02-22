## 1. Title and Author

- **Project Title:** Amazon UK Shoes Content-Based Recommendation System using Product Textual Features
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Harshith Molugu
    
## 2. Background

- **Topic:** Amazon UK Shoes Content-Based Recommendation System using Product Textual Features
- **Overview:** This project aims to develop a recommendation engine tailored for the Amazon UK shoes dataset. Leveraging features extracted from product descriptions, dimensions, and materials, the recommendation system delivers personalized shoe recommendations based on users' preferences and interests.
- **Objectives:**
  1. Utilize textual data to extract meaningful features from shoe products.
  2. Implement content-based filtering to compute item similarity scores.
  3. Generate personalized recommendations for users based on their historical interactions and preferences.
  4. Enhance user experience by providing relevant and tailored shoe recommendations.
  5. Drive sales and conversion by effectively showcasing a diverse range of shoe products to users.

## 3. Data 

- **Data Sources:** The dataset used in this project is sourced from data.world.
- **Data Size:** 13,474 Kb
- **Data Shape:** (11605, 19)
- **Time Period:** Not applicable
- **What does each row represent?** Each row represents a unique shoe product.
- **Data Dictionary:**
  - **Columns Name:** 
    1. title
    2. asin
    3. price
    4. brand
    5. package_dimensions
    6. date_first_available
    7. manufacturer
    8. asin_number
    9. item_model_number
    10. country_of_origin
    11. department
    12. breadcrumbs
    13. outer_material
    14. inner_material
    15. sole
    16. closure
    17. heel_height
    18. heel_type
    19. shoe_width
  - **Data Type:** 
    - String (title, asin, brand, package_dimensions, manufacturer, asin_number, item_model_number, country_of_origin, department, breadcrumbs, outer_material, inner_material, sole, closure, heel_type, shoe_width)
    - Price (price)
    - Date (date_first_available)
    - Numeric (heel_height)
  - **Definition:** 
    - title: Title of the shoe product
    - asin: Amazon Standard Identification Number
    - price: Price of the shoe product
    - brand: Brand of the shoe product
    - package_dimensions: Dimensions of the package containing the shoe product
    - date_first_available: Date when the shoe product was first available on Amazon
    - manufacturer: Manufacturer of the shoe product
    - asin_number: ASIN number of the shoe product
    - item_model_number: Model number of the shoe product
    - country_of_origin: Country of origin of the shoe product
    - department: Department/category of the shoe product
    - breadcrumbs: Navigation path/category hierarchy of the shoe product
    - outer_material: Material used for the outer part of the shoe
    - inner_material: Material used for the inner part of the shoe
    - sole: Material used for the sole of the shoe
    - closure: Closure type of the shoe (e.g., lace-up, strap)
    - heel_height: Height of the heel in centimeters
    - heel_type: Type of heel (e.g., flat, no heel)
    - shoe_width: Width of the shoe (e.g., medium, schmal)
- **Target/Label:** Not specified
- **Features/Predictors:** All columns except for the target/label column (if specified).

## 4.Expected Outcomes

  1. Improved recommendation accuracy by leveraging textual features for content-based filtering.
  2. Increased user engagement and satisfaction through personalized and relevant recommendations.
  3. Boost in sales performance by delivering a diverse range of shoe products tailored to user preferences.
