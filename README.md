![Jupyter](https://github.com/user-attachments/assets/f8733152-4793-4a54-9598-d2b6bf1cd63f)# Reddit User Image Extractor

![reddit-banner-image](https://github.com/user-attachments/assets/33a3a7ff-51c4-41a1-9799-7bf8c7437aa3)

## Introduction

The Reddit User Image Extractor effectively harnesses ELT processes to gather and store user images from the 'amiugly' subreddit. By utilizing the Reddit API, SQLAlchemy, SQLite, and Amazon S3, this application provides a foundation for future machine learning and data processing tasks.

The data collection process is automated on a daily basis using GitHub Actions, ensuring that the database remains up-to-date with the latest user images. This seamless integration of automation not only saves time but also enhances the consistency and reliability of the database.

One potential application of the collected data is to develop a classification model that predicts the gender of individuals in the images. By training a machine learning algorithm on a labeled dataset, the model could analyze visual features to make accurate predictions about the gender of the person in a given photo. This capability could enhance various applications, such as targeted marketing or user profiling in social media platforms.

Overall, this project not only showcases the integration of various tools and technologies but also highlights the potential for further exploration in image classification and data analysis.

![Uploading <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><path d="M109.766 7.281a7.691 7.691 0 01-1.09 4.282 7.583 7.583 0 01-3.262 2.949 7.49 7.49 0 01-4.34.62 7.525 7.525 0 01-3.953-1.913A7.642 7.642 0 0195.137 5a7.606 7.606 0 012.629-3.531 7.509 7.509 0 014.136-1.461 7.51 7.51 0 015.422 1.996 7.627 7.627 0 012.438 5.273zm0 0" fill="#767677"/><path d="M65.758 96.79c-20.098 0-37.649-7.364-46.766-18.267a49.95 49.95 0 0018.102 24.254 49.251 49.251 0 0028.676 9.215 49.279 49.279 0 0028.675-9.215 49.917 49.917 0 0018.094-24.254C103.406 89.426 85.855 96.79 65.758 96.79zm0 0M65.75 25.883c20.098 0 37.652 7.367 46.766 18.265a49.95 49.95 0 00-18.102-24.253 49.27 49.27 0 00-28.672-9.22 49.27 49.27 0 00-28.672 9.22A49.909 49.909 0 0018.97 44.148C28.102 33.27 45.652 25.883 65.75 25.883zm0 0" fill="#f37726"/><path d="M38.164 117.984a9.671 9.671 0 01-1.371 5.399 9.5 9.5 0 01-9.59 4.504 9.405 9.405 0 01-4.98-2.418 9.671 9.671 0 01-2.809-4.797 9.73 9.73 0 01.313-5.567 9.624 9.624 0 013.328-4.453 9.466 9.466 0 0112.043.688 9.63 9.63 0 013.066 6.648zm0 0" fill="#989798"/><path d="M21.285 23.418a5.53 5.53 0 01-3.14-.816 5.627 5.627 0 01-2.618-5.672 5.612 5.612 0 011.407-2.95 5.593 5.593 0 012.789-1.664 5.46 5.46 0 013.238.184 5.539 5.539 0 012.586 1.969 5.66 5.66 0 01-.399 7.129 5.557 5.557 0 01-3.867 1.82zm0 0" fill="#6f7070"/></svg>Jupyter.svg…]()

## Tools

- Database:

  - SQLAlchemy
  - SQLite
  - Amazon S3

- Deploy

  - Github actions
