#function accept a total area and devide it into areas
def calculateArea(totalArea):
    totalArea = input('Area ? ')
    result = totalArea
#try statement to hundle error when the user itroduce some value which is different of numbers
    try:     
    #if statment give a plan according to area
        if 0 < int(result) < 10:
            print('with this area, you can just think in some workshop to improve your arts skills')
        elif 11 >= int(result) <= 25:
            a = int(result) * 50/100 #living room
            b = int(result) * 25/100 #kitchen
            c = int(result) * 25/100 #bathroom
            print('we suggest for you some sweet studio with three essential pieces')
            print('living room, with area of     ' + str(a) + ' Square Metters')
            print('kithen , with area of         ' + str(b) + ' Square Metters')
            print('bathroom ,  with area of      ' + str(c) + ' Square Metters')
        elif int(result) <= 50:   
            a = int(result) * 30/100 #living room
            b = int(result) * 30/100 #bedroom
            c = int(result) * 20/100 #kithen
            d = int(result) * 20/100 #bathroom
            print('We plan for you a economic beautiful appart: ')
            print('living room    ' + str(a) + ' Metter Square')
            print('Bedroom        ' + str(b) + ' Metter Square')
            print('Kithen         ' + str(c) + ' Metter Square')
            print('bathroom       ' + str(d) + ' Metter Square')
        elif  int(result) >= 50:
            a = int(result) * 25/100 #living room
            b = int(result) * 25/100 #bedroom
            c = int(result) * 25/100 #kithen
            d = c * 50/100 #bathroom
            e = c * 50/100 #dinner room
            print('Plan for your Standing House : ')
            print('living room    ' + str(a) + ' Metter Square')
            print('Bedthroom      ' + str(b) + ' Metter Square')
            print('Kithen         ' + str(c) + ' Metter Square')
            print('bathroom       ' + str(d) + ' Metter Square')
            print('dinner room    ' + str(e) + ' Metter Square')
    except ValueError:
        print('Ops..! is not number')

calculateArea(None)



