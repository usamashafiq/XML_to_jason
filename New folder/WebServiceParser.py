import xmltodict
import json


# read the file from user
def reader():
    path = input("Enter the xml file path :: ")
    try:
        with open(path) as pa:
            File_Data = pa.read()
            return File_Data
    except:
        print("PLEASE ENTER CORRECT FILE PATH")
        return


# check the xml file have methods or not
def Ext_Abs_Meth(file):
    Document_save = xmltodict.specse(file)
    try:
        essential_details = Document_save["service"]["abstract_method"]
        return essential_details
    except:
        print("ABSTRACT METHOD NOT FOUND IN XML FILE PLEASE ENTER C0RECT FILE")
        return


# specse the xml file 
def Token_Xml(essential_details):
    Collect_data = []

    if type(essential_details) == dict:
        Coll_Da = C_F_G_d(essential_details)
        Collect_data.append(Coll_Da)
    if type(essential_details) == list:
        for info in essential_details:
            Coll_Da = C_F_G_d(info)
            Collect_data.append(Coll_Da)
    OBJ_MAKER_JSON = {"abstract_method": Collect_data}
    FINAL_DICT = json.dumps(OBJ_MAKER_JSON, indent=2)
    print(FINAL_DICT)


# check file which data we get in xml file to make json file
def C_F_G_d(info):
    constant = []
    List_Ex = []
    Coll_Da = {}

    if "@name" in info:
        Coll_Da["method_name"] = info['@name']
    if "visibility" in info:
        Coll_Da["visibility"] = info["visibility"]

    if "arguments" in info:
        for spec in info["arguments"]:
            if type(info["arguments"][spec]) == list:
                for evaluate in info["arguments"][spec]:
                    tmp = {"datatype": evaluate["@type"], "label": evaluate["#text"]}
                    constant.append(tmp)
            if type(info["arguments"][spec]) == dict:
                evaluate = info["arguments"][spec]
                tmp = {"datatype": evaluate["@type"], "label": evaluate["#text"]}
                constant.append(tmp)
        Coll_Da["arguments"] = {"parameter": constant}

    if "exceptions" in info:
        if type(info["exceptions"]["exception"]) == str:
            List_Ex.append(info["exceptions"]["exception"])
        if type(info["exceptions"]["exception"]) == list:
            for exception in info["exceptions"]["exception"]:
                List_Ex.append(exception)
        Coll_Da["exceptions"] = {"exception": List_Ex}
    if "return" in info:
        Coll_Da["return"] = info["return"]
    return Coll_Da


if __name__ == '__main__':
    Data_file = reader()
    Method = Ext_Abs_Meth(Data_file)
    Token_Xml(Method)
