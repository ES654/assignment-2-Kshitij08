def accuracy(y_hat, y):
    """
    Function to calculate the accuracy
    
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the accuracy as float
    """
    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert(y_hat.size == y.size)
    
    # TODO: Write here
    
    count = 0
    
    for i in range(len(y)):
        if y_hat[i]==y[i]:
            count = count+1
            
    accuracy = count/len(y) 
    
    return(accuracy)


def precision(y_hat, y, cls):
    """
    Function to calculate the precision
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the precision as float
    """
    assert(y_hat.size == y.size)
    
    #out of the number of times we predict Good, how many times is the condition actually Good
    act_corr_pred = 0
    corr_pred = 0
    temp = 10**(-6)
    
    for i in range(len(y)):
        if y_hat[i] == cls:
            if y_hat[i] == y[i]:
                act_corr_pred = act_corr_pred + 1
            corr_pred = corr_pred + 1
    
    
    if corr_pred>temp:
        corr_pred = corr_pred*1
    else:
        corr_pred = temp
        
    precision = act_corr_pred/corr_pred
    
    return(precision)



def recall(y_hat, y, cls):
    """
    Function to calculate the recall
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the recall as float
    """
    assert(y_hat.size == y.size)
        
    #the fraction of the total amount of relevant instances that were actually retrieved
    act_corr_pred = 0
    corr_pred = 0
    temp = 10**(-6)

    for i in range(len(y)):
        if y[i] == cls:
            if y[i] == y_hat[i]:
                act_corr_pred = act_corr_pred + 1
            corr_pred = corr_pred + 1
    
    if corr_pred>r:
        corr_pred = corr_pred*1
    else:
        corr_pred = temp
        
    recall = act_corr_pred/corr_pred
    
    return(recall)


def rmse(y_hat, y):
    """
    Function to calculate the root-mean-squared-error(rmse)
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the rmse as float
    """
    assert(y_hat.size == y.size)
    
    sum_ = 0
    
    for i in range(len(y)):
        sum_ = (y_hat[i] - y[i])**2 + sum_
        
    rmse = (sum_/len(y))**0.5
    
    return(rmse)

    
def mae(y_hat, y):
    """
    Function to calculate the mean-absolute-error(mae)
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the mae as float
    """
    assert(y_hat.size == y.size)
    
    sum_ = 0
    
    for i in range(len(y)):
        sum_ = abs(y_hat[i] - y[i]) + sum_
        
    mae = (sum_/len(y))
    
    return(mae)
