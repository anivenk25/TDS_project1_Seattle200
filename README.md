# GitHub User Analysis in Seattle

- This project scrapes the GitHub API to identify users in Seattle with over 200 followers, focusing on their bios and repositories.
- An interesting finding is that many users have academic backgrounds, with common phrases like "research scientist at" and "University of Washington" appearing frequently.
- Based on the analysis, I recommend developers consider using JavaScript, which has shown significant popularity and trends indicating high engagement.

## Overview

This project utilizes the GitHub API to scrape data about users located in Seattle who have more than 200 followers. The goal is to analyze user profiles and repositories to uncover trends and insights about the developer community in this region.

## Data Collection Process

1. **API Requests**: I sent GET requests to the GitHub API to retrieve user information and repository details.
2. **Data Filtering**: Users were filtered based on their location (Seattle) and follower count (over 200).
3. **Data Structuring**: The retrieved data was organized into pandas DataFrames for analysis and export.
4. **Saving Results**: The final datasets were saved as CSV files for further analysis and visualization.

## Analysis

During the analysis, I discovered that the GitHub community in Seattle has a strong representation of academic and research-oriented professionals. This indicates that the platform serves as a crucial intersection for both education and technology application.

## Conclusion

The analysis highlights the importance of GitHub as a hub for professionals in academia and industry. Given the rising popularity of JavaScript, I recommend developers focus on this language to enhance their skills and project visibility.

## Future Work

Further research could involve a comparative analysis of user engagement across different programming languages or a deeper dive into the types of projects being developed by users in this demographic.
