import random


class Person:
    def __init__(self, name, age, financial_condition, place_of_residence):
        self.name = name
        self.age = age
        self.financial_condition = financial_condition
        self.place_of_residence = place_of_residence


class Human(Person):
    def human_information(self):
        if self.place_of_residence.lower() == "no":
            print(f'{self.name}: Hi, my name is {self.name}, and I`m {self.age} years old. '
                  f'My family come to this town,'
                  f'and I want to buy house.')
        else:
            print(f'{self.name}: Hello! My name is {self.name}, I`m {self.age}, and I want to buy my second house.')

    def ansver_propose(self):
        print(f'{self.name}: Ok, i have {self.financial_condition}$. What you can propose?')

    def reaction(self):
        realtor.house_cost()
        self.decision_human = Realtor().houses
        number = random.randint(0, 3)
        for position, house in enumerate(self.decision_human):
            if number == position:
                if self.financial_condition >= house['price']:
                    print(f"{self.name}: I want buy house on {house['place']}")
                    self.house_price = house['price']
                else:
                    print(f"{self.name}: I want buy house in {house['place']}, "
                          f"but I don't have enough money of my own. "
                          f"Can you give me some discount?")
                    self.house_price = house['price']

    def work(self):
        self.need_money = Realtor().final_price
        if self.financial_condition < self.need_money:
            print(f"{self.name}: Hm, I steel haven`t money, but I can take credit.")
            self.buy_decision = 1
        elif self.financial_condition >= self.need_money:
            print(f"{self.name}: Oh, that`s great! I want buy it!")
            self.buy_decision = 1
        else:
            print(f"{self.name}: You know after some thought, "
                  f"I came to the conclusion that I don't want to buy a house right now. Thank you! ")
            self.buy_decision = 0

    def the_end(self):
        self.final_result = Realtor().final_result
        if self.final_result == True:
            self.name_realtor = Realtor().name
            if self.financial_condition < self.need_money:
                self.credit = self.need_money - self.financial_condition
                self.mounth = int(self.credit/7000)
                print(f"\n{self.mounth} mounth later...\n\n{self.name}: My credit is close! Dobby is free elf!")
            else:
                print(f"{self.name}: Thank you, Mr.{self.name_realtor}, I`m happy to listen this!")
        else:
            print(f"\n{self.name}: I must go to the Police, I was fooled :(")


class House:
    def __init__(self):
        self.houses = [
            {"place": 'St.Pablo st.', 'area': 40, 'price': 150000},
            {"place": 'Milka st.', 'area': 60, 'price': 300000},
            {"place": 'Milutenka st.', 'area': 50, 'price': 250000},
            {"place": 'Chreshchatyk st.', 'area': 45, 'price': 200000}
        ]


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name):
        self.name = name
        self.houses = House().houses

    def reprecent(self):
        print(f'{self.name}(R): Hi! My name is {self.name}, '
              f'I`m realtor and i have some very good proposition`s for you.')

    def house_cost(self):
        print(f'{self.name}(R): We have 4 houses with different area:')
        for i in self.houses:
            print(f"    {i['place']}, {i['area']} m2, price - {i['price']}")

    def discount(self):
        self.decision_realtor = human.house_price
        discount_percent = random.randint(0, 20)
        self.final_price = int(self.decision_realtor*((100-discount_percent)/100))
        if discount_percent == 0:
            print(f"{self.name}(R): Sorry but I can`t give you any discount. So, final price is {self.final_price}$ . "
                  f"So, what will you do?")
        else:
            print(f"{self.name}(R): Yes, of course I can give you {discount_percent}% discount. "
                  f"Now price is {self.final_price}$ . So, what will you do?")

    def steal(self):
        self.name_human = human.name
        self.buy_decision = human.buy_decision
        if self.buy_decision == 1:
            print(f"{self.name}(R): Ok, here is the contract number on which you must pay. "
                  f"As soon as the money is transferred, I will contact you.")
            self.steal_chance = random.randint(0, 100)
            if self.steal_chance in range(0, 10):
                print(f"\nAfter 6 hours... \n\nNumber of {self.name} not serviced.")
                self.final_result = False
            else:
                print(f"\nAfter 6 hours... \n\n{self.name}(R): Hey, Mr.{self.name_human}, "
                      f"I received the money and am ready to provide "
                      f"you with ready-made documents and keys at any time.")
                self.final_result = True


if __name__ == '__main__':
    place = {1: 'YES', 2: 'NO'}
    result = random.randint(1, 2)
    money = random.randrange(100000, 200000, 1000)
    human = Human(name='Nazar', age=24, financial_condition=money, place_of_residence=place[result])
    human.human_information()
    realtor = Realtor(name='Frank')
    realtor.reprecent()
    human.ansver_propose()
    human.reaction()
    realtor.discount()
    human.work()
    realtor.steal()
    human.the_end()
