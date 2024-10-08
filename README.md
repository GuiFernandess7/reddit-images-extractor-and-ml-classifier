# Reddit User Image Extractor

![reddit-banner-image](https://github.com/user-attachments/assets/33a3a7ff-51c4-41a1-9799-7bf8c7437aa3)

## Introduction

The Reddit User Image Extractor effectively harnesses ELT processes to gather and store user images from the **amiugly** subreddit. By utilizing the Reddit API, SQLAlchemy, SQLite, and Amazon S3, this application provides a foundation for future machine learning and data processing tasks.

The data collection process is automated on a daily basis using GitHub Actions, ensuring that the database remains up-to-date with the latest user images. This seamless integration of automation not only saves time but also enhances the consistency and reliability of the database.

One potential application of the collected data is to develop a classification model that predicts the gender of individuals in the images. By training a machine learning algorithm on a labeled dataset, the model could analyze visual features to make accurate predictions about the gender of the person in a given photo. This capability could enhance various applications, such as targeted marketing or user profiling in social media platforms.

Overall, this project not only showcases the integration of various tools and technologies but also highlights the potential for further exploration in image classification and data analysis.

## Tools

<img src="https://github.com/user-attachments/assets/cbe55116-f761-41d7-ba32-52dcb426d7de" alt="python" width="100"/>
<img src="https://github.com/user-attachments/assets/a9dd9bf5-1498-4229-8df4-f6d97360a2ed" alt="Jupyter" width="100" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/29a2dbdd-26d5-46d1-95dd-639738cbeadc" alt="SQLite" width="100" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/505b5fde-3343-4096-9b7d-fd9b1bc5f146" alt="SQLAlchemy" width="100" style="margin-right: 50px;"/>
<img src="https://github.com/user-attachments/assets/fe8212df-d398-4073-8268-4fd6a7dea83e" alt="AWS" width="100"/>

<svg class="w-6 h-6" height="40" width="40" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient x1="0%" y1="100%" x2="100%" y2="0%" id="Arch_Amazon-S3-Standard_32_svg__a"><stop stop-color="#1B660F" offset="0%"></stop><stop stop-color="#6CAE3E" offset="100%"></stop></linearGradient></defs><g fill="none" fill-rule="evenodd"><path d="M0 0h40v40H0z" fill="url(#Arch_Amazon-S3-Standard_32_svg__a)"></path><path d="M30.074 22.671l.2-1.301c1.703 1.016 1.735 1.444 1.732 1.46-.004.003-.308.24-1.932-.159zm-10.185-3.733a.995.995 0 01-.992.994.994.994 0 010-1.99c.547 0 .992.448.992.996zm7.869 12.33c0 .123-.495.31-.93.478l-.445.17c-.475.189-1.037.359-1.669.504-1.576.366-3.75.585-5.817.585-5.503 0-8.435-1.009-8.439-1.798L8.256 13.57c1.899 1.452 5.8 2.382 10.641 2.382 4.63 0 9.364-.897 11.584-2.472l-1.366 8.92c-2.871-.874-6.392-2.56-8.132-3.398l-.105-.05.002-.015c0-1.098-.89-1.99-1.983-1.99a1.988 1.988 0 00-1.983 1.99c0 1.097.89 1.99 1.983 1.99.733 0 1.367-.407 1.71-1.002 1.806.868 5.41 2.591 8.356 3.468l-1.205 7.874zm-8.86-23.273c6.676 0 11.857 1.86 11.894 3.465l-.024.148c-.27 1.579-5.352 3.35-11.87 3.35-6.388 0-10.71-1.725-10.89-3.375l-.015-.12c.023-1.678 4.397-3.468 10.904-3.468zm11.538 12.318l1.344-8.76c.001-.026.006-.05.006-.076C31.786 8.674 25.233 7 18.897 7 12.003 7 7 8.883 7 11.477l.003.061 2.468 19.73c0 2.6 7.852 2.732 9.426 2.732 2.137 0 4.394-.228 6.04-.61a12.74 12.74 0 001.81-.548l.432-.167c.844-.321 1.57-.598 1.564-1.331l1.18-7.684c.655.158 1.197.24 1.63.24.58-.001.973-.143 1.21-.428a.982.982 0 00.219-.832c-.127-.681-.923-1.405-2.546-2.327z" fill="#FFF"></path></g></svg>
