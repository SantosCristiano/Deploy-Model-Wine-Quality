import pickle

class WineQuality( object ):
    def __init__( self ):
        self.free_sulfur_scaler = pickle.load( open('/Users/santo/repos/Wine-Quality/deploy/free_sulfur_scaler.pkl', 'rb') )
        self.free_sulfur_scaler = pickle.load( open('/Users/santo/repos/Wine-Quality/deploy/total_sulfur_scaler.pkl', 'rb') )
        
    def data_preparation( self, df ):
        # rescaling free sulfur
        df1['free sulfur dioxide'] = self.free_sulfur_scaler.transform( df1[['free sulfur dioxide']].value )
        # rescaling total sulfur
        df1['total sulfur dioxide'] = self.total_sulfur_scaler.transform( df1[['total sulfur dioxide']].values )
        
        return df