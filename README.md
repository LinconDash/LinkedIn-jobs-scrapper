# LinkedIn-jobs-scrapper
## Overview
The LinkedIn Job Scraper is a powerful webscrapping program designed to scrape real-time job postings from the `LinkedIn` platform.
It processes and cleans the scraped data, exporting it to a CSV file, enabling users to conveniently view and apply for jobs in Excel based on their interests. 
It provides a lot of data such as which company, what job-role, when posted, and so on. It will really be helpful to the students of all different domain to find the jobs according to their own domain. <br>
By automating the process of job data extraction, this scraper allows users to quickly gather and organize job postings based on specific criteria such as job type and location. The scraper uses BeautifulSoup for parsing HTML and LXML content, and pandas for data manipulation. 
The output is a clean CSV file, which can be easily opened in Excel for further analysis and job application tracking. This tool simplifies the job search process, saving users valuable time and effort. 
This tool is ideal for job seekers looking to automate and optimize their job search process on LinkedIn, providing a structured and efficient way to gather job information.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Technical Details](#technical-details)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Example Usage](#example-usage)
- [Output](#output)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Real-time Job Scraping:** Fetches up-to-date job postings from LinkedIn.
- **Data Cleaning:** Ensures the scraped data is well-organized and free from duplicates.
- **CSV Export:** Exports the cleaned data into a CSV file for easy use in Excel.
- **Customizable Inputs:** Allows users to specify the region/country and job type.

For Example : If you are a CSE major and have interest in Python search `Python Devloper` in `India`. Or if you have interest in Data try searching `Data Analyst` in `United States`. Or if you want to be in Markeing try searching `Digital Marketing` in `China`.  

## Prerequisites
- Python 3.7 and above
- Stable internet connection
- Excel (Any other spreadsheet software that supports csv file)
- LinkedIn account (optional)
- Git (for installation)

## Technical Details:
- **Language:** Python
- **Libraries:** BeautifulSoup or bs4, pandas, os, csv, requests, json
- **Output:** CSV file with detailed jobs information based on the input parameters
- **Input Parameters:** Region/country, job-type

## Installation
Before you begin, ensure you have the following prerequisites already installed on your system.

### 1. Clone the Repository
First, clone the repository to your local machine using Git. Open open your terminal and run the following command:
``` bash
git clone https://github.com/LinconDash/LinkedIn-jobs-scrapper.git
cd LinkedIn-jobs-scrapper
```

### 2. Create a Virtual Environment (Optional)
It's a good practice to use a virtual environment to manage your project dependencies because the packages and site-packages donot get installed on your local enviroment thereby reducing both storage and dependencies issues. Run the following commands to create and activate a virtual environment:
- In Windows
``` bash
python -m venv venv
venv\Scripts\activate
```
- In Mac
``` bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages listed according to their versions in the `requirements.txt` file using pip:
``` bash
pip install -r requirements.txt
```

## Example Usage
- **Configuration:** Modify the `configfiles.json` file to set your LinkedIn credentials and other parameter like "target-rows" which can be used to fetch the no. of rows of data you want. 
- **Open main.py:** Open up the `main.py` and see the main section just like the image below:
  - <img src="Images/Input Image.png" >
  - Example : Searching `Python Developer` Jobs in `India`
  - Please feel free to try different kinds jobs you have interest in and also the location according to your choice.
- **Run main.py:** Run the file `main.py` by using the terminal:
``` bash
python main.py
# or python3 main.py
```

## Output



