from yamlParser import YamlSectionParser

def getYamlContents( pathToYamlFile ):
    """
    Args:
        param1 (str): Path of input yaml file

    Returns:
        dict: yaml file contents
    """

    with open( pathToYamlFile,"r")as stream:
        try:
            import yaml
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Main............
yamlSectionExtractor = YamlSectionParser()
sampleYamlFileContents = getYamlContents( "config.yaml" )
print( yamlSectionExtractor.getYamlSection( sampleYamlFileContents, [ "section1.s1arr1item1", "section1.s1common", "section2.s2key1", "section2.s2key2.commonKey"] ))
