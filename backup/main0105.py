import flet as ft
import pay
from icecream import ic
def main(page: ft.Page):
    page.title = "Routes Example"
    table = ["","",""]
    waring = ft.Text("") 
    page.session.set("waring", waring)
    page.session.set("table", table)


    def button1_clicked(e):
        """
        當Button1被按下時所觸發
        """
        global tb,people
        name = []
        data = {}
        while tb.value[-1] == "\n": tb.value = tb.value[:-1]
        #判斷姓名總數人數是否相同，否則回到根目錄
        if tb.value == "":
            waring.value = "請輸入人名"
            page.go("/")
        elif len(tb.value.split("\n")) != int(people.value):
            waring.value = "請輸入正確數量"
            
            page.go("/")
        else:
            waring.value = ""
            for item in tb.value.split("\n"):
                name.append(item)
            #呼叫自定義函式 pay ，並得到init的人物dict
            if len(name) != len(set(name)):
                waring.value = "人名請勿重複"
                page.go("/")
            else:
                personlist = pay.Person_init(int(people.value),name)
                for i in range (int(people.value)):
                    data[f"{name[i]}"] = {}
                #將 num(總人數 : int) tb(姓名 : ft物件) data(temp : dict) name(姓名 : list) personlist (init人物 : dict ) 放入 session
                page.session.set("num", people.value)
                page.session.set("tb", tb)
                page.session.set("data", data)
                page.session.set("name", name)
                page.session.set("personlist", personlist)
                page.session.set("data", data)
                
                


                #切到 /pay 目錄
                page.go("/pay")
        page.session.set("waring", waring)

    def check():
        
        global d,number_textbox,option_textbox
        data = page.session.get("data")
        if option_textbox.value == "" and number_textbox.value == "":
            pass
        elif number_textbox.value == "" or  option_textbox.value == "" or d.value == "": #type(int(option_textbox.value)) != type(1) or 
            ic("i'm here!")
            waring.value = "請輸入正確資訊"
        else:
            table = page.session.get("table")
            table = [item for item in table if item != ""]
            table.append(d.value)
            table.append(number_textbox.value)
            table.append(option_textbox.value)
            data[d.value][number_textbox.value] = option_textbox.value
            page.session.set("data", data)
            page.session.set("table", table)

            
       
            
    def button2_clicked(e):
        check()
        
        global number_textbox,option_textbox,texttable
        number_textbox.value = ""
        option_textbox.value = ""
        # texttable.value = "\n".join([f"{table[0]} Buy {table[1]} cost {table[2]}" for i in range(0, len(table), 3)])
        # failed
        page.go("/")
        page.go("/pay")
        page.session.set("waring", waring)


    def button3_clicked(e):
        check()
        data = page.session.get("data")
        personlist = page.session.get("personlist")
        num = page.session.get("num")
        result = pay.result(personlist,pay.PayList(data,int(num)))
        page.session.set("result", result)
        page.go("/result")

    def route_change(route):
        """
        切換目錄
        """
        #將畫面清空
        page.views.clear()
        global tb,people
        waring = page.session.get("waring")
        #定義 people(下拉式選單) 與 tb(文字框) 物件
        people = ft.Dropdown(label="人數", options=[ft.dropdown.Option(str(i)) for i in range(2,10)])
        tb = ft.TextField(
                        label="請輸入人名",
                        hint_text="Name1\nName2",
                        multiline=True,
                        filled=True,
                        min_lines=0,
                        max_lines=10)
        #將 control 依序加入 page.views
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT), #標題
                    people,tb,waring,
                    ft.ElevatedButton(text="Submit",on_click=button1_clicked) #當按鈕按下時觸發                   
                ],
            )
        )

        # /oay 目錄
        if page.route == "/pay":
            global d,number_textbox,option_textbox,texttable

            # keys = page.session.get_keys()
            # for key in keys:
            #     value = page.session.get(key)
            #     ic(key,value)


            #導入 session 內容
            num = page.session.get("num")
            name = page.session.get("name")
            table = page.session.get("table")
            # waring = page.session.get("waring")
            #定義 d 姓名 (下拉式選單)  number_textbox 輸入品項名稱 (文字框) option_textbox 金額 (文字框)
            d = ft.Dropdown(label="人名", options = [ft.dropdown.Option(f"{name[i]}") for i in range(int(num))])
            
            # item_list = ft.DataTable(
            #                         columns=[
            #                             ft.DataColumn(ft.Text("name"),ft.DataColumn(ft.Text("品項")),ft.DataColumn(ft.Text("金額")))
            #                         ],
            #                         rows=[
            #                             ft.DataRow(
            #                                 cells=[
            #                                     ft.DataCell(ft.Text(table[0])),
            #                                     ft.DataCell(ft.Text(table[1])),
            #                                     ft.DataCell(ft.Text(table[2]))
            #                                 ]
            #                             )
            #                               # 步长为3，每三个元素为一行
            #                         ],
            #                     )
            table = ["p","p","p","p","p","p","p","p","p","p","p","p"]
            text_lines = "\n".join([f"{table[i]} Buy {table[i + 1]} cost {table[i + 2]}" for i in range(0, len(table), 3)])
            texttable = ft.TextField(value=text_lines, read_only=True,multiline=True)




            number_textbox = ft.TextField(hint_text="品項", text_align=ft.TextAlign.CENTER, width=100)
            option_textbox = ft.TextField(hint_text="dollars",keyboard_type=ft.KeyboardType.NUMBER)
            bn2 = ft.ElevatedButton(text="繼續", on_click=button2_clicked)
            bn3 = ft.ElevatedButton(text="結束輸入", on_click=button3_clicked)
            w = ft.Text(waring.value)
            page.views.append(
                ft.View(
                    "/pay",
                    [   
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),texttable,
                        w,d,ft.Row([number_textbox,option_textbox]),ft.Row([bn2,bn3]), 
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        elif page.route == "/result":
            result = page.session.get("result")

            page.views.append(
                ft.View(
                    "/result",
                    [   
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text(result), 
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        else:
            page.go("/")
        #更新畫面
        page.update()


    def view_pop(view):
        # 移除堆疊中的最上層視圖
        page.views.pop()
        # 取得更新後的最上層視圖
        top_view = page.views[-1]
        # 導航到最上層視圖的路由
        page.go(top_view.route)

    # 設定路由改變時的回調函數為 route_change 函數
    page.on_route_change = route_change
    # 設定視圖彈出時的回調函數為 view_pop 函數
    page.on_view_pop = view_pop
    # 導航到當前的路由
    page.go(page.route)
    
#Let's go...
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
