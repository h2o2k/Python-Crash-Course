def printModels(unprintedDesigns, completedModels):
    while unprintedDesigns:
        currentDesigns = unprintedDesigns.pop()
        print("Printing model: " + currentDesigns)
        completedModels.append(currentDesigns)

def showCompletedModels(completedModels):
    print("\nThe follow models have been printed:")
    for completedModel in completedModels:
        print(completedModel)

unprintedDesigns = ['iphone case', 'robot pendant', 'orange']
completedModels = []

printModels(unprintedDesigns, completedModels)
showCompletedModels(completedModels)
