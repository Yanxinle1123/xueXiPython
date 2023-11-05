from parsers.model2code.smart2py.smart2py import smart2py
from parsers.model2model.plant2smart import MM_PLANT
from parsers.model2model.plant2smart import plant2smart
from tools import todo


def plant2py(plant_uml_model, output, debug_enabled, todo_enabled):
    todo.enable = todo_enabled
    # 进行预处理，将skin 和 "等特殊字符处理
    output_file_temp = f"{plant_uml_model}.tmp"
    with open(plant_uml_model, "r") as fi, open(output_file_temp, "w") as fo:
        # 一行一行处理
        for one_line in fi:
            last_one_line = one_line.replace('"', "")
            last_one_line = last_one_line.replace('skin', "")
            last_one_line = last_one_line.replace('rose', "")
            fo.write(last_one_line)

    plant_model = MM_PLANT.model_from_file(output_file_temp, debug=debug_enabled)
    smart_model = plant2smart(plant_model)
    smart2py(smart_model, output_path=output)
