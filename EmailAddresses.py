def get_emails():
    email_list = []
    user_input = input("Email address: ")
    while(user_input != 'q'):
        email_list.append(user_input)
        user_input = input("Email address: ")
    else:
        return email_list


def get_names_and_domains(email_list):
    names_and_domains = []
    for email in email_list:
        temp = email.split('@')
        names_and_domains.append(tuple(temp))
    return names_and_domains


def main():
    email_list = get_emails()
    print(email_list)
    names_and_domains = get_names_and_domains(email_list)
    print(names_and_domains)

main()