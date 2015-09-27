import csv
import HTMLParser


def load_data(reader):
    tmp = []
    for row in reader:
        tmp.append(row)
    return tmp


def clean_text_fields(data):
    for row in data:
        for col in row:
            row[col] = row[col].upper()


def clean_zip_codes(data):
    for row in data:
        if len(row['zip']) < 5:
            row['zip'] = '0' + row['zip']


def clean_html_from_data(data):
    for row in data:
        for col in row:
            row[col] = row[col].replace("&NBSP;", " ")
            row[col] = row[col].replace("&nbsp;", " ")


def save_large_contributions(data, writer):
    for row in data:
        if int(row['amount']) > 1000:
            writer.writerow(row)



reader = csv.DictReader(open('data/sample.csv', 'r'))
writer = csv.DictWriter(open('data/sample-clean.csv', 'w'), reader.fieldnames)

data = load_data(reader)

writer.writeheader()


clean_text_fields(data)
clean_zip_codes(data)
clean_html_from_data(data)
save_large_contributions(data, writer)