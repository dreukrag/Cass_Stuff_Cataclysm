import os
import json

# x = [i[2] for i in os.walk('.')]
# y=[]
# for t in x:
#     for f in t:
#         if f.endswith(".json"):
#             y.append(f)
# x =
# [os.path.join(r,file) for r,d,f in os.walk(".") for file in f]
x = []
for r, d, f in os.walk("."):
    for file in f:
        if file.endswith(".json"):
            x.append(os.path.join(r, file))

# print(x)

for file in x:
    with open(file, "r+") as fr:
        # print(file)
        data = json.load(fr)
        for recipe in data:
            if "time" in recipe:
                # print(recipe["time"])
                recipe["time"] = "1 s"
            elif "blueprint_needs" in recipe:
                if "time" in recipe["blueprint_needs"]:
                    # print(recipe["blueprint_needs"]["time"])
                    # recipe["blueprint_needs"]["time"] = "1 s"
                    if "inline" in recipe["blueprint_needs"]:
                        print("has inline")
                        if "components" in recipe["blueprint_needs"]["inline"]:
                            print("has components")
                            for cmpList in recipe["blueprint_needs"]["inline"]["components"]:
                                for itm in cmpList:
                                    print(itm)
                                    newval = itm[1]/4
                                    if newval >= 1:
                                        itm[1] = int(newval)
                                    else:
                                        itm[1] = 1

        fr.seek(0)
        # print(data)
        json.dump(data, fr, indent=4)
        fr.truncate()
    # break
