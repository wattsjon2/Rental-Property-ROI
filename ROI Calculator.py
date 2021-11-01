import os
os.system('cls' if os.name == 'nt' else 'clear')


class ROI():
    """
    The ROI Class will have the ability to take in expesnses and income as well as calculate cash flow and cash on cash ROI
    
    Attributes for Garage():
    - income:
        rental income
        laundry
        storage
        misc

    - expenses:
        tax
        insurance
        utilities
        HOA
        lawn/snow care
        vacancy
        repairs
        capital expenditure
        property mangament
        mortgage
    
    The functions in Garage():
    
    update income
    update expenses
    calculate cashflow and cash on cash ROI
    """
    
    def __init__(self, income = 0, expenses = 0, upfront = 0, dictInc = {"Rental Income" :0, "Misc Income" : 0}, dictExp = {"Tax(%)" : 0, "Insurance($)": 0, "Utilities($)": 0, "HOA Fees($)": 0, "lawn or snow care($)": 0, "Vacancy(%)": 0, "Capital expenditures(%)": 0, "Property Management(%)":0, "Mortgage($)":0 }, dictUpfront = {"Down Payment": 0, "Closing Cost":0, "Refurbishment Cost": 0, "Other": 0}):
        self.income = income
        self.expenses = expenses
        self.upfront = upfront
        self.dictInc = dictInc
        self.dictExp = dictExp
        self.dictUpfront = dictUpfront


    def printIncome(self):
        i = 1
        totalinc = sum(self.dictInc.values())
        print(f'Your total income is ${totalinc}')
        print('Here are your current income sources')
        for key, value in self.dictInc.items():
            print('{0}: {1:<15}${2:<6}'.format(i,key,value))
            i += 1
    def updateIncome(self):
        response = input('What would you like to update? Please input the number. To see the updated expense table enter "view". To go back enter "back"  ')
        if response.lower() not in ['1','2','back','view']:
            print('Please enter a valid choice')
            self.updateIncome()
        elif response.lower() == 'back':
            pass
        elif response.lower() == 'view':
            self.printIncome()
            self.updateIncome()
        elif response.lower() == '1':
            responseIncUpdate = input("What is your rental income, rounded to the nearest dollar? ")
            if responseIncUpdate.isnumeric() == False:
                print('please enter a number, rounded to the nearest dollar')
                self.updateIncome()
            else:
                self.dictInc['Rental Income'] = int(responseIncUpdate)
                self.income = sum(self.dictInc.values())
                self.updateIncome()

        elif response.lower() == '2':
            responseIncUpdate = input("What is your misc income, rounded to the nearest dollar? ")
            if responseIncUpdate.isnumeric() == False:
                print('please enter a number, rounded to the nearest dollar')
                self.updateIncome()
            else:
                self.dictInc['Misc Income'] = int(responseIncUpdate)
                self.income = sum(self.dictInc.values())
                self.updateIncome()
    
    def printExpenses(self):
        if self.income == 0:
            print('Your income has not be completed yet, it is recommended to complete that first')
        i = 1
        print(f'Your total expenditure is ${self.expenses}')
        print('Here are your current expenses')
        for key, value in self.dictExp.items():
            if "$" in key:
                print('{0}: {1:<25}${2:<6}'.format(i,key,value))
            else:
                print('{0}: {1:<25}%{2:<6}'.format(i,key,value))
            i += 1

    def updateExpenses(self):
        dictExpkey = {1: "Tax(%)",2: "Insurance($)",3: "Utilities($)",4: "HOA Fees($)",5: "lawn or snow care($)",6 : "Vacancy(%)",7 : "Capital expenditures(%)",8: "Property Management(%)",9: "Mortgage($)"}
        response = input('What would you like to update? Please input the number. To see the updated expense table enter "view". To go back enter "back" ')
        if response.lower() not in ['1','2','3','4','5','6','7','8','9','back','view']:
            print('Please enter a valid choice')
            self.updateExpenses()
        elif response.lower() == 'back':
            pass
        elif response.lower() == 'view':
            self.printExpenses()
            self.updateExpenses()
        else:
            updateItem = dictExpkey.get(int(response))
            if "$" in updateItem:
                responseExpUpdate = input(f"What is your {updateItem}, rounded to the nearest dollar? ")
            else:
                responseExpUpdate = input(f"What is your {updateItem}, rounded to the nearest percent? ")

            if responseExpUpdate.isnumeric() == False:
                print('please enter a whole number')
                self.updateExpenses()
            else:
                self.dictExp[updateItem] = int(responseExpUpdate)
                totalExp = 0
                for key, value in self.dictExp.items():
                    if "$" in key:
                        totalExp += int(value)
                    else:
                        totalExp += int(value)/100 * self.income
                self.expenses = totalExp
                self.updateExpenses()


    def viewItems(self):
        print(f' the income is set to: ${self.income}')
        print(f' The expenses are set to: ${self.expenses}')
        print(f' The upfront costs are set to: ${self.upfront}')

    def calcCashFlow(self):
        cashFlow = int(self.income) - int(self.expenses)
        print(f'Your monthly cash flow is ${cashFlow}')

    def printUpfrontCosts(self):
        i = 1
        print(f'Your total expenditure is ${self.upfront}')
        print('Here are your current upfront costs')
        for key, value in self.dictUpfront.items():
            print('{0}: {1:<25}${2:<6}'.format(i,key,value))
            i += 1

    def updateUpfrontCosts(self):
        dictUpfrontkey = {1: "Down Payment",2: "Closing Cost",3: "Refurbishment Cost",4: "Other"}
        response = input('What would you like to update? Please input the number. To see the updated expense table enter "view". To go back enter "back"  ')
        if response.lower() not in ['1','2','3','4','back','view']:
            print('Please enter a valid choice')
            self.updateUpfrontCosts()
        elif response.lower() == 'back':
            pass

        elif response.lower() == 'view':
            self.printUpfrontCosts()
            self.updateUpfrontCosts()
        else:
            updateItem = dictUpfrontkey.get(int(response))
            responseUpfrontUpdate = input(f"What is your {updateItem}, rounded to the nearest dollar? ")

            if responseUpfrontUpdate.isnumeric() == False:
                print('please enter a whole number')
                self.updateUpfrontCosts()
            else:
                self.dictUpfront[updateItem] = int(responseUpfrontUpdate)
                self.upfront = sum(self.dictUpfront.values())
                self.updateUpfrontCosts()

    def calcROI(self):
        roiDec = ((int(self.income) - int(self.expenses))*12)/int(self.upfront)
        roiPercent = round(roiDec*100,2)
        print(f'The ROI is: {roiPercent}%')

    def calcReqInc(self):
        desiredROI = input('What would you like for a return on investment, rounded to the nearest percent ')
        if desiredROI.isnumeric() == False:
                print('please enter a whole number')
                self.calcReqInc()
        else:
            dollarval = 0
            percentval = 0
            dictExp = {"Tax(%)" : 0, "Insurance($)": 0, "Utilities($)": 0, "HOA Fees($)": 0, "lawn or snow care($)": 0, "Vacancy(%)": 0, "Capital expenditures(%)": 0, "Property Management(%)":0, "Mortgage($)":0 }
            for key, value in self.dictExp.items():
                if "$" in key:
                    dollarval += value
                else:
                    percentval += value
            percentval = percentval/100
            requiredIncome = (dollarval + (self.upfront * int(desiredROI))/1200)/(1-percentval)
            requiredIncome = round(requiredIncome,2)
            print(f'The minimum monthly income to get a {desiredROI}% ROI is ${requiredIncome}')




def run():
    
    newROI = ROI()
    

    while True:
        response = input("what would you like to do? 1: update income/2: update expenses/3: update upfront costs/4: calculate cash flow/5: calculate ROI/6: Find a desired ROI/7: Quit. Please enter the corrosponding number ")
        
        if response.lower() not in ['1','2','3','4','5','6','7','8']: #membership check
            response = input('Please enter THE NUMBER of your choice')     
        
        if response.lower() == '7':
            print('Thanks for using Bigger Pockets!')
            break
        
        elif response.lower() == '1':
            newROI.printIncome()
            newROI.updateIncome()

        elif response.lower() == '2':
            newROI.printExpenses()
            newROI.updateExpenses()
            
        elif response.lower() == '4':
            newROI.calcCashFlow()

        elif response.lower() == '5':
            newROI.calcROI()

        elif response.lower() == '8':
            newROI.viewItems()
        
        elif response.lower() == '3':
            newROI.printUpfrontCosts()
            newROI.updateUpfrontCosts()

        elif response.lower() == '6':
            newROI.calcReqInc()

run()