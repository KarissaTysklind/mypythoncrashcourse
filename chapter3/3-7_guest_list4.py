guest_list = ["Queen Elisabeth II", "David Attenborough", "Morgan Freeman", "Jordan Petterson"]
invite = "{}, you are invited to join me for dinner {}\n"
date = "tomorrow"

#Define a function to create the invites:
def dinner_invite(guest_list, date):
    for guest in guest_list:
        print(invite.format(guest, date))

#Oh no, Morngan Freeman cannot make it tomorrow:
#print("\nUnfortunately {} is not available tomorrow :( \n".format(guest_list[-2]))

#what about Jake Gyllen haal:
guest_list[-2] = "Jake Gyllenhaal" 

#There is more space in the table:

#print("Hello everyone, we have found a bigger table so we have decided to invite a few more people.\n")

new_guests = ["Michael Kane", "Tom Hardy", "Zandra Bullock"]
guest_list.insert(0, new_guests[0])
guest_list.insert(2, new_guests[1])
guest_list.append(new_guests[-1])
#dinner_invite(guest_list, date)

# I can only invite 2 people for dinner:

print("Unfortunately I can only afford to invite two of you #skint\n")
#print(guest_list)

def uninvite_guest(guest_list):
    while len(guest_list) > 2:
        uninvited_guest = guest_list.pop()
        print ("Sorry, {}, but you are now uninvited to my dinner.\n".format(uninvited_guest))

uninvite_guest(guest_list)

print("My new guest list is:")
for guest in guest_list:
    print(guest)

dinner_invite(guest_list, date)

del guest_list[0]
del guest_list[0]

print(guest_list)