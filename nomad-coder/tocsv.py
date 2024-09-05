import csv

job_title = [
    'Title',
    'Company',
    'Location',
    'Salary',
    'Link',
]

def save_to_csv(filename, jobs):
    filename = filename + '.csv'
    f = open(filename, mode='w', encoding='utf-8')

    writter = csv.writer(f)

    # write headers to target csv file.
    writter.writerow(job_title)

    for job_row in jobs:
        writter.writerow(job_row.values())
    
    f.close()

    return filename
