import registration
# make a .txt file
# how to use the registration system, shift is related to the encryption just pick a number 1-25
print(registration.registry(username, password, firstname, lastname, age,change_pass,shift,file_name))
# how to login
if registration.login(username, password, shift,file_name) == True:
# how to use change password
print(registration.change_pass(username,change_pass,new_pass,shift,file_names))
# how to update the scores
print(registration.update_scores(username, update_score, shift,file_names))
print(registration.leaderboard(file_name,shift))
