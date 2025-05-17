Project Observations & Insights – Cuisines Dataset

1.Dataset Overview:

The dataset contains restaurant-level data, including country, city, cuisine types, ratings, votes, and price range.

It was cleaned by removing duplicates and rows with missing values to ensure accurate analysis.

2.Country Mapping:

The dataset originally used numerical country codes. These were mapped to actual country names (e.g., 1 → India, 216 → US), helping in more readable and interpretable visualizations.

3.Feature Categorization:

The columns were categorized into:

Categorical Features: Country_name, City, Restaurant Name, Cuisines, Currency

Numerical Features: Votes, Aggregate rating, Price range

4.Top Countries by Restaurant Count:

India has the highest number of restaurants listed, followed by the USA and the UAE.

This indicates the dataset is heavily skewed towards Indian restaurants.

5.Top Cities by Restaurant Count:

New Delhi, Gurgaon, and Noida are among the top cities, again indicating India’s dominance in the dataset.

6.Popular Cuisines:

North Indian, Chinese, and Fast Food are the most frequently served cuisines.

7.Currencies Used:

Multiple currencies are present, showing this dataset is global.

Indian Rupee (INR), Emirati Dirham (AED), and US Dollar (USD) are commonly used.

8.Restaurant Ratings:

Most restaurants have an average rating between 3.0 and 4.5.

Many entries had a 0 rating, likely due to lack of user reviews. These were removed for accurate analysis.

9.Average Ratings by Category:

Country: Some countries have better average ratings than others. For example, Singapore and New Zealand showed high average ratings.

City: Cities like Wellington and Warangal showed higher average ratings.

Cuisines: European, Japanese, and Lebanese cuisines had higher average ratings compared to others.

Currency: Currency-wise, some countries with strong currencies tended to have slightly better ratings, possibly indicating better services or experiences.

10.Discrete Features Analysis:

Has Table Booking:

Most restaurants do not offer table booking.

Has Online Delivery:

A good portion offers online delivery, especially in India.

Is Delivering Now:

Fewer restaurants are marked as currently delivering.

Rating Color and Text:

Rating colors (green, orange, red) and texts (Excellent, Very Good, Good, etc.) give a quick glance into restaurant quality.

Majority fall under "Good" or "Very Good" categories.

11.Online Delivery vs Rating (partially visible in the code):

Restaurants offering online delivery may show some correlation with better ratings, though full insight is not visible in the file.

