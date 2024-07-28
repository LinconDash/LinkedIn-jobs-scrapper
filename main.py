# Importing Libraries
import os
import csv
import os.path
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import time
import json


# Making a class of scrapper
class LinkedIN_Scrapper:

    def __init__(self, location, job_role):
        base_url, target_num = self.load_configs(file="configfile.json")
        search_url = base_url + f"keywords={job_role}&location={location}&refresh=true"
        if type(base_url) is not None:
            print("Base-url is correct !!")
        if target_num != 0:
            print("Target rows is non-zero")

        # Making an output setup
        if not os.path.exists("Data"):
            os.makedirs("Data")
            print("Made an Data directory successfully")
        now = datetime.now()
        output_filename = "Data/jobs-scraped-on-" + now.strftime("%d-%m-%Y") + ".csv"
        header = ["Job_Role", "Company", "Job_location", "Employment_type", "Posted", "Easy_Apply", "Seniority_level",
                  "Industries", "Job_Function"]
        job_data = self.get_job_data(search_url, target_num)
        self.get_output_file(header, output_filename, job_data)
        self.clean_raw_data()
        return

    def get_job_data(self, search_url, target_num):
        response = requests.get(search_url)
        status_code = response.status_code
        if status_code == 200:
            print("Yup the status code is correct !")
        else:
            print("Terminating the program as the requested url status code is not 200 .....")
            exit(0)
        num_jobs = 0
        start = 0
        job_data = []
        tic = time()
        batch_count = 1
        while num_jobs < target_num:
            print(f"Batch {batch_count} of {int(target_num/25)} started ..... ")
            search_url = search_url + f"&start={start}"
            response = requests.get(url=search_url)
            status_code = response.status_code
            data = response.text
            # print(status_code)

            # Lets make the soup out of it.
            soup = BeautifulSoup(data, "lxml")
            # print(soup)
            job_listings = soup.find(name="ul", class_="jobs-search__results-list")
            jobs = job_listings.find_all(name="li")
            for job in jobs:

                # Let's fetch the job data from LinkedIN

                job_title = job.find(name="h3", class_="base-search-card__title").text.strip()
                company = job.find(name="h4", class_="base-search-card__subtitle").text.strip()
                location = job.find(name="span", class_="job-search-card__location").text.strip()
                posted = job.find(name="time", class_="job-search-card__listdate")
                if posted is not None:
                    posted = job.find(name="time", class_="job-search-card__listdate").text.strip()
                employment_type = None
                seniority_level = None
                industries = None
                job_function = None
                easy_apply = None

                # Let's go to the detailed page to extract more informations.
                company_link = job.find(name="a", class_="base-card__full-link")
                # If only the link is given then we get the details.
                if company_link is not None:
                    company_link = job.find(name="a", class_="base-card__full-link").get('href')
                    details_page = requests.get(company_link)
                    details = details_page.text

                    # Let's make another soup out of it.
                    soup2 = BeautifulSoup(details, "lxml")
                    # Let's see if there is an Apply link or not
                    apply = soup2.find(name="button", class_="apply-button")
                    if apply is not None:
                        apply = apply.text.strip()
                        if apply == "Easy Apply" or apply == "Apply":
                            easy_apply = "Yes"
                    else:
                        easy_apply = "No"
                    job_description = soup2.find(name="ul", class_="description__job-criteria-list")
                    if job_description is not None:
                        list_objects = job_description.find_all(name="span", class_="description__job-criteria-text")
                        if list_objects is not None:
                            new_list = [None,None,None,None]
                            index = 0
                            for span in list_objects:
                                new_list[index] = span.text.strip()
                                index += 1
                            seniority_level = new_list[0]
                            employment_type = new_list[1]
                            job_function = new_list[2]
                            industries = new_list[3]
                else:
                    employment_type = None
                    seniority_level = None
                    industries = None
                    job_function = None
                job_data.append(
                    [job_title, company, location, employment_type, posted, easy_apply, seniority_level, industries,
                     job_function])
            start += 25
            batch_count += 1
            num_jobs = start
        toc = time()
        print(f"Fetched the whole data in {(toc - tic):.2f} seconds")
        return job_data

    def load_configs(self, file):
        with open(file) as config_file:
            extractions = json.load(config_file)
            base_url = extractions["url"]
            target_num = extractions["target_rows"]
        return base_url, target_num

    def get_output_file(self, header, filename, job_data):
        with open(filename, mode="w", newline='', encoding="utf-8") as outputfile:
            csv_file = csv.writer(outputfile)
            csv_file.writerow(header)
            csv_file.writerows(job_data)
            print(f"Added a csv file in Data directory successfully named {filename} !!")

    def clean_raw_data(self):
        df = pd.read_csv("Data/jobs-scraped-on-" + datetime.now().strftime("%d-%m-%Y") + ".csv")
        print("Does the data have duplicated rows ", df.duplicated().any())
        df.drop_duplicates(inplace=True, ignore_index=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv("Data/jobs-scraped-on-" + datetime.now().strftime("%d-%m-%Y") + ".csv")
        print("Cleaned data saved to jobs-scraped-on-" + datetime.now().strftime("%d-%m-%Y") + ".csv")
        return


if __name__ == "__main__":
    LinkedIN_Scrapper("India", "Python Developer")