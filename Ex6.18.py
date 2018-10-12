#Gets number of characters
def get_num_of_characters(inputStr):
    count = 0
    for char in inputStr:
    	count += 1
    return count

#Uses replace function to replace whitespaces
def output_without_whitespace(inputStr):
    inputStr = inputStr.replace(' ','')
    return inputStr

if __name__ == '__main__':
    inputStr = input('Enter a sentence or phrase: ')
    print('You entered:', inputStr)

    print('Number of characters:', get_num_of_characters(inputStr))
    print('String with no whitespace:', output_without_whitespace(inputStr))
