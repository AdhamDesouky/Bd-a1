# Big Data Assignment 1 Documentation

## Introduction
Welcome to the documentation for Assignment 1 of the CSCI461 Introduction to Big Data course at Nile University, Spring 2024. This project revolves around the development of a comprehensive pipeline for processing Google Play Store Reviews data, with the primary objective of conducting sentiment analysis.

## Dataset
The dataset utilized for this assignment comprises app reviews sourced directly from the Google Play Store. Google Play, formerly known as Android Market, serves as the official app store for devices running the Android operating system. It offers users a vast array of applications developed using the Android software development kit (SDK). Notably, Google Play has amassed over 82 billion app downloads and hosts more than 3.5 million published apps, thereby solidifying its position as the largest app store globally.

## Directory Structure
The project directory, labeled as **bd-a1/**, serves as the central hub for all project-related files and resources. Within this directory, a subdirectory named **bd-a1/service-result/** has been designated to store the output files generated by the pipeline.

![bash 1](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/82699162-e18f-4678-afe1-87d5d38f4057)
![bash 2](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/71980fd5-1fd2-4a78-8dc9-3041a4c661f0)
![bash 3](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/a587b5d4-8837-4472-9357-002243c4e397)
![bash 4](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/dc1ee5b9-ef64-461c-9134-bf95b6516efa)
![bash 5](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/e9a6d851-ba22-4cf8-8bfd-bc9c42b66977)


## Dockerfile
The Dockerfile lays the foundation for our project by specifying the base image as Ubuntu. It orchestrates the installation of essential packages required for data processing, including Python3, Pandas, Numpy, Seaborn, Matplotlib, scikit-learn, and Scipy. Additionally, the Dockerfile creates a designated directory within the container and seamlessly transfers the dataset into it, ensuring a streamlined workflow.

## Pipeline Execution
Our pipeline comprises a series of Python scripts, each meticulously crafted to perform specific tasks in the data processing workflow:

1. **load.py**: This script serves as the entry point for the pipeline, reading the dataset and orchestrating the sequential execution of subsequent processing steps.
  ![loadfile](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/aaf8ba87-7603-4eec-867d-a101a13480e3)

2. **dpre.py**: Responsible for preprocessing tasks, including data cleaning, transformation, reduction, and discretization. Upon completion, it saves the resulting processed data as a new CSV file named `res_dpre.csv`.
  ![dpre](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/8cc4c322-053e-4d6b-85aa-29cbeb8a79d7)

3. **eda.py**: This script conducts exploratory data analysis, providing invaluable insights into the dataset. The insights gleaned from this analysis are captured and saved as text files, with each file representing a unique insight (e.g., `eda-in-1.txt`, `eda-in-2.txt`, etc.).
  
4. **vis.py**: Similar to eda.py, this script generates visualizations to aid in data distribution analysis. However, unlike eda.py, the visualizations produced by this script are saved as PNG images, facilitating easier dissemination and interpretation.
  
5. **model.py**: Implements the K-means algorithm on the dataset, facilitating cluster analysis. Upon completion, the script saves the number of records in each cluster as a text file named `k.txt`, providing valuable insights into the dataset's clustering patterns.
  
6. **final_in_container.sh**: This bash script serves as the final step in the pipeline, facilitating the transfer of output files from the container to the local machine. The output files are deposited in the `assignment_output` directory on the local machine, thereby ensuring seamless access to the processed data and analysis results.

## Bonus Achievements
In addition to completing the core requirements outlined in the assignment prompt, we have accomplished the following bonus tasks:

- **Docker Image Push to Docker Hub**: The Docker image generated during this project has been successfully pushed to Docker Hub, ensuring accessibility and reproducibility for future endeavors.

![bonus 1 ](https://github.com/AdhamDesouky/Bd-a1/assets/126396682/d03779cc-ec8c-4c48-92c2-06b69725d8d7)
  




## Contributors
- Adham Desouky
- Omar Hazzaa
- Zeina Salah
- Norseen Ismail
