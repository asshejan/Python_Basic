class calculator:
    brand = 'casio M550'

    def add(num1, num2):
        res = num1 + num2
        return res
    def multi( num1, num2):
        res = num1 * num2
        return res

    def deduct(self, num1, num2):
        if(num1>num2):
            return num1 - num2
        elif(num2 > num1):
            return num2 - num1
        else:
            return 0
    
    def devide(self, num1, num2):
        return num1/num2
    
    print(add(10, 19))
    print(multi(10, 3))


    

