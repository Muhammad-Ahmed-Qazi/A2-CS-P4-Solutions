# 3a
class Employee:
    # PRIVATE HourlyPay : REAL
    # PRIVATE EmployeeNumber : STRING
    # PRIVATE JobTitle : STRING
    # PRIVATE PayYear2022 : ARRAY[0:51] OF REAL

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay
        self.__EmployeeNumber = EmployeeNumber
        self.__JobTitle = JobTitle
        self.__PayYear2022 = [0.0 for i in range(52)]
    
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self, WeekNo, HoursNo):
        WeekPay = self.__HourlyPay * HoursNo
        self.__PayYear2022[WeekNo - 1] = WeekPay
    
    def GetTotalPay(self):
        return sum(self.__PayYear2022)

# 3b
class Manager(Employee):
    # PRIVATE BonusValue : REAL

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue
    
    def SetPay(self, WeekNo, HoursNo):
        HoursNo += HoursNo * (self.__BonusValue / 100)
        super().SetPay(WeekNo, HoursNo)
    
# Main program

# 3c
# DECLARE EmployeeArray : ARRAY[0:7] OF Employee
EmployeeArray = [None for i in range(8)]

try:
    with open("./2023/May-June/Employees.txt", "r") as file:
        for i in range(8):
            HourlyPay = float(file.readline().strip())
            EmployeeNumber = file.readline().strip()
            ThirdLine = file.readline().strip()
            try:
                ThirdLine = float(ThirdLine)
                BonusValue = ThirdLine
                JobTitle = file.readline().strip()
            except:
                BonusValue = -1.0
                JobTitle = ThirdLine
            if BonusValue == -1.0:
                EmployeeArray[i] = Employee(HourlyPay, EmployeeNumber, JobTitle)
            else:
                EmployeeArray[i] = Manager(HourlyPay, EmployeeNumber, JobTitle, BonusValue)
    # file.close() # with statement has already closed the file.
except FileNotFoundError:
    print("File not found!")
except:
    print("Some other error!")

# 3d
def EnterHours():
    # global EmployeeArray
    CurrEmployeeNumber = 0
    j = -1
    DataDict = {}

    try:
        with open("./2023/May-June/HoursWeek1.txt", "r") as file:
            for i in range(8):
                EmployeeNumber = file.readline().strip()
                HoursNo = float(file.readline().strip())
                DataDict[EmployeeNumber] = HoursNo
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Some other error!")
    
    for key in DataDict.keys():
        j = -1
        while CurrEmployeeNumber != key:
            j += 1
            CurrEmployeeNumber = EmployeeArray[j].GetEmployeeNumber()
            if j == 8: break
        
        # print(j)
        Item = EmployeeArray[j]
        Item.SetPay(1, DataDict[key])

# 3e
EnterHours()
for Item in EmployeeArray:
    print(f"Employee no. {Item.GetEmployeeNumber()}: ${round(Item.GetTotalPay(), 1)}")    