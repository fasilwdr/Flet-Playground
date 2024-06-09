import flet as ft



def UserError(page, text):
    snackbar = ft.SnackBar(content=ft.Text(text, color=ft.colors.WHITE, text_align="center"), open=True, bgcolor=ft.colors.RED)
    page.show_snack_bar(snackbar)


class ResultView(ft.View):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.route = '/result'
        self.padding = 0
        data = self.page.data
        self.appbar = ft.AppBar(title=ft.Text("Flet Playground Result"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True)
        self.controls = [
            ft.Pagelet(
                appbar=data.get('appbar'),
                content=data.get('content'),
                bgcolor=data.get('bgcolor'),
                navigation_bar=data.get('navigation_bar'),
                bottom_app_bar=data.get('bottom_app_bar'),
                drawer=data.get('drawer'),
                end_drawer=data.get('end_drawer'),
                floating_action_button=data.get('floating_action_button'),
                floating_action_button_location=data.get('floating_action_button_location'),
                width=data.get('width'),
                height=data.get('height'),
                bottom_sheet=data.get('bottom_sheet'),
            )
        ]


class RootView(ft.View):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.route = '/'
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.scroll = ft.ScrollMode.AUTO
        self.flet_controls = ft.Ref[ft.ListView]()
        self.pagelet_data = {
            'width': ft.Ref[ft.TextField](),
            'height': ft.Ref[ft.TextField](),
            'appbar': ft.Ref[ft.TextField](),
            'bgcolor': ft.Ref[ft.TextField](),
            'drawer': ft.Ref[ft.TextField](),
            'end_drawer': ft.Ref[ft.TextField](),
            'bottom_appbar': ft.Ref[ft.TextField](),
            'floating_action_button': ft.Ref[ft.TextField](),
            'floating_action_button_location': ft.Ref[ft.TextField](),
            'navigation_bar': ft.Ref[ft.TextField](),
            'bottom_sheet': ft.Ref[ft.TextField](),
        }
        self.controls = [
            ft.AppBar(title=ft.Text("Flet Play Ground"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
            ft.ExpansionPanelList(
                expand_icon_color=ft.colors.GREY,
                elevation=5,
                divider_color=ft.colors.GREY_900,
                controls=[
                    ft.ExpansionPanel(
                        header=ft.Container(
                            padding=10,
                            content=ft.Text("Page Properties", size=15, weight=ft.FontWeight.BOLD)
                        ),
                        bgcolor=ft.colors.BLUE_400,
                        content=ft.ListView(
                            controls=[
                                ft.ListTile(
                                    title=ft.TextField(label="width", ref=self.pagelet_data['width'], multiline=True,
                                                       value="page.width",
                                                       keyboard_type=ft.KeyboardType.NUMBER,
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="height", ref=self.pagelet_data['height'], multiline=True,
                                                       value="page.height - 80",
                                                       keyboard_type=ft.KeyboardType.NUMBER,
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="appbar", ref=self.pagelet_data['appbar'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="bgcolor", ref=self.pagelet_data['bgcolor'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="bottom_appbar", ref=self.pagelet_data['bottom_appbar'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="floating_action_button", ref=self.pagelet_data['floating_action_button'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="floating_action_button_location", ref=self.pagelet_data['floating_action_button_location'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="navigation_bar", ref=self.pagelet_data['navigation_bar'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="bottom_sheet", ref=self.pagelet_data['bottom_sheet'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="drawer", ref=self.pagelet_data['drawer'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                ),
                                ft.ListTile(
                                    title=ft.TextField(label="end_drawer", ref=self.pagelet_data['end_drawer'], multiline=True,
                                                       value="None",
                                                       expand=True,
                                                       bgcolor=ft.colors.SURFACE_VARIANT, border=ft.InputBorder.NONE)
                                )
                            ]
                        )
                    ),
                    ft.ExpansionPanel(
                        header=ft.Container(
                            padding=10,
                            content=ft.Text("Page Controls", size=15, weight=ft.FontWeight.BOLD)
                        ),
                        expanded=True,
                        bgcolor=ft.colors.BLUE_400,
                        content=ft.ListView(
                            ref=self.flet_controls,
                            controls=[
                                ft.ListTile(
                                    title=ft.TextField("", bgcolor=ft.colors.SURFACE_VARIANT,
                                                       border=ft.InputBorder.NONE,
                                                       hint_text="#Already assigned flet as ft",
                                                       hint_style=ft.TextStyle(color=ft.colors.GREY, size=10),
                                                       multiline=True),
                                    trailing=ft.IconButton(ft.icons.DELETE, on_click=self.delete_control),
                                )
                            ]
                        )
                    )

                ]
            ),
            ft.Row(
                controls=[
                    ft.IconButton(ft.icons.ADD, on_click=self.add_control),
                    ft.IconButton(ft.icons.CLEAR_ALL, on_click=self.clear_controls),
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ]
        self.bottom_appbar = ft.BottomAppBar(
            height=60,
            content=ft.Row(controls=[
                ft.Text("Flet version: 0.22.1", size=10, color=ft.colors.GREY, text_align="center"),
                ft.FilledButton("Run", on_click=self.run_file),
            ], spacing=0, alignment=ft.MainAxisAlignment.SPACE_AROUND)
        )

    def run_file(self, e):
        try:
            page = self.page
            data = {
                'width': eval(self.pagelet_data['width'].current.value),
                'height': eval(self.pagelet_data['height'].current.value),
                'appbar': eval(self.pagelet_data['appbar'].current.value),
                'bgcolor': eval(self.pagelet_data['bgcolor'].current.value),
                'bottom_appbar': eval(self.pagelet_data['bottom_appbar'].current.value),
                'floating_action_button': eval(self.pagelet_data['floating_action_button'].current.value),
                'floating_action_button_location': eval(self.pagelet_data['floating_action_button_location'].current.value),
                'navigation_bar': eval(self.pagelet_data['navigation_bar'].current.value),
                'bottom_sheet': eval(self.pagelet_data['bottom_sheet'].current.value),
                'drawer': eval(self.pagelet_data['drawer'].current.value),
                'end_drawer': eval(self.pagelet_data['end_drawer'].current.value),
            }
            controls = ft.Column(controls=[])
            for list_tile in self.flet_controls.current.controls:
                if list_tile.title.value != '':
                    controls.controls.append(eval(list_tile.title.value))
            data['content'] = controls
            self.page.data = data
            self.page.update()
            self.page.go('/result')
        except Exception as e:
            return UserError(self.page, e)

    def add_control(self, e):
        self.flet_controls.current.controls.append(ft.ListTile(
                                    title=ft.TextField("", bgcolor=ft.colors.SURFACE_VARIANT,
                                                       border=ft.InputBorder.NONE,
                                                       hint_text="#Already assigned flet as ft",
                                                       hint_style=ft.TextStyle(color=ft.colors.GREY, size=10),
                                                       multiline=True),
                                    trailing=ft.IconButton(ft.icons.DELETE, on_click=self.delete_control),
                                ))
        self.flet_controls.current.update()

    def clear_controls(self, e):
        list_view = self.flet_controls.current
        list_view.controls.clear()
        list_view.controls.append(ft.ListTile(
                                    title=ft.TextField("", bgcolor=ft.colors.SURFACE_VARIANT,
                                                       border=ft.InputBorder.NONE,
                                                       hint_text="#Already assigned flet as ft",
                                                       hint_style=ft.TextStyle(color=ft.colors.GREY, size=10),
                                                       multiline=True),
                                    trailing=ft.IconButton(ft.icons.DELETE, on_click=self.delete_control),
                                ))
        list_view.update()

    def delete_control(self, e):
        list_view = self.flet_controls.current
        if len(list_view.controls) > 1:
            list_view.controls.remove(e.control.parent)
        else:
            list_view.controls[0].title.value = ""
        list_view.update()


def main(page: ft.Page):
    page.title = "Flet Playground"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e):
        page.views.clear()
        page.views.append(
            RootView(page)
        )
        if page.route == '/result':
            page.views.append(ResultView(page))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main)
