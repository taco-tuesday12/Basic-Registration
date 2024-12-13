import registration
# make a .txt file
# how to use the registration system, encryptCode is a ment to be a dictionary you insert in that has all the key binds and the values as the encryption code 
print(registration.registry(username, password, firstname, lastname, age,change_pass,encryptCode,file_name))
# how to login
if registration.login(username, password, encryptCode,file_name) == True:
# how to use change password
print(registration.change_pass(username,change_pass,new_pass,encryptCode,file_names))
# how to update the scores
print(registration.update_scores(username, update_score, encryptCode,file_names))
print(registration.leaderboard(file_name,encryptCode))
# codeLength is how long you want the encryption code for each letter its an integer and you can use the dictionary it prints as the eccryptCode
print(registration.codeMaker(codeLength))
