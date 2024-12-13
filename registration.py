import json
import math
import random
def registry(username, password, firstname, lastname, age,change_pass,encryptCode,file_name):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    player_profile = {}
    made_profile = {}
    player_profile['password'] = encrypt(password,encryptCode)
    player_profile['first name'] = encrypt(firstname,encryptCode)
    player_profile['lastname'] = encrypt(lastname,encryptCode)
    player_profile['age'] = encrypt(age,encryptCode)
    player_profile['highscore'] = '0'
    player_profile['changepass'] = encrypt(change_pass,encryptCode)
    made_profile[encrypt(username,encryptCode)] = player_profile

    with open(file_name1, 'r') as read_profile:
        read_data = read_profile.readlines()
        if len(read_data )>0:
            for lets in read_data:
                profile1 = json.loads(lets)
                for user1 in profile1:
                    if decrypt(user1,encryptCode) == username:
                        return f"This Username is already being Used"
    with open(file_name1, 'a') as write_profile:
        write_profile.write(str(json.dumps(made_profile)) + '\n')
        return f'Profile made'
def login(username, password, encryptCode,file_name):
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
                    if decrypt(user,encryptCode) == username:
                        if decrypt(profile[user]['password'],encryptCode) == password:
                            return True
                        else:
                            return f'Incorrect password for {username}'
        return f'Username {username} not found or there are no profiles'
def change_pass(username,new_pass,encryptCode,file_name):
    updated_profiles = []
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    with open(file_name1, 'r') as read_profilee:
        for line in read_profilee:
            profile = json.loads(line)
            username = encrypt(username,encryptCode)
            if username in profile: 
                profile[username]['password'] = encrypt(new_pass,encryptCode)
            updated_profiles.append(profile)

    with open(file_name1, 'w') as write_profile:
        for profile in updated_profiles:
            json.dump(profile, write_profile)
            write_profile.write('\n')

    if any(username in profile for profile in updated_profiles):
        username = decrypt(username,encryptCode)
        return f'Password changed successfully for {username}'
    else:
        return f'Username {username} not found or incorrect name/age'
def update_scores(username, update_score,encryptCode, file_name):
    if '.txt' in file_name:
        file_name1 = file_name
    else:
        file_name1 = file_name + '.txt'
    updated_profiles = []
    with open(file_name1, 'r') as read_profilee:
        for line in read_profilee:
            profile = json.loads(line)
            username = encrypt(username,encryptCode)
            if username in profile:
                if decrypt(profile[username]['highscore'],encryptCode)<update_score:
                    profile[username]['highscore'] = encrypt(update_score,encryptCode)
                    profile[username]["recentscore"] = encrypt(update_score,encryptCode)
                else:
                    profile[username]["recentscore"] = encrypt(update_score,encryptCode)
            updated_profiles.append(profile)

    with open(file_name1, 'w') as write_profile:
        for profile in updated_profiles:
            json.dump(profile, write_profile)
            write_profile.write('\n')
   
def leaderboard(file_name,encryptCode):
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
            highscore = int(decrypt(dict_data[player]['highscore'],encryptCode))
            recent = '  recentscore = ' + decrypt(dict_data[player]['recentscore'],encryptCode) + '\n'
            line = '-----------------------------\n'
            player_data.append({'player': player, 'highscore': highscore, 'recent': recent})
    sorted_players = sorted(player_data, key=lambda x: x['highscore'], reverse=True)
    for player_data in sorted_players:
        highscore = '  Highscore = ' + str(player_data['highscore'])
        profile = str(position),' ',decrypt(player_data['player'],encryptCode), highscore, player_data['recent'],line
        g.append(''.join(profile))
        position += 1
    return ''.join(g)

def encrypt(data,key):
    encrypted = []
    for letter in data:
        if letter in key:
            encrypted.append(key[letter])
    return ''.join(encrypted)
def decrypt(data,key):
    dataList = []
    decrypted = []
    firstKey = len(list(key.values())[0])
    for letter in data:
        dataList.append(letter)
    for i in range(0,int((len(dataList)/firstKey))):
        decrypted.append(list(key.keys())[list(key.values()).index(''.join(dataList[0:firstKey]))])
        del dataList[0:firstKey]
    return f''.join(decrypted)
def codeMaker(codeLength):
    keys = [' ', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    codes = {}
    for letter in keys:
        code = []
        for i in range(codeLength):
            code.append(random.choice(keys))
        codes[letter] = ''.join(code)
    return codes 
