from random import randint, choice
import os


def createMatrix():
    encryptionMatrix, decryptionMatrix = [], []
    for row in range(10):
        encryptionRow, decryptionRow = [], []
        for column in range(10):
            encryptionRow.append((row + column) % 10)
            decryptionRow.append((column - row + 10) % 10)
        encryptionMatrix.append(encryptionRow)
        decryptionMatrix.append(decryptionRow)
    return encryptionMatrix, decryptionMatrix


def encryption(text, encryptionMatrix):
    newText = ''
    cipherText = ''
    for character in text:
        if len(str(ord(character))) == 3:
            newText += str(ord(character))
        elif len(str(ord(character))) == 2:
            newText += f"0{str(ord(character))}"
        elif len(str(ord(character))) == 1:
            newText += f"00{str(ord(character))}"
        else:
            print("Invalid input")
            return
    newText.split()
    newList = []
    for index in range(len(newText)):
        newList.append(int(newText[index]))
    newText = newList
    for index in range(len(newText)):
        cipherText += str(encryptionMatrix[newText[index]]
                          [newText[(index + 1) % len(newText)]])

    cipherPlainText = ''
    cipherText.split()
    for index in range(0, len(cipherText), 3):
        cipherPlainText += chr(
            int(f"{cipherText[index]}{cipherText[index + 1]}{cipherText[index + 2]}"))
    return cipherPlainText


def startUp():
    encryptionMatrix, decryptionMatrix = createMatrix()
    runAgain = True
    while runAgain:
        print("Please select an option...")
        print("(A) Encrypt a message")
        print("(B) Decrypt a message")
        print("(C) Encrypt a text file")
        print("(D) Decrypt a text file")
        choice = input("\nYour choice: ")
        if choice.lower() == 'a':
            print("\n\n")
            print(
                f"Encrypted message: {encryption(input('Please enter the message you would like to encrypt: '), encryptionMatrix)}")
        else:
            print(
                "That option was not a valid one. Please try again by choosing a valid option.\n\n\n")
            continue
        runAgain = input(
            "\n\nWould you like to run the program again? [Y / N]: ")
        if runAgain.lower() == 'y':
            renAgain = True
            print("\n\n\n")
        else:
            break
    print("\n\n\nExiting the program...")
    return


if __name__ == '__main__':
    try:
        startUp()
    except KeyboardInterrupt:
        pass
