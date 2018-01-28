class YamlSectionParser:

    #Recursive Function
    def traverseDict(self, dictContents, fullNestedKey, fullNestedKeyIndex):
        """
        Args:
            param1(dict) dictContents: dict containing current section being matched
            param2(str) fullNestedKey: Contains full key name of the required dict section
                                       It is constant throughout the complete recursive calls
                                       Eg: "key1.key2.key3"
            param3(int) fullNestedKeyIndex: As fullNestedKey is '.' delimited, this param points to
                                       the current key being searched, from fullNestedKey( split on '.' )

        Returns:
            dict: Values matching nested keys
                  Eg: { "key1.key2.key3": [<values>] }
        """

        if isinstance(dictContents, dict):

            if(fullNestedKey.split(".")[fullNestedKeyIndex] in dictContents):
                matchedValue = dictContents.__getitem__(fullNestedKey.split(".")[fullNestedKeyIndex])

                # If the last key is matched, return the matchedValue
                if(len(fullNestedKey.split("."))-1 == fullNestedKeyIndex):
                    return matchedValue
                else:
                    return self.traverseDict(matchedValue, fullNestedKey, fullNestedKeyIndex + 1)
            else:
                return None

        elif isinstance(dictContents, list):
            result = []
            for item in dictContents:
                matchedValuePerItem = self.traverseDict(item, fullNestedKey, fullNestedKeyIndex)
                if matchedValuePerItem:
                    if isinstance(matchedValuePerItem, list):
                        # If matchedValuePerItem is list, join it with result list
                        result = result+matchedValuePerItem
                    else:
                        # If matchedValuePerItem is anything other than list (dict/str), append it to result list
                        result.append(matchedValuePerItem)
            return result


    def getYamlSection(self, dictContents, nestedKeys):
        """
        Args:
            param1(dict) dictContents: dict containing all sections
            param2(list<str>) nestedKeys: Contains full key names of the required dict sections
                                          Eg: [ "key1.key2.key3", "key4.key5" ]

        Returns:
            dict: Values matching for each nestedKey
                  Eg: { "key1.key2.key3": [<values>], "key4.key5": [<values>] }
        """
        result = {}
        for key in nestedKeys:
            values = self.traverseDict(dictContents, key, 0)
            result[key] = values
        return result

