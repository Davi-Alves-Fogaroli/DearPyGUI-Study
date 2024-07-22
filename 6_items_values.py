#  more about values: https://dearpygui.readthedocs.io/en/latest/documentation/item-value.html
import dearpygui.dearpygui as dpg

dpg.create_context()

def print_value(sender, app_data, user_data):
    # quando usamos o commando 'dpg.get_value(sender)', nos forçamos a insesão do valor de input dentro do argumento 
    # sender, que deveria armazenar o id padrão do item
    print("sender value: ", dpg.get_value(sender))
    
    # bem o comando 'dpg.get_value(app_data)' não aceita valores float. e retorna erro 1008(Exception: Error: [1008]
    # Message:       Python value error. Must be int.)
        # print("app_data value: ", dpg.get_value(app_data))
    print("user_data value: ", dpg.get_value(user_data), "\n")

    # Agora, se nos referenciamos puxamos o app_data e o referenciamos diretamente, sem usar o dpg.get_value como 
    # intermediario, nao temos erro ao armazernar valores com ponto flutuante
        # print(f"app_data is: {app_data}")
    # print(f"sender is: {sender}")
    # print(f"user_data is: {user_data}")


with dpg.window(label="Items Values", width=300):
    input_txt_1 = dpg.add_input_text()
    # the valu for the input_txt_2  will have a strating value of "This is a default value!" 
    input_text_2 = dpg.add_input_text(
        label = "Imput text 2",
        default_value = "This is a default value!",
        callback = print_value,
    )
    slider_float_1 = dpg.add_slider_float()
    sleder_float_2 = dpg.add_slider_float(
        label = "Slider Float 2",
        default_value = 50.0,
        callback = print_value,
    )
    dpg.add_slider_int(default_value=15, tag="slider_int")
   #dpg.set_item_callback(item, callback) 
    dpg.set_item_callback(input_txt_1, print_value)
    dpg.set_item_callback(slider_float_1, print_value)


dpg.set_value("slider_int", 40)


dpg.create_viewport(title="Items Values", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()