import time, json, os, random, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class User:
  def __init__(self, acc_num):
    self.id = random.randint(111111, 999999)
    self.acc_num = acc_num
    self.holders_name = None
    self.holders_email = None
    self.holders_phone = None
    self.holders_address = None
    self.holders_dob = None

  def create_user(self):
    self.holders_name = input('Enter your name - ')
    self.holders_email = input('Enter your email address - ')
    self.holders_phone = input('Enter your phone number - ')
    self.holders_address = input('Enter your address - ')
    self.holders_dob = input('Enter your Date of Birth (DD-MM-YYYY) - ')


class Account:
  def __init__(self):
    self.account_number = random.randint(1111111111, 9999999999)
    self.account_created_date = datetime.datetime.now()
    self.user = None

  def create(self):
    print("Enter personal details")
    user = User(self.account_number)
    user.create_user()
    self.user = user

    print("\nprocessing......")
    time.sleep(0.4)
    print("""
      -------------------------
      --  Account is created --
      -------------------------
    """)


class Bank:
  _welcome_text = """
    #####################################
    @@@@    WELCOME TO MOHIT BANK    @@@@
    #####################################
    \n
  """
  _bank_functionalities = [
    'Create Account',
    'Close Account',
  ]

  def __init__(self):
    self._welcome_handler()

  def _show_bank_functionality(self):
    print("Choose what you want to do.")
    print("---------------------------")
    for i, functionality in enumerate(self._bank_functionalities):
      print(f'Press {i + 1} for {functionality}')

  def _welcome_handler(self):
    print(self._welcome_text)

  def open(self):
    self._show_bank_functionality()
    choice = input('Enter your choice - ')
    
    if not choice.isnumeric():
      print("wrong input")
      return 
    
    if int(choice) == 1:
      account = Account()
      account.create()

if __name__ == "__main__":
  bank = Bank()
  bank.open()