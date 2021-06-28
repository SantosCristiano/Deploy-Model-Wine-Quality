import pickle 

class WineQuality( object ):
    def __init__( self ):
        self.free_sulfur_scaler = pickle.load( open( '/Users/santo/repos/Deploy/model_wine_quality.pkl', 'rb'))
        self.total_sulfur_scaler = pickle.load( open( '/Users/santo/repos/Deploy/model_wine_quality.pkl', 'rb'))
        
    
    def data_preparation( self, df ):
        # rescaling free sulfur
        df['free sulfur dioxide'] = self.free_sulfur_scaler.transform( df[['free sulfur dioxide']].values )
        
        # rescaling total sulfur
        df['total sulfur dioxide'] = self.total_sulfur_scaler.transform( df[['total sulfur dioxide']].values )
        
        return df