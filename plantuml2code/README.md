# plantuml2code

This project aims to allow developpers to generate code from a Plant UML class diagramm.
Languages curently supported :

- Python
- C

# How to use:

-
    1) 先安装: pip install textX
    2) Define a PlantUML class diagram:

PlantUML is an easy grammar that generates UML drawings : [PlantUML project](http://plantuml.com/class-diagram)

-
    3) Launch plant2code with the specified language and the diagram path as arguments (you can also specify where you
       want the code to be generated)

##### python main.py python uml-v3.txt ../pc_game

```sh
$ plant2code python path/to/plantuml_diagram.txt /tmp/output
```

-
    4) That's it ! Your code as been generated, now you should follow the todo indications (printed as comment inside
       the code) to complete the code.

# Documentation:

```
Usage: plant2code <python|c> PLANT_UML_FILE [OPTION]...         (1st form)
  or:  plant2code <python|c> PLANT_UML_FILE OUTPUT [OPTION]...  (2nd form)

In the 1st form, generate code from the PLANT_UML_FILE in the current directory.
In the 2nd form, generate code from the PLANT_UML_FILE and output it in the OUPUT path.

Mandatory arguments to long options are mandatory for short options too.
  -h, --help            display this help and exit
  -d, --debug           enable debug
      --disable-todo    disable todo indications
```

# Dependences:

* Python3
* TexT 1.6 (current version not supported) : ```pip3 install textx==1.6```
