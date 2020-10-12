#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random


def create_user(fname, lname, phone, email):
    """
    Function to create a new user
    """
    new_user = User(fname, lname, phone, email)
    return new_user


def create_credential(uname, pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credential(uname, pword, email)
    return new_credential


def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()
def verify_user(first_name,pword):
    checking_user = Credential.check_user(first_name,pword)
    return checking_user

    def save_cred(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()


def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


def del_cred(credential):
    """
    Function to delete all users credentials
    """
    credential.delete_credential()


def display_user():
    """
    Function that returns saved users
    """
    return User.display_users()

def display_cred():
    """
    function that returns saved user credentials
    """
    return Credential.display_credential()


def main():

    print("Welcome to your Password Locker, choose your path from the list of allowed actions")

    while True:
        print("Allowed Actions: \n 1 - create a new user account with a Personal password\n 2 - create a new user account with a auto-generated password\n 3 - Display all user accounts \n 4 - Login  to an existing Account\n ex -exit the contact list \n")

        short_code = input().lower()

        if short_code == '1':
            print("New User")
            print("-"*10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            print("Enter Password ...")
            pword = input()