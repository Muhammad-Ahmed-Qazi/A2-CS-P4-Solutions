import struct

# 2a
class ProductUDT():
    def __init__(self):
        self.ProductID = 0
        self.ProductName = ""

ProductStack = [ProductUDT() for i in range(50)]
TopPointer = -1

# 2b
def push(Product):
    global TopPointer

    if TopPointer == 49:
        print("Stack overflow! Unable to add more products.")
    else:
        TopPointer += 1
        ProductStack[TopPointer] = Product

def pop():
    global TopPointer

    if TopPointer == -1:
        print("Stack underflow! No products to remove.")
        return -1
    else:
        data = ProductStack[TopPointer]
        TopPointer -= 1
        return data

def EncodeShipment():
    try:
        with open("../../Documents/Try Folder/shipment_data.txt", "r") as file:
            while True:
                try:
                    line = file.readline().strip()
                    line = line.split(" ")
                    thisRecord = ProductUDT()
                    thisRecord.ProductID = line[0]
                    thisRecord.ProductName = line[1]
                    push(thisRecord)
                except: break
        # File will be automatically closed when "with" block ends.
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Some other error!")

def DecodeShipment():
    binFormat = "i46s"
    size = struct.calcsize(binFormat)
    
    with open("../../Documents/Try Folder/shipment_data.dat", "wb") as file:
        # Initialisation of file
        for count in range(50):
            productID = 0
            productName = ""
            record = struct.pack(binFormat, productID, productName.encode())
            file.write(record)
    # File will be automatically closed when "with" block ends.

    with open("../../Documents/Try Folder/shipment_data.dat", "+rb") as file:
        # Saving data in file
        result = pop()
        file.seek(0)
        count = 0
        while result != -1:
            record = file.read(size)
            productID, productName = struct.unpack(binFormat, record)
            if productID == 0:
                record = struct.pack(binFormat, int(result.ProductID), result.ProductName.encode())
                file.seek(size * count)
                file.write(record)
            else:
                print("Data is already there!")
            count += 1
            result = pop()
    # File will be automatically closed when "with" block ends.

# 2c
def RetrieveProductName(product_id):
    flag = False
    binFormat = "i46s"
    size = struct.calcsize(binFormat)

    with open("../../Documents/Try Folder/shipment_data.dat", "+rb") as file:
        offset = (product_id - 1) * size
        file.seek(offset)
        try:
            record = file.read(size)
            read_id, read_name = struct.unpack(binFormat, record)
            while read_id != product_id:
                record = file.read(size)
                read_id, read_name = struct.unpack(binFormat, record) 
        
            if read_id == product_id: 
                return read_name.decode()
        except:
            pass

        if not flag: print("Product not found!")
    # File will be automatically closed when "with" block ends.

# 2d
# Main program
EncodeShipment()
DecodeShipment()
print(RetrieveProductName(7))