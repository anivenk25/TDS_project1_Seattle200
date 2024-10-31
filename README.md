# GitHub User Analysis in Seattle

 `````

  ██████ ▓█████ ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████ 
▒██    ▒ ▓█   ▀▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀ 
░ ▓██▄   ▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███   
  ▒   ██▒▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄ 
▒██████▒▒░▒████▒▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░
░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░   ░        ░    ░ ░ ▒  ░ ░ ░  ░
░  ░  ░     ░    ░   ▒    ░        ░        ░ ░      ░   
      ░     ░  ░     ░  ░                     ░  ░   ░  ░                                                                                                                             
`````                  

- To scrape the GitHub API, I used Python with the requests library to send GET requests for user data in Seattle. I filtered users with over 200 followers by examining the API response for relevant attributes like bios and repositories. I implemented pagination to gather comprehensive data and stored the results in a structured format for analysis.
- An intriguing insight from the analysis is the prevalence of academic backgrounds among GitHub users in Seattle. Many bios featured phrases such as "research scientist at" and "University of Washington," highlighting a strong link between academia and the tech industry. This suggests that local universities significantly contribute to the region’s skilled workforce, fostering innovation and research.
- Based on my findings, I recommend developers embrace JavaScript and R for their projects. JavaScript shows significant popularity, reflecting strong community engagement, while R appeals to those focused on data science and analytics. Utilizing both languages can enhance versatility and open opportunities for collaboration, allowing developers to effectively address diverse project requirements and industry demands.
  
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
