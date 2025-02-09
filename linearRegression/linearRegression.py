class LinearRegression():
    
    def __init__(self, fit_intercept=True, method='normal'):
        '''

        :param fit_intercept: Whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (i.e. data is expected to be centered).
        :param method:
        '''
        self.fit_intercept = fit_intercept
        self.method = method
        self.theta = np.array([0])


    def fit(self, X, y):
        '''
        Function to train and construct the LinearRegression
        :param X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns.
        :param y: pd.Series with rows corresponding to output variable (shape of Y is N)
        :return:
        '''

        X = np.array(X)
        y = np.array(y)
        
        if self.fit_intercept == True:
            m, _ = X.shape
            ones = np.ones((m,1))
            X = np.concatenate((ones,X),1)
        
        #note to self: pinv retuns inverse of matrix when it's available, and pseuo-inverse when it's not
        #https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.9-The-Moore-Penrose-Pseudoinverse/
        self.theta = np.dot(np.linalg.pinv(np.dot(X.T,X)),np.dot(X.T,y))

    def predict(self, X):
        '''
        Funtion to run the LinearRegression on a data point
        :param X: pd.DataFrame with rows as samples and columns as features
        :return: y: pd.Series with rows corresponding to output variable. The output variable in a row is the prediction for sample in corresponding row in X.
        '''
        X = np.array(X)
        
        if self.fit_intercept == True:
            m, _ = X.shape
            ones = np.ones((m,1))
            X = np.concatenate((ones,X), 1)
        
        return np.dot(X,self.theta)

    def plot_residuals(self):
        """
        Function to plot the residuals for LinearRegression on the train set and the fit. This method can only be called when `fit` has been earlier invoked.

        This should plot a figure with 1 row and 3 columns
        Column 1 is a scatter plot of ground truth(y) and estimate(\hat{y})
        Column 2 is a histogram/KDE plot of the residuals and the title is the mean and the variance
        Column 3 plots a bar plot on a log scale showing the coefficients of the different features and the intercept term (\theta_i)

        """
        pass
