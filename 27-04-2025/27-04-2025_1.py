class Home():
    def __init__(self):
        self.property_size="1200sqft"
        self.loc="abc-123-werr-234"
        self.house_left=100
    def buy_house(self,cu_name):
        print("congratulations", cu_name,"youhave secured a house of size", self.property_size, "at location", self.loc)
        self.house_left-=1
        print("house left:",self.house_left)


build_man=Home()
build_man.buy_house("vp")
build_man.buy_house("vivek")
build_man.buy_house("adicto")
build_man.buy_house("anuj")
build_man.buy_house("wadhwa")

