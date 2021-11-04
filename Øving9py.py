# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:02:30 2021

@author: Thomas
"""

#Øving 8 oppgave b
class Spørsmål:
    def __init__(self, prompt, svar, svar_alt):
        self.prompt = prompt
        self.svar = svar
        self.svar_alt = svar_alt

         
              
    def __str__(self):
        resultat = self.svar_alt
        for count, value in enumerate(self.svar_alt):
            resultat = self.prompt
            print(count, value)
        return f"{resultat}"
    
    
    def sjekk_svar(self,svar):
        temp = self.svar == svar
        return temp
    def svar_tekst(self):
        return self.svar_alt[self.svar]
        

            
    
   
def read_lines_and_return_question():
    liste_med_spørsmål = []
    with open("sporsmaalsfil.txt","r", encoding="UTF8") as fil:
        for linje in fil:
            linje = linje.strip()        
            linjeliste = linje.split(":")
            
            prompt = linjeliste[0]
            svar = linjeliste[1]
            svar = svar.strip()
            svar_alt = linjeliste[2]
            svar_alt = svar_alt.replace("[]", "")
            nyesvar = svar_alt.split(",")
            
            
            
            liste_med_spørsmål.append(Spørsmål(prompt, int(svar), nyesvar))
        return liste_med_spørsmål
    


      
if __name__ == "__main__":
    spillere = {
        "spiller 1: " : 0,
        "spiller 2: " : 0
        }
    
    liste_med_spm = read_lines_and_return_question()
    for i in liste_med_spm:
        print(i)
        for spiller in spillere:
            svar = int(input(f"{spiller}"))
            if i.sjekk_svar(svar):
                spillere[spiller] += 1
        print(i.svar_tekst())
print(spillere)
                
    

            
            

        



        

