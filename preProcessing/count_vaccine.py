vaccine_count = 0
vax_count = 0
jab_count = 0

# open the text file
with open('sub_count_input.txt','r', encoding='utf-8') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # checking for the relevant terms           
            if word == "vaccine" or word == "Vaccine" or word == "vaccines" or word == "Vaccines" or word == "vaccination":
                vaccine_count += 1
            elif word == "vaccinations" or word == "vacine":
                vaccine_count += 1
            elif word == "vax" or word == "Vax" or word == "vaxx":
                vax_count += 1
            elif word == "jab" or word == "Jab":
                jab_count += 1

print("Number of times \"vaccine\" occurs: ", vaccine_count)
print("Number of times \"vax\" occurs: ", vax_count)
print("Number of times \"jab\" occurs: ", jab_count)