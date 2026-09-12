def twoSum(self, array, target):
    slovarik = {}
    for i in range(len(array)):
        difference = target - array[i]    
        if difference in slovarik:
            return [slovarik[difference], i]
        slovarik[array[i]] = i