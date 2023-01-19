guest_list = ["Queen Elisabeth II", "David Attenborough", "Morgan Freeman", "Jordan Petterson"]
invite = "{}, you are invited to join me for dinner {}"

def dinner_invite(guest_list, date):
    for guest in guest_list:
        print(invite.format(guest, date))


dinner_invite(guest_list, "tomorrow")