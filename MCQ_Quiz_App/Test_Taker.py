list_of_names=[]
list_of_email=[]
users_list=[list_of_names,list_of_email]
class TestTaker:
    def __init__(self):
        pass
        
    def register(self):
        name=self.name()
        mail_ID=self.email()
        #contact=self.contact_num()
    
    def name(self):
        print("Enter name")
        name=input()
        self.name=name
        list_of_names.append(name)
           
    def email(self):
        print("enter the mail address")
        email_add=input()
        import re
        if(re.search("^[a-zA-Z]+[0-9]+.*@gmail.com$",email_add)):
            list_of_email.append(email_add)
            self.email=email_add
        else:
            print("emailID must start with an alphabet, then it should have one or more digit and should have a domain @gamil.com")
            
                
            
            
            



        