import json
import math
import random
def registry(username, password, firstname, lastname, age,change_pass,shift,file_name):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    player_profile = {}
    made_profile = {}
    player_profile['password'] = encrypt(password,shift)
    player_profile['first name'] = encrypt(firstname,shift)
    player_profile['lastname'] = encrypt(lastname,shift)
    player_profile['age'] = encrypt(age,shift)
    player_profile['highscore'] = '0'
    player_profile['changepass'] = encrypt(change_pass,shift)
    made_profile[encrypt(username,shift)] = player_profile

    with open(file_name1, 'r') as read_profile:
        read_data = read_profile.readlines()
        if len(read_data )>0:
            for lets in read_data:
                profile1 = json.loads(lets)
                for user1 in profile1:
                    if decrypt(user1,shift) == username:
                        return f"This Username is already being Used"
    with open(file_name1, 'a') as write_profile:
        write_profile.write(str(json.dumps(made_profile)) + '\n')
        return f'Profile made'
def login(username, password, shift,file_name):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    with open(file_name1, 'r') as read_profile:
        read_data = read_profile.readlines()
        if read_data:
            for line in read_data:
                profile = json.loads(line)
                for user in profile:
                    if decrypt(user,shift) == username:
                        if decrypt(profile[user]['password'],shift) == password:
                            return True
                        else:
                            return f'Incorrect password for {username}'
        return f'Username {username} not found or there are no profiles'
def change_pass(username,new_pass,shift,file_name):
    updated_profiles = []
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    with open(file_name1, 'r') as read_profilee:
        for line in read_profilee:
            profile = json.loads(line)
            username = encrypt(username,shift)
            if username in profile: 
                profile[username]['password'] = encrypt(new_pass,shift)
            updated_profiles.append(profile)

    with open(file_name1, 'w') as write_profile:
        for profile in updated_profiles:
            json.dump(profile, write_profile)
            write_profile.write('\n')

    if any(username in profile for profile in updated_profiles):
        username = decrypt(username,7)
        return f'Password changed successfully for {username}'
    else:
        return f'Username {username} not found or incorrect name/age'
def update_scores(username, update_score,shift, file_name):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    updated_profiles = []
    with open(file_name1, 'r') as read_profilee:
        for line in read_profilee:
            profile = json.loads(line)
            username = encrypt(username,shift)
            if username in profile:
                if profile[username]['highscore']<update_score:
                    profile[username]['highscore'] = update_score
                    profile[username]["recentscore"] = update_score
                else:
                    profile[username]["recentscore"] = update_score
            updated_profiles.append(profile)

    with open(file_name1, 'w') as write_profile:
        for profile in updated_profiles:
            json.dump(profile, write_profile)
            write_profile.write('\n')
   
def leaderboard(file_name,shift):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    g = []
    player_data = []
    position = 1
    with open(file_name1, "r") as file:
        for line in file:
            dict_data = json.loads(line)
            player = list(dict_data.keys())[0]
            highscore = int(decrypt(dict_data[player]['highscore'],shift))
            recent = '  recentscore = ' + decrypt(dict_data[player]['recentscore'],shift) + '\n'
            line = '-----------------------------\n'
            player_data.append({'player': player, 'highscore': highscore, 'recent': recent})
    sorted_players = sorted(player_data, key=lambda x: x['highscore'], reverse=True)
    for player_data in sorted_players:
        highscore = '  Highscore = ' + str(player_data['highscore'])
        profile = str(position),' ',player_data['player'], highscore, player_data['recent'],line
        g.append(''.join(profile))
        position += 1
    return ''.join(g)

def encrypt(data, shift):
    encrypted_text = ""
    for char in data:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                encrypted_text =encrypted_text+ chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                encrypted_text =encrypted_text+ chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text
def decrypt(code, shift):
    return encrypt(code, -shift)
