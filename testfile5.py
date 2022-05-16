
#running on a program with mixed spacing

def loan_yearly(): #comment at the back will be ignored too
    loan=     ask_loan()
    interest  =ask_interest() 
    yearly_mon   =     ask_pay('year')
    calculations(loan, interest,    yearly_mon  ,'Years' )
    
def loan_monthly()  :
    loan    = ask_loan()
    interest  =   ask_interest()
    monthly_mon      =ask_pay('month')
    calculations( loan, interest ,monthly_mon,         'Month' )

def ask_pay(x) :
    
    pay=input ('How much are you going to pay per ' + x + ":" )
    
    print('blahblah' +x+ "blahblah" )
    print("blah" +x + 'blah')

    #detect valid reserved words
    while check_value(pay) ==     False :
        print   ('***Try again***')
        pay= input  ("How much are 67 you going to pay per " + x+':')
    
    return pay


