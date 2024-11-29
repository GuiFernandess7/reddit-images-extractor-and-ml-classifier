# Reddit User Image Extractor

![reddit-banner-image](https://github.com/user-attachments/assets/33a3a7ff-51c4-41a1-9799-7bf8c7437aa3)

## Introduction

The Reddit User Image Extractor effectively harnesses ELT processes to gather and store user images from the **amiugly** subreddit. By utilizing the Reddit API, SQLAlchemy, SQLite, and Amazon S3, this application provides a foundation for future machine learning and data processing tasks.

The data collection process is automated on a daily basis using GitHub Actions, ensuring that the database remains up-to-date with the latest user images. This seamless integration of automation not only saves time but also enhances the consistency and reliability of the database.

One potential application of the collected data is to develop a classification model that predicts the gender of individuals in the images. By training a machine learning algorithm on a labeled dataset, the model could analyze visual features to make accurate predictions about the gender of the person in a given photo. This capability could enhance various applications, such as targeted marketing or user profiling in social media platforms.

This project not only showcases the integration of various tools and technologies but also highlights the potential for further exploration in image classification and data analysis.

## ELT Process

![Untitled-2024-11-02-2027](https://github.com/user-attachments/assets/86155e77-5a89-4d38-b4a7-dbda9b122c48)

1. **Reddit API (Image Data Collection)**: The initial collection of image URLs is performed through the Reddit API. Metadata, including image URLs, is stored in an SQLite database, which includes a column named `img_url` to hold the image addresses.

2. **Python Application (URL Extraction and Storage)**: A Python script processes the extracted URLs and stores the initial data in an SQLite database hosted on Amazon S3. This database serves as a central repository for the image data, allowing easy updates and labeling.

3. **DBeaver (Data Labeling)**: In DBeaver, I review and label each image as either `M` (Male) or `F` (Female). For images that no longer exist, you can leave the URL as `NULL`, which prevents unnecessary downloads. After labeling, a Python script updates the SQLite file on S3 with the new labels.

4. **Google Colab (Image Download)**: In Colab, the image download process begins by reading the updated SQLite database and filtering only valid URLs (non-NULL values). The script then downloads the images as JPG files and stores them on Google Drive, ensuring that only accessible images are considered for training and inference.

5. **Inference in Colab (Gender Classification)**: During the inference phase, the model uses the images stored in Google Drive and associates each image with its respective label (`M` or `F`) by matching the image `id` with the database records. This association allows the model to classify the images based on the pre-assigned labels in the SQLite database.

This two-step validation process — first in DBeaver and later in Colab — ensures that only relevant and accessible image URLs are processed and labeled, optimizing the dataset and model performance.

## Tools

<img src="https://github.com/user-attachments/assets/cbe55116-f761-41d7-ba32-52dcb426d7de" alt="python" width="60"/>
<img src="https://github.com/user-attachments/assets/a9dd9bf5-1498-4229-8df4-f6d97360a2ed" alt="Jupyter" width="60" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/29a2dbdd-26d5-46d1-95dd-639738cbeadc" alt="SQLite" width="60" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/505b5fde-3343-4096-9b7d-fd9b1bc5f146" alt="SQLAlchemy" width="60" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/fe8212df-d398-4073-8268-4fd6a7dea83e" alt="AWS" width="60"/>
<img src="https://github.com/user-attachments/assets/4c034feb-4da7-4edb-8b28-d966d25d0163" alt="Bucket" width="60"/>
