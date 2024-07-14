age = 25
height_cm = 170
is_member = True
username = "john_doe"
friends_list = ["alice", "bob", "charlie"]
guest_list = ["john_doe", "jane_doe", "alice"]
print("Logical Operators with Mixed Data Types:")
is_adult_and_member = (age >= 18) and is_member
print(f"Is an adult and a member: {is_adult_and_member}")
is_in_guest_or_friends_list = (username in guest_list) or (username in friends_list)
print(f"Is the username in the guest list or friends list: {is_in_guest_or_friends_list}")
height_check_and_not_friends = (height_cm < 180) and not (username in friends_list)
print(f"Height less than 180 cm and not in friends list: {height_check_and_not_friends}")
is_not_in_any_list = not (username in friends_list or username in guest_list)
print(f"Is not in any list (friends or guest): {is_not_in_any_list}")
complex_condition = (age >= 18) and (username in guest_list or height_cm < 180)
print(f"Complex condition (adult and (in guest list or height < 180 cm)): {complex_condition}")
another_complex_condition = (username in guest_list and not is_member) or (height_cm > 160)
print(f"Another complex condition ((in guest list and not a member) or height > 160 cm): {another_complex_condition}")

