import json
import warnings
import numpy as np
import scipy.stats as stats

# Ignore warning from numpy
warnings.simplefilter('ignore', np.RankWarning)

def lambda_handler(event, context):
    
    # Initialize output list
    output = []
    
    # Default empty dictionary
    emptyResult = {
        "Material Group": None,
        "Pricing Category": None,
        "Valid Prices": None,
        "Logarithmic Regression Base": None,
        "Logarithmic Regression Exponent": None,
        "P Value": None
    }
    
    # Try loading json from request body
    try:
        
        body = json.loads(event['body'])
    
    # Return empty result if not possible
    except:
        
        output.append(emptyResult)
    
    # Else parse json
    else:
        
        i = 0
        
        end = len(body) if len(body) > 1 else 1
        
        while i <= (end - 1):
            
            # Try reading values and calculating return values
            try:
                
                materialGroup = body[i]['Material Group']
                pricingCategory = body[i]['Pricing Category']
                transferPrices = list(map(float, body[i]['Transfer Prices'].split(sep=',')))
                kgrps = list(map(float, body[i]['KGRPs'].split(sep=',')))
                
                logarithmicRegression = np.polyfit(np.log(transferPrices), np.log(kgrps), 1)
                linearRegression = stats.linregress(np.log(transferPrices), np.log(kgrps))
                
                # Create dictionary for return values
                result = {
                    "Material Group": materialGroup,
                    "Pricing Category": pricingCategory,
                    "Valid Prices": len(transferPrices),
                    "Logarithmic Regression Base": logarithmicRegression[1],
                    "Logarithmic Regression Exponent": logarithmicRegression[0],
                    "P Value": linearRegression[3]
                }
                
                # Add dictionary to output list
                output.append(result)
            
            # Return empty result if not possible
            except:
                
                output.append(emptyResult)
                
            finally:
                
                i += 1
        
    return {
        'statusCode': 200,
        "body": json.dumps(output)
    }
