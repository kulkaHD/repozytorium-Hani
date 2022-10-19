from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, name, last_name, priv_num, email):
        self.name = name
        self.last_name = last_name
        self.priv_num = priv_num
        self.email = email
        
    def __str__(self):
        return f'{self.name} {self.last_name} {self.priv_num} {self.email}'
    @property
    def contact_phone(self):
        return self.priv_num
    def contact (self):
        print (f"Wybieram numer {self.contact_phone} i dzwonię do {self.name} {self.last_name}")
    @property
    def label_length(self):
        return len(self.name) + len(self.last_name)
  

class BusinessContact (BaseContact):
    def __init__(self, job, company, work_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_num = work_num
        self._contact = (f"Wybieram numer {self.work_num} i dzwonię do {self.name} {self.last_name}")
    def __str__(self):  
        return f'{self.name} {self.last_name} {self.job} {self.company} {self.work_num}'
    @property
    def contact_phone(self):
        return self.work_num



def create_contacts(create_card,x):
    card = []
    for i in range(x):
        if create_card == "priv":
            card.append(BaseContact(name = fake.first_name(), last_name = fake.last_name(), priv_num = fake.phone_number(), email = fake.ascii_free_email()))
        elif create_card == "biz":
            card.append(BusinessContact(name = fake.first_name(), last_name = fake.last_name(),priv_num = fake.phone_number(), email = fake.ascii_free_email(), job = fake.job(), company = fake.company(), work_num = fake.phone_number()))
    return card
cardPriv = create_contacts("priv", 3)
cardBiz = create_contacts("biz", 3)


print (cardPriv)
BaseContact.contact(cardPriv[0])
BusinessContact.contact(cardBiz[0])
print(cardBiz[0])
print(cardPriv[0].label_length)
print(cardBiz[0].label_length)