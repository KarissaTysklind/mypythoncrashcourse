guest_list = ["Queen Elisabeth II", "David Attenborough", "Morgan Freeman", "Jordan Petterson"]
invite = "{}, you are invited to join me for dinner {}\n"
date = "tomorrow"

#Define a function to create the invites:
def dinner_invite(guest_list, date):
    for guest in guest_list:
        print(invite.format(guest, date))

        
dinner_invite(guest_list, date)

#Oh no, Morngan Freeman cannot make it tomorrow:
print("\nUnfortunately {} is not available tomorrow :( \n".format(guest_list[-2]))

#what about Jake Gyllen haal:
guest_list[-2] = "Jake Gyllenhaal" 

dinner_invite(guest_list, date)


