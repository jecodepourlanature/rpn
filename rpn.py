import geopandas as gpd

class rpn:
    
    def __init__(self,path):
        self.data=self.loadData(path)
    
    def loadData(self,path): #Charger un shape (ou autre)
        df=gpd.read_file(path)       
        return df 
    
    def observateurs(self):
        return sorted(list(self.data.observ.unique()))