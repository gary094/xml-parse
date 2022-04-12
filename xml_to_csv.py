import xmltodict


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def read_value(filepath):
    value_dict = xmltodict.parse(read_file(filepath))
    body_length = None
    for item in value_dict["asphereDatabase"]["datasetDatabase"]["datasets"]["dataset"]["partialDataset"]["itemContent"]["items"].items():
        for ditem in item[1]:
            for k, v in ditem.items():
                if k == "floatValue":
                    for i in v.items():
                        if i[0] == "value":
                            body_length = i[1]
                            # print("Body length:", i[1], "mm")
    return body_length


if __name__ == "__main__":
    value_dict = xmltodict.parse(read_file("xml_data.xml"))
    print("Body length:", value_dict["asdf"]["value"], "mm")
