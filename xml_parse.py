import xmltodict

def read_file(path):
  with open(path, 'r') as file:
    return file.read()

if __name__ == "__main__":
  value_dict = xmltodict.parse(read_file("/home/gary/data.xml"))
  for item in value_dict["asphereDatabase"]["datasetDatabase"]["datasets"]["dataset"]["partialDataset"]["itemContent"]["items"].items():
      for ditem in item[1]:
          for k, v in ditem.items():
              if k == "floatValue":
                  for i in v.items():
                      if i[0] == "value":
                          print("Body length:", i[1], "mm")

