# 2a
class Picture:
    # PRIVATE Description : STRING
    # PRIVATE Width : INTEGER
    # PRIVATE Height : INTEGER
    # PRIVATE FrameColour : STRING

    def __init__(self, description, width, height, frameColour):
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frameColour = frameColour
    
    # 2b
    def GetDescription(self):
        return self.__description
    
    def GetHeight(self):
        return self.__height
    
    def GetWidth(self):
        return self.__width
    
    def GetColour(self):
        return self.__frameColour
    
    # 2c
    def SetDescription(self, description):
        self.__description = description

# 2d
# DECLARE array[0:99] : ARRAY OF Picture
array = [None for i in range(100)]

# 2e
def ReadData():
    global array
    count = 0

    try:
        with open("./2021/October-November/Pictures.txt", "r") as file:
            line = file.readline()
            file.seek(0)
            while line:
                desc = file.readline().strip()
                width = file.readline().strip()
                height = file.readline().strip()
                col = file.readline().strip()
                obj = Picture(desc, width, height, col)

                temp = file.tell()
                line = file.readline()
                file.seek(temp)
                
                array[count] = obj
                count += 1
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Some other error occurred!")

    return count + 1

# 2f
# Main Program
pictures = ReadData()

# 2g
col = input("Enter colour of picture:\n>>> ").lower()
width = int(input("Enter maximum width:\n>>> "))
height = int(input("Enter maximum height:\n>>> "))

for i in range(pictures - 1):
    flag = True
    picture = array[i]

    if col != (picture.GetColour()).lower(): flag = False
    if width < int(picture.GetWidth()): flag = False
    if height < int(picture.GetHeight()): flag = False

    if flag:
        print(f"Picture Details:\nDescription: {picture.GetDescription()}\nWidth: {picture.GetWidth()}\nHeight: {picture.GetHeight()}\n")