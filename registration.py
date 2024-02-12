import json
import math
def File_maker(File_name):
    if '.txt' not in File_name:
        with open(File_name+'.txt','a') as Built_file:
            Built_file.write(json.dumps(''))
    else:
        with open(File_name,'a') as Built_file:
            Built_file.write(json.dumps())

def registry(username, password, firstname, lastname, age,file_name):
    player_profile = {}
    made_profile = {}
    player_profile['password'] = password
    player_profile['first name'] = firstname
    player_profile['lastname'] = lastname
    player_profile['age'] = age
    player_profile['highscore'] = '0'
    player_profile['recentscore'] = '0'
    made_profile[username] = player_profile

    with open(file_name+'.txt', 'r') as read_profile:
        read_data = read_profile.readlines()
        if read_data:
            for line in read_data:
                check_profile = json.loads(line)
                if username in check_profile:
                    return f'This Username is already being used'

    with open(file_name+'.txt', 'a') as write_profile:
        write_profile.write(json.dumps(made_profile) + '\n')

def login(username, password, file_name):
    with open(file_name+'.txt', 'r') as read_profile:
        read_data = read_profile.readlines()
        if read_data:
            for line in read_data:
                profile = json.loads(line)
                for user, data in profile.items():
                    if user == username:
                        if data['password'] == password:
                            return True
                        else:
                            return f'Incorrect password for {username}'
        return f'Username {username} not found or there are no profiles'

def change_pass(username, name1, name2, age, file_names):
    updated_profiles = []

    with open(file_names + '.txt', 'r') as read_profilee:
        for line in read_profilee:
            profile = json.loads(line)
            if username in profile:
                if name1 == profile[username]['first name'] and name2 == profile[username]['lastname'] and str(age) == profile[username]['age']:
                    new_pass = input('Enter your new password: ')
                    profile[username]['password'] = new_pass
            updated_profiles.append(profile)

    with open(file_names + '.txt', 'w') as write_profile:
        for profile in updated_profiles:
            json.dump(profile, write_profile)
            write_profile.write('\n')

    if any(username in profile for profile in updated_profiles):
        return f'Password changed successfully for {username}'
    else:
        return f'Username {username} not found or incorrect name/age'
def update_scores(username, update_score, file_names):

    update_score = update_score.strip()
    l2 = float(update_score)
    updated_scores = []

    with open(file_names + '.txt', 'r') as read_profile:
        for line in read_profile:
            if line.strip():  
                profile = json.loads(line)
                if username in profile:
                    g4 = float(profile[username]['highscore'])
                    if g4 < l2:
                        profile[username]['highscore'] = update_score
                        profile[username]['recentscore'] = update_score
                    else:
                        profile[username]['recentscore'] = update_score
                updated_scores.append(profile)

    with open(file_names + '.txt', 'w') as write_profile:
        for profile in updated_scores:
            json.dump(profile, write_profile)
            write_profile.write('\n')

    if any(username in profile for profile in updated_scores):
        return f'Scores updated successfully for {username}'
    else:
        return f'Username {username} not found or incorrect name/age'
