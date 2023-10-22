import random
def do_x_percent(n):
    chance = random.randint(0,99)
    return chance < n

_last_choice = "?"
def choose_character(include_str, exclude_str=''):
    global _last_choice
    chosen_character = random.choice(include_str)
    while chosen_character == _last_choice or chosen_character in exclude_str:
        chosen_character = random.choice(include_str)

    _last_choice = chosen_character
    return chosen_character

def rand_digit(exclude_str=''):
    return choose_character('0123456789', exclude_str)

def rand_vowel(exclude_str=''):
    return choose_character('aeiou', exclude_str)

def rand_consonant(exclude_str='qz'):
    return choose_character('bcdfghjklmnpqrstvwyz', exclude_str)

def gen_first_name():
    name = rand_consonant().upper() + rand_vowel()

    for i in range(random.randint(1, 2)):
        name += rand_consonant()
        name += rand_vowel()

    return name

def gen_last_name():
    name = random.choice(['', '', '', '', '', 'de ', 'el '])
    name += rand_consonant().upper() + rand_vowel()

    for i in range(random.randint(2, 3)):
        name += rand_consonant()
        name += rand_vowel()
        if do_x_percent(20):
            name += rand_vowel()

    return name

def gen_default_email(first_name, last_name):
    compacted_last = last_name.replace(' ', '')
    if do_x_percent(60):
        email = first_name[0].lower() + compacted_last[:4].lower()
        num = random.randint(1,7)
        email += f'{num:03d}@plattsburgh.edu'
    else:
        email = first_name.lower() + compacted_last[0].lower()
        domain = random.randint(1,3)
        if domain == 1:
            email += '@gmail.com'
        if domain == 2:
            email += '@yahoo.com'
        if domain == 3:
            email += '@msn.com'

    return email

def gen_phone_number():
    phone_number = '+' + str(random.randint(1,42))

    phone_number += ' '
    phone_number += rand_digit('0')
    for i in range(2):
       phone_number += rand_digit()

    phone_number += ' '
    for i in range(random.randint(3,4)):
       phone_number += rand_digit()

    phone_number += ' '
    for i in range(random.randint(3,4)):
       phone_number += rand_digit()

    return phone_number

def gen_pastimes():
    pastime_set = set()
    num_pastimes = random.randint(0, 4)

    for i in range(num_pastimes):
        pastime = random.choice(
            ['tennis', 'piano', 'farming', 'fishing',
             'coding', 'swimming', 'singing', 'airplanes', 'dancing',
             'reading', 'saxophone', 'cards', 'hiking', 'bicycling', 'running',
             'javelin', 'sewing', 'painting', 'poetry'])
        pastime_set.add(pastime)

    pastime_string = ""
    first_time = True
    for pastime in pastime_set:
        if first_time:
            first_time = False
        else:
            pastime_string += ', '
            first_time = False
        pastime_string += pastime

    return pastime_string




# Assignment 13 Source File Generator
# DO NOT MODIFY

class Person:
    def __init__(self):
        self.first_name = gen_first_name()
        self.last_name = gen_last_name()
        self.email = gen_default_email(self.first_name, self.last_name)
        self.phone_number = gen_phone_number()
        self.pastimes = gen_pastimes()
    def __str__(self):
        ret = f'{self.first_name} {self.last_name}, {self.email}, {self.phone_number}'
        if len(self.pastimes) > 0:
          ret += f', {self.pastimes}'
        return ret
    def __lt__(self, other):
        return self.first_name < other.first_name
    def as_transmitted(self):
        return str(self)
    def as_received(self):
        receive_string = self.as_transmitted()

        # These are our "typical" random transmission errors :)
        if do_x_percent(80):
            receive_string = receive_string.replace('nn', 'nnn')
        if do_x_percent(40):
            receive_string = receive_string.replace('+', '++')
        if do_x_percent(60):
            receive_string = receive_string.replace('00', '0O')
        if do_x_percent(40):
            receive_string = receive_string.replace('.com', '_dot_com')
        if do_x_percent(20):
            receive_string = receive_string.replace('swimming', 'swiming')
        if do_x_percent(20):
            receive_string = receive_string.replace('plattsburgh', 'platsburgh')
        if do_x_percent(20):
            receive_string = receive_string.replace('plattsburgh', 'plattsburg')
        if do_x_percent(20):
            receive_string = receive_string.replace('plattsburgh', 'platsburg')
        if do_x_percent(20):
            receive_string = receive_string.replace('plattsburgh', 'plattsberg')
        if do_x_percent(20):
            receive_string = receive_string.replace(' ', '_', 7)

        return receive_string

# Example People and how they are garbled
random.seed(1)
people = [Person() for x in range(20)]
for person in sorted(people):
    print(person)
    print(person.as_received())






# Assignment 13 Source File Generator
# DO NOT MODIFY

# Creates a population of Person objects
# Writes them uncorrupted to source_file.txt
# Writes them as received to as_received[123].txt
# Most records go into only one file but some are duplicated in two files
def make_files(my_name, record_count=100):
    random.seed(hash(my_name))

    people = [Person() for x in range(record_count)]

    source_file = open('source.txt', 'w')
    received_file1 = open('as_received1.txt', 'w')
    received_file2 = open('as_received2.txt', 'w')
    received_file3 = open('as_received3.txt', 'w')

    all_files = [source_file, received_file1, received_file2, received_file3]

    for file in all_files:
        file.write('Name, Email, Phone, Pastimes\n')

    source_file_line_count = 0
    received_file1_line_count = 0
    received_file2_line_count = 0
    received_file3_line_count = 0
    for person in sorted(people):
        source_file.write(person.as_transmitted() + '\n')
        source_file_line_count += 1

        # These are all 3-bit numbers that have either 1 or 2 bits turned on
        #   with a bias to a single bit
        choice = random.choice([1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 3, 5, 6])
        if choice & 1:
            received_file1.write(person.as_received() + '\n')
            received_file1_line_count += 1
        if choice & 2:
            received_file2.write(person.as_received() + '\n')
            received_file2_line_count += 1
        if choice & 4:
            received_file3.write(person.as_received() + '\n')
            received_file3_line_count += 1

    print(f'source_file written with {source_file_line_count} lines')
    print(f'received_file1 written with {received_file1_line_count} lines')
    print(f'received_file2 written with {received_file2_line_count} lines')
    print(f'received_file3 written with {received_file3_line_count} lines')

    for file in all_files:
        file.close()



# Run this to make your data files

# Put in YOUR name
# Generate 20-50 records to debug and 100000 for your final code check
make_files(my_name='Lili Gunderson', record_count=1000000)

def read_and_clean_data(input_file_path):
    cleaned_data = set()
    with open(input_file_path, 'r') as file:
        header_row = file.readline().strip()
        for line in file:
            entry = line.strip()
            cleaned_entry = entry

            
            cleaned_entry = cleaned_entry.replace('nnn', 'nn')
            cleaned_entry = cleaned_entry.replace('++', '+')
            cleaned_entry = cleaned_entry.replace('0O', '00')
            cleaned_entry = cleaned_entry.replace('_dot_com', '.com')
            cleaned_entry = cleaned_entry.replace('swiming', 'swimming')
            cleaned_entry = cleaned_entry.replace('platsburg', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('platsburgh', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('platsberg', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('_', ' ')
            cleaned_entry = cleaned_entry.replace('plattsburg', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('plattsberg', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('plattsburghh', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('plattsbeurghhh', 'plattsburgh')
            cleaned_entry = cleaned_entry.replace('plattsburghh', 'plattsburgh')

            cleaned_data.add(cleaned_entry)

    return header_row, sorted(cleaned_data)

def write_cleaned_data(header, data, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(header + '\n') 
        for entry in data:
            file.write(entry + '\n') 

def compare_files(file_path1, file_path2):

    header1, data1 = read_and_clean_data(file_path1)
    header2, data2 = read_and_clean_data(file_path2)

    
    return header1 == header2 and data1 == data2

source_data_file = 'source.txt'
received_data_files = ['as_received1.txt', 'as_received2.txt', 'as_received3.txt']
cleaned_data_file = 'cleaned.txt'


for received_file in received_data_files:
    header, cleaned_data = read_and_clean_data(received_file)
    write_cleaned_data(header, cleaned_data, received_file)


header, source_data = read_and_clean_data(source_data_file)
write_cleaned_data(header, source_data, cleaned_data_file)

if compare_files(cleaned_data_file, source_data_file):
    print('The files are identical.')
else:
    print('The files are not identical.')
