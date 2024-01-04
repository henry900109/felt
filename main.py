import flet as ft
import pay
from time import sleep





def main(page: ft.Page):
    page.title = "Flet Count App"
    page.vertical_alignment = ft.MainAxisAlignment.NONE
    # page.debug = True
    page.padding = 20

    data = {}
    
    def button1_clicked(e):
        name = []
        t = ft.Text() 
        if tb.value == "":
            t.value = "請輸入人名"
        elif len(tb.value.split("\n")) != int(people.value):
            t.value = "清輸入正確數量"
        else:
            for item in tb.value.split("\n"):
                name.append(item)
            personlist = pay.Person_init(int(people.value),name)
            t.value =str(personlist)
            for i in range (int(people.value)):
                data[f"{name[i]}"] = {}
            page.remove(people)
            page.remove(tb)
            page.remove(bn1)
            # page.remove(t)
            # columns=[ft.DataColumn(ft.Text("name"))],
            # for i in range(int(people.value)):
                # table = ft.DataTable(rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(name[i]))])])
                # page.add(table)
            # radio_buttons = [ft.Radio(value=f"{name[i]}", label=f"{name[i]}") for i in range(int(people.value))]
            # radio_group = ft.RadioGroup(content=ft.Column(radio_buttons))
            # page.add(radio_group)
            # t = ft.Text()
            # t.value = "花了"
            # d = ft.Text()
            # d.value = "元"
            # page.add(ft.Row([t,number_textbox,d])) 

            def button2_clicked(e):
                data[d.value][number_textbox.value] = option_textbox.value
                print(data)
                option_textbox.value = ""
                number_textbox.value = ""
                page.update()

            # def find_option(option_name):
            #     for option in d.options:
            #         if option_name == option.key:
            #             return option
            #     return None

            # def add_clicked(e):
            #         d.options.append(ft.dropdown.Option(option_textbox.value))
            #         d.value = option_textbox.value
            #         option_textbox.value = ""
            #         page.update()

            # def delete_clicked(e):
            #     option = find_option(d.value)
            #     if option != None:
            #         d.options.remove(option)
            #         # d.value = None
            #         page.update()





            def button3_clicked(e):
                pm = pay.PayList(data,int(people.value))
                result = pay.result(personlist,pm)
                page.remove(option_textbox)
                page.remove(d)
                page.remove(number_textbox)
                t = ft.Text()
                t.value = result
                page.add(t)
                page.remove(row)


                page.update()

            d = [ft.dropdown.Option(f"{name[i]}") for i in range(int(people.value))]
            d = ft.Dropdown(label="人名", options = d)
            number_textbox = ft.TextField(hint_text="品項", text_align=ft.TextAlign.CENTER, width=100)

            option_textbox = ft.TextField(hint_text="Enter item name")
            bn2 = ft.ElevatedButton(text="繼續", on_click=button2_clicked)
            bn3 = ft.ElevatedButton(text="結束輸入", on_click=button3_clicked)
            page.add(d,number_textbox,option_textbox)
            row = ft.Row([bn2,bn3])
            page.add(row) 
        page.update()



 

    people = ft.Dropdown(label="人數", options=[
        ft.dropdown.Option("1"),
        ft.dropdown.Option("2"),
        ft.dropdown.Option("3"),
        ft.dropdown.Option("4"),
    ])

    tb = ft.TextField(
            label="請輸入人名",
            hint_text="Name1\nName2",
            multiline=True,
            filled=True,
            min_lines=0,
            max_lines=10,
        )



    bn1 = ft.ElevatedButton(text="Submit", on_click=button1_clicked)
    t = ft.Text()

    # page.add(ft.Row([
    #     people,
    # ]))
    # , alignment=ft.MainAxisAlignment.CENTER)
    page.add(people,tb,bn1,t)


ft.app(target=main, view=ft.WEB_BROWSER,port=5001)