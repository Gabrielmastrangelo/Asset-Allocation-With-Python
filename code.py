#Importing the libraries
import yfinance as yf
import pandas as pd

 # Dictionary with the asset classes and the chosen etfs with their respective weights to represent them in our portfolio
securities = {
    'US_Stocks' : ['IVV', 0.5],
    'Bonds' : ['AGG', 0.3],
    'TIPs' : ['TIP', 0.2],
}


def getPortfData(portfolio):
    '''
    The function gets a dictionary as input, compile the data from Yahoo Finance, 
    and calculates the historical return of the individual ETFs and the porfolio chosen
    
    Input: Dictionary, "Assets Classes: [ETF, Weight]"
    Output: DataFrame, with the historical performance of each individual ETF and the Portfolio
    '''
    
    def gettingData(dictionary_port):
        '''
        This function will get a dictionary as input and will compile the data from the individual classes
        and return it in a list.
        '''
        basket_returns = []
        
        for asset in dictionary_port.items():
            security = yf.Ticker(asset[1][0]).history(period="max") #Get all the historical prices available 
            returns = security['Close'].pct_change().dropna() #Calculates the percentual change
            basket_returns.append(returns) #Put the new compiled data in a list
            
        return basket_returns #Return the list
    
    def calculatingPortPerform(assets_returns, dictionary_port):
        '''
        This function gets the historical performance of the individual assets and the dictionary with the
        weights and assets, in order to compute the portfolio performance
        '''    
        hist_returns = pd.concat(assets_returns, 1) #Concatenate all the historical performance of the individual assets
        hist_returns = hist_returns.dropna()        #Each asset has a different time series, this we merge them in order to 
                                                    #compute only the time when each all of them were available
        hist_returns = (hist_returns+1).cumprod()   #We compute the accumuled return
        hist_returns.columns = dictionary_port.keys()     #We assign the value for each class in the dataframe as their tickers
        hist_returns["Portfolio"] = hist_returns.shape[0]*[0] #Create a column with 0s
        
        for i in range(len(hist_returns.columns)-1):
            '''
            Here we weighted each individual asset performace by their share in our portfolio
            and them we sum it in our portfolio.
            '''
            asset_return = hist_returns[hist_returns.columns[i]]
            weight = list(dictionary_port.items())[i][1][1]
            hist_returns.Portfolio = asset_return*weight + hist_returns.Portfolio

        return hist_returns - 1 #Return the data frame with all the historical returns

    historical_data = gettingData(portfolio) #call the first function
    portfolioData = calculatingPortPerform(historical_data, portfolio)
    
    return portfolioData
    
dados = getPortfData(securities) #We call the function
dados.to_excel('dataPortfolio.xlsx') #We save the data frame in a Excel File

#We create our plot
plot = dados.plot(title = 'Passive Investing Portfolio Example') 
vals = plot.get_yticks()
yaxis = plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
fig = plot.get_figure()
#And we save it as a png file
fig.savefig('Plot.png')