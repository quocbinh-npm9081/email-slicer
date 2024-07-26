
def emailProcess(email : str):#quocbinh@gmail.com
    email_username = email[0:email.index("@")] #quocbinh
    email_domain = email[email.index("@")+1:] #gmail.com
    print(f"username: {email_username} \n")
    print(f"email_domain: {email_domain}")

def main():
    email = input("Please enter your email: ").strip()
    emailProcess(email)

if __name__ == "__main__":
    main()
