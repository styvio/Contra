dataSet = [1,3,5,7,4,9,14,27,23,40]

def setFactors(dataSet):
    print("Styvio Console: setting initial step factors...")
    initialFactors = []
    for i in range(0, len(dataSet)):
        if(i < (len(dataSet)-1)):
            initialFactors.append((((dataSet[i+1])-(dataSet[i]))/(dataSet[i]))*100)
    return(initialFactors)

def formatData(dataSet, initialFactors):
    print("Styvio Console: formatting data...")
    differences = []
    for i in range(0, (len(dataSet)-1)):
        differences.append(initialFactors[i]-dataSet[i])
    differences.append(-999)
    orderedDifferences, orderedDataSet = zip(*sorted(zip(differences, dataSet)))
    return(orderedDifferences, orderedDataSet)
    
def makePredictions(dataSet, orderedDifferences, orderedDataSet):
    predictedValue = 0
    for i in range(1, len(orderedDifferences)):
        predictedValue = dataSet[len(dataSet)-1]*(orderedDifferences[i] * ((i-1)/(len(orderedDifferences * 100))))
    return(predictedValue)

def runPredictions(dataSet):
    print("Styvio Console: starting prediction algorithm...")
    initialFactors = setFactors(dataSet)
    orderedDifferences, orderedDataSet = formatData(dataSet, initialFactors)
    prediction = makePredictions(dataSet, orderedDifferences, orderedDataSet)
    return(prediction)

if __name__ == "__main__":
   output = runPredictions(dataSet)
   print("Styvio Console: Algorithm has finished running. predictions are ready...")
   print()
   print(f"Original Dataset: {dataSet}")
   print()
   print(f"Next Value Prediction: {output}")
   print()
