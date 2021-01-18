import csv

QUESTIONS_FILE_PATH = 'sample_data/question.csv'
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def get_all_questions():
    all_questions = []
    with open(QUESTIONS_FILE_PATH) as csv_file:
        #csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            all_questions.append(row)
    return  all_questions