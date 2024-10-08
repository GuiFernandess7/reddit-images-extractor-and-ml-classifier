# Reddit User Image Extractor

## Introduction

The Reddit User Image Extractor effectively harnesses ELT processes to gather and store user images from the 'amiugly' subreddit. By utilizing the Reddit API, SQLAlchemy, SQLite, and Amazon S3, this application provides a foundation for future machine learning and data processing tasks.

The data collection process is automated on a daily basis using GitHub Actions, ensuring that the database remains up-to-date with the latest user images. This seamless integration of automation not only saves time but also enhances the consistency and reliability of the database.

One potential application of the collected data is to develop a classification model that predicts the gender of individuals in the images. By training a machine learning algorithm on a labeled dataset, the model could analyze visual features to make accurate predictions about the gender of the person in a given photo. This capability could enhance various applications, such as targeted marketing or user profiling in social media platforms.

Overall, this project not only showcases the integration of various tools and technologies but also highlights the potential for further exploration in image classification and data analysis.

## Tools

- Database:

  - SQLAlchemy
  - SQLite
  - Amazon S3

- Deploy

  - Github actions
