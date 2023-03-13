# Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
#converting any codes (or aliases) therein to their corresponding emoji.
#See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

#First install package : pip install emoji
import emoji
user_answer=input('Input: ') #The name has to be between ::, pex :money_bag:
output=emoji.emojize(user_answer)
print('Output: ',output)



