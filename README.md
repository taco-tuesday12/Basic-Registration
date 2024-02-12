import registration
# make a .txt file
# how to use the registration system
print(registration.registry(username, password, firstname, lastname, age,file_name))
# how to login
if registration.login(username, password, file_name) == True:
# how to use change password
print(registration.change_pass(username, name1, name2, age, file_names))
# how to update the scores
print(registration.update_scores(username, update_score, file_names))
