alphabet = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ ')

mode = input("Encrypt, Decrypt, or Exit: ").lower()

#--------------------------------------------------------------------------------------------------------------------

if mode == "encrypt":
    message = list(input("Enter Your Message: "))
    new_message = str()

    for i in message:
        if i in alphabet:
            new_message = new_message + str(alphabet.index(i)) + "."

    print(new_message)

#--------------------------------------------------------------------------------------------------------------------

if mode == "decrypt":

    message = input("Enter Your Message: ")
    message = message.split(".")
    message.pop(-1)
    new_message = ''

    for index in message:
        index = int(index)
        new_message += alphabet[index]
    print(new_message)

#--------------------------------------------------------------------------------------------------------------------

if mode == "Exit" or "exit":
    pass
