import dearpygui.dearpygui as dpg

# Dictionary to store values
trocador_dic = {
    "Fluidos": {
        "Vazão": {
            "Gases": None,
            "Ar": None,
        },
        "Temperatura Entrada": {
            "Gases": None,
            "Ar": None,
        },
    },
    "Name": [],
    "Pre_ar": []
}

class Pre_ar:
    def __init__(self, burntime, thrust, totalMass, propellantMass):
        self.burntime = burntime
        self.thrust = thrust
        self.totalMass = totalMass
        self.propellantMass = propellantMass

# Function to define Pre_ar
def define_pre_ar(name, burntime, thrust, totalMass, propellantMass):
    print("Defining Pre_ar...")
    from g_t1 import PRE_AR_LIST_G
    # Print user_data values
    print("1")    
    user_data = [name, burntime, thrust, totalMass, propellantMass]
    print("2")
    for count, item in enumerate(user_data):
        print(f"User_data index: {count}, value: ", dpg.get_value(item))

    # Append values to the dictionary
    trocador_dic["Name"].append(dpg.get_value(name))
    trocador_dic["Pre_ar"].append(Pre_ar(
        dpg.get_value(burntime),
        dpg.get_value(thrust),
        dpg.get_value(totalMass),
        dpg.get_value(propellantMass)
    ))

    # Print the stored values
    print(f"\nTrocador, Pre_ar: {trocador_dic['Pre_ar']}\n")

    # Update the listbox with new names
    dpg.configure_item(PRE_AR_LIST_G, items=trocador_dic["Name"])

    # Print updated list
    print(f"Updated List: {trocador_dic['Name']}")
