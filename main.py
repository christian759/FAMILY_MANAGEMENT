from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.list.list import MDList
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
from time import sleep
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
import json
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.switch import Switch
# from popup import popup_screen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dropdownitem import MDDropDownItem


# Login Page
class Login(MDScreen):

    """
        This class creates the login screen for the application.

        Parameters:
            **kwargs: Optional keyword arguments.

        Attributes:
            anchor_layout (MDAnchorLayout): A widget that holds the other widgets on the screen.
            main_card (MDCard): A widget that holds the input fields and buttons.
            username (MDTextField): A text field for the username.
            email (MDTextField): A text field for the email.
            password (MDTextField): A text field for the password.
            phone_number (MDTextField): A text field for the phone number.
            message_login (MDLabel): A label that displays a message after the user logs in.
            message_signup (MDLabel): A label that displays a message after the user signs up.
            small_grid (MDGridLayout): A grid layout that holds the login and sign up buttons.
            login_button (MDRectangleFlatButton): A button for logging in.
            sign_up_button (MDRectangleFlatButton): A button for signing up.
            welcome (MDLabel): A label that welcomes the user.

        """

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.anchor_layout = MDAnchorLayout()
        self.main_card = MDCard(size_hint=(None, None), size=('500dp', '500dp'), padding='10dp', spacing='10dp',
                                orientation='vertical', ripple_color='white')
        self.anchor_layout.add_widget(self.main_card)
        self.username = MDTextField(icon_left="account",
                                    hint_text='Username',
                                    font_size='18sp',
                                    size_hint_y=None,
                                    height='60dp')
        self.main_card.add_widget(self.username)
        self.email = MDTextField(icon_left="email",
                                 hint_text='Email',
                                 font_size='18sp',
                                 size_hint_y=None,
                                 height='60dp')
        self.main_card.add_widget(self.email)
        self.password = MDTextField(icon_left="lock",
                                    hint_text='Password',
                                    password=True,
                                    font_size='18sp',
                                    size_hint_y=None,
                                    height='60dp')
        self.main_card.add_widget(self.password)
        self.phone_number = MDTextField(icon_left='phone',
                                        hint_text="Phone Number",
                                        font_size='18sp',
                                        size_hint_y=None,
                                        height='60dp')
        self.main_card.add_widget(self.phone_number)
        self.message_login = MDLabel(text="Login successful")
        self.message_signup = MDLabel(text="Signup successful")
        small_grid = MDGridLayout(cols=2, spacing=20, padding=20, size_hint=(1, 1))
        login_button = MDRectangleFlatButton(text='Login', height='60dp', on_press=self.on_login_button_press)
        sign_up_button = MDRectangleFlatButton(text='Sign Up', height='60dp', on_press=self.on_signup_button_press)
        small_grid.add_widget(login_button)
        small_grid.add_widget(sign_up_button)
        self.welcome = MDLabel(text="Welcome Back", font_size='20sp')
        self.main_card.add_widget(small_grid)
        self.add_widget(self.anchor_layout)

        # The information dialog
        self.dialog = MDDialog(size_hint=(0.9, 0.9),
                               title="Tell us more about yourself",
                               buttons=[MDFlatButton(text="skip", on_release=self.dialogue),
                                        MDFlatButton(text="Proceed", on_release=self.enter_other_information)]
                               )
       

# dismiss function for the dialog
    def dialogue(self, instance):
        self.dialog.dismiss()
        next_page = Front()
        MyApp.change(self, next_page)

    # function for saving the user information in a json file
    def save_contact(self, username, phone_number, email, password):
        contact_data = {
            "username": username,
            "phone_number": phone_number,
            "email": email,
            "password": password
        }

        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is not valid JSON, start with an empty list
            contacts = []

        contacts.append(contact_data)

        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=2)

# function for the signup button the login page
    def on_signup_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")
        self.main_card.add_widget(self.message_signup)
        self.save_contact(username, phone_number, email, password)
        self.clear_content()
        self.show_dialog()

# function for the login button in the login page
    def on_login_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")
        self.main_card.add_widget(self.message_login)
        self.save_contact(username, phone_number, email, password)
        self.save_contact(username, phone_number, email, password)
        next_page = Front()
        print("pass")
        sleep(3)
        MyApp.change(self, next_page)

# function to clear the content of the screen
    def clear_content(self):
        # Remove all children (content) from the screen
        self.anchor_layout.clear_widgets()

# function that shows the dialog on click
    def show_dialog(self):
        self.dialog.open()

# To remove the dialog and show front page
    def enter_other_information(self, instance):
        self.dialog.dismiss()
        next_page = Extra()
        print("pass")
        MyApp.change(self, next_page)




# class for the extra page for more information
class Extra(MDScreen):
    def __init__(self, **kwargs):
        super(Extra, self).__init__(**kwargs)
        self.card = MDCard(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           size_hint=(0.9, 0.8),
                           elevation=7,
                           orientation='vertical')
        self.scrollbabe = MDScrollView()
        self.content = MDGridLayout(cols=1, spacing="20dp", padding=10)
        self.title = MDLabel(text="More Information", font_style="H5")
        self.content.add_widget(self.title)
        self.big_name = MDLabel(text="Enter full name")
        self.content.add_widget(self.big_name)
        self.name_field = MDTextFieldRect(font_size='18sp',
                                          size_hint_y=None,
                                          width=80,
                                          height=50,
                                          hint_text="e.g John Doe",
                                          _primary_color=(0, 0, 0, 1),
                                          background_color=(0, 0, 0, 0.05)
                                          )
        self.content.add_widget(self.name_field)
        self.status_text = MDLabel(text="Relationship Status")
        self.content.add_widget(self.status_text)
        self.status_entry = MDTextFieldRect(font_size='18sp',
                                            size_hint_y=None,
                                            width=80,
                                            height=50,
                                            hint_text="e.g Single",
                                            _primary_color="cyan",
                                            background_color=(0, 0, 0, 0.05)
                                            )
        self.content.add_widget(self.status_entry)
        self.general_email_text = MDLabel(text="Occupation")
        self.email_entry = MDTextFieldRect(font_size='18sp',
                                           size_hint_y=None,
                                           width=80,
                                           height=50,
                                           _primary_color="cyan",
                                           background_color=(0, 0, 0, 0.1)
                                           )
        self.content.add_widget(self.general_email_text)
        self.content.add_widget(self.email_entry)
        self.location = MDLabel(text="Country")
        self.country = MDTextFieldRect(font_size='18sp',
                                       size_hint_y=None,
                                       width=80,
                                       height=50,
                                       _primary_color="cyan",
                                       background_color=(0, 0, 0, 0.1)
                                       )
        self.content.add_widget(self.location)
        self.content.add_widget(self.country)
        self.scrollbabe.add_widget(self.content)
        self.card.add_widget(self.scrollbabe)
        self.add_widget(self.card)
        self.done = MDRectangleFlatButton(text="Done",
                                          on_release=self.done_button_press,
                                          md_bg_color=(1, 1, 1, 0.7),
                                          pos_hint={'center_x': 0.9, 'center_y': 0.05},
                                          size_hint=(0.005, 0.0005))
        self.add_widget(self.done)

    def done_button_press(self, instance):
        next_page = Front()
        MyApp.change(self, next_page)


class Front(MDScreen):
    """
            Initializes the Front screen.

            Parameters:
                **kwargs: Optional keyword arguments.
    """

    def __init__(self, **kwargs):
        super(Front, self).__init__(**kwargs)
        self.handler = MDGridLayout(cols=3, rows=1, spacing=15, padding=10)
        self.tab_card = MDCard(orientation="vertical",
                               size_hint=(0.07, 1),
                               padding=(10, 10, 10, 10),
                               ripple_behavior=False,
                               elevation=7
                               )
    # widget under the tab_card
        self.tab_layout = MDGridLayout(cols=1, padding=0, spacing=10)

        self.home_button = MDIconButton(icon="home", size_hint=(0.001, 0.002),
                                        pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                        on_release=self.home_activate)

        self.workspace_button = MDIconButton(icon="briefcase", size_hint=(0.002, 0.002),
                                             pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                             on_release=self.workspace_activate)

        self.cover_space_i = MDLabel(text="", size_hint=(0.76, 0.01))

        self.email_button = MDIconButton(icon="email", size_hint=(0.001, 0.002),
                                         pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                         on_release=self.meeting_activate)

        self.connect_button = MDIconButton(icon="earth", size_hint=(0.001, 0.002),
                                           pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                           on_release=self.connect_activate)

        self.register_button = MDIconButton(icon="account-circle", size_hint=(0.001, 0.002),
                                            pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                            on_release=self.profile_activate)

        self.main_card = MDCard(orientation="vertical",
                                size_hint=(0.88, 1),
                                padding=(10, 10, 10, 10),
                               # ripple_behavior="False",
                                elevation=7,
                                line_color=(0, 0, 0.8, 1),
                                line_width=1,
                                shadow_color=(0.2, 0.2, 0.2, 0.8),
                                shadow_softness=1,
                                md_bg_color=(0.1, 0.1, 0.1, 0.9)
                                )

    # widgets under the main card
        # widget subject to home page
        self.home_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.label_home = MDLabel(text="This is the home page")
        self.home_layout.add_widget(self.label_home)

        # widget subject to the work page
        self.work_layout = MDScrollView()
        self.work_grid = MDGridLayout(cols=2, spacing=20)
        self.todo_card = MDCard(orientation="vertical",
                                padding = 10,
                                ripple_behavior= True,
                                md_bg_color = (0.15, 0.15, 0.16, 0.92)
                                )
        self.todo_label = MDLabel(text="Todo list")
        self.todo_card.add_widget(self.todo_label)
        self.work_grid.add_widget(self.todo_card)
        self.work_layout.add_widget(self.work_grid)

        # widget subject to the email page
        self.email_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.email_entry = MDTextField(mode= "rectangle",
                                        icon_left= "email",
                                        size_hint_y= .11,
                                        hint_text= "Enter email address",
                                        hint_text_color= (0.3, 0.3, 0.4, 0.7),
                                        multiline= True)
        self.email_message = MDTextField(mode="rectangle",
                                         size_hint_y= .9,
                                         hint_text_color= (0.3, 0.5, 0.1, 0.7),
                                         hint_text= "Type your mail",
                                         multiline= True)
        self.send_email = MDFlatButton(line_color =(0.7, 0.2, 0.1, 0.7),
                                       text= "send",
                                       icon= "chevron-double-rigth",
                                       size_hint_y=.1,
                                       md_bg_color=(0.2, 0.1, 0.5, .9),
                                       ripple_color=(0.9, 0, 0.1, 1),
                                       size_hint_x = 1
                                    #   on_release: root.send(self)
                                    )
        self.email_layout.add_widget(self.email_entry)
        self.email_layout.add_widget(self.email_message)
        self.email_layout.add_widget(self.send_email)

        # widgets subject to the connection page
        self.connect_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.connect_label = MDLabel(text="This is the connection layout")
        self.connect_layout.add_widget(self.connect_label)

        # widgets subject to the profile page
        self.profile_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.profile_label = MDLabel(text="This is your profile Page")
        self.profile_layout.add_widget(self.profile_label)

        self.tool_card = MDCard(orientation="vertical",
                                size_hint=(0.05, 1),
                                padding=(10, 10, 10, 10),
                                ripple_behavior=False,
                                elevation=7
                                )

        self.tool_layout = MDGridLayout(cols=1, padding=0, spacing=50)

        self.cover_space_ii = MDLabel(text="", size_hint=(0.72, 0.01))

        self.calender = MDIconButton(icon='calendar', size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                     on_release=self.activate_calendar)

        self.time = MDIconButton(icon='timer', size_hint=(0.001, 0.0013),
                                 pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                 on_release=self.activate_timer)

        self.calculator = MDIconButton(icon='calculator', size_hint=(0.001, 0.0013),
                                       pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                       on_release=self.activate_calculator)

        self.location = MDIconButton(icon='map-marker', size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x': 0.4})
                                     # on_release=self.activate_location)

        self.settings = MDIconButton(icon="cog", size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x':0.4},
                                     on_release = self.activate_settings)

        self.date_dialog = MDDatePicker()

        self.time_dialog = MDTimePicker()

        self.inform_save = MDDialog(size_hint=(0.9, 0.9),
                                    title=f"Alarm has been scheduled",
                                    buttons=[MDFlatButton(text="ok", on_release=self.assurance)]
                                    )
        """
        THE RIGHT SIDE BAR
        """
        # The Calculator
        self.calculator = MDGridLayout(cols = 1, rows= 2, spacing = 10)
        entry_field = MDTextFieldRect(font_size = '16sp',
                                      height = 40,
                                      padding = 20
                                      )
        self.buttons = MDGridLayout(rows = 4, spacing = 7, cols = 4)
        self.button_1 = MDIconButton(icon = "1")
        self.button_2 = MDIconButton(icon = "2")
        self.button_3 = MDIconButton(icon = "3")
        self.button_4 = MDIconButton(icon = "4")
        self.button_5 = MDIconButton(icon = "5")
        self.button_6 = MDIconButton(icon = "6")
        self.button_7 = MDIconButton(icon = "7")
        self.button_8 = MDIconButton(icon = "8")
        self.button_9 = MDIconButton(icon = "9")
        self.button_0 = MDIconButton(icon = "0")
        self.button_ = MDIconButton(icon = "=")
        self.button_add = MDIconButton(icon="plus")
        self.button_sub = MDIconButton(icon = "-")
        self.button_mult = MDIconButton(icon = "*")
        self.button_div = MDIconButton(icon="/")
        self.button_clear = MDFlatButton(text = "Clear")

        self.buttons.add_widget(self.button_1)
        self.buttons.add_widget(self.button_2)
        self.buttons.add_widget(self.button_3)
        self.buttons.add_widget(self.button_4)
        self.buttons.add_widget(self.button_5)
        self.buttons.add_widget(self.button_6)
        self.buttons.add_widget(self.button_7)
        self.buttons.add_widget(self.button_8)
        self.buttons.add_widget(self.button_9)
        self.buttons.add_widget(self.button_0)
        self.buttons.add_widget(self.button_add)
        self.buttons.add_widget(self.button_sub)
        self.buttons.add_widget(self.button_mult)
        self.buttons.add_widget(self.button_div)
        self.buttons.add_widget(self.button_clear)

        self.calculator.add_widget(entry_field)
        self.calculator.add_widget(self.buttons)

        self.calculator_popup = Popup(title="Calculator", content=self.calculator)

        def activate_calculator(self, instance):
            self.calculator_popup.open()

        # END OF THE CALCULATOR LAYOUT

    # adding all widgets
        # adding minor widget to the tab card
        self.tab_layout.add_widget(self.home_button)
        self.tab_layout.add_widget(self.workspace_button)
        self.tab_layout.add_widget(self.cover_space_i)
        self.tab_layout.add_widget(self.email_button)
        self.tab_layout.add_widget(self.connect_button)
        self.tab_layout.add_widget(self.register_button)
        self.tab_card.add_widget(self.tab_layout)

        # adding just the home layout to the main card
        self.main_card.add_widget(self.home_layout)

        # adding minor widget to the tool card
        self.tool_layout.add_widget(self.calender)
        self.tool_layout.add_widget(self.time)
        self.tool_layout.add_widget(self.calculator)
        self.tool_layout.add_widget(self.location)
        self.tool_layout.add_widget(self.cover_space_ii)
        self.tool_layout.add_widget(self.settings)

        self.tool_card.add_widget(self.tool_layout)

        # adding three major cards to the handler
        self.handler.add_widget(self.tab_card)
        self.handler.add_widget(self.main_card)
        self.handler.add_widget(self.tool_card)
        self.add_widget(self.handler)

        # adding widget to the settings layout
        self.settings_layout = MDFloatLayout(line_color=(0, 0, 0.8, 1))
        self.check_work = MDLabel(text="Activate light theme",
                                  font_style = "H6",
                                  pos_hint = {'center_x': .6, 'center_y':.8})
        self.switch = Switch(pos_hint = {'center_x': .6, 'center_y':.8},
                             active = False)
        self.switch.bind(on_active=self.on_checkbox_active)
        self.settings_layout.add_widget(self.check_work)
        self.settings_layout.add_widget(self.switch)


    # functions for the layout for the card
    def home_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.home_layout)

    def workspace_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.work_layout)

    def meeting_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.email_layout)

    def connect_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.connect_layout)

    def profile_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.profile_layout)

    def activate_calendar(self, instance):
        self.date_dialog.bind(on_save=self.on_date_save)
        self.date_dialog.open()

    def on_date_save(self, instance, value, daterange):
        print(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def activate_timer(self, instance):
        self.time_dialog.bind(on_save=self.on_save)
        self.time_dialog.open()

    def on_save(self, instance, value):
        self.inform_save.open()
        print(value)

    def assurance(self, instance):
        self.inform_save.dismiss()

    def activate_settings(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.settings_layout)



    def on_checkbox_active(self, checkbox, value):
        if value:
            MyApp.change_theme(self, "Dark")
        else:
            pass



class Todo_app(MDScrollView):
    def __init__(self, **kwargs):
        super(Todo_app, self).__init__(**kwargs)
        self.overall = MDFloatLayout()
        self.content = MDGridLayout(rows= 1, spacing = 10, size_hint=(1, 1))
        self.create_task = MDIconButton(icon="plus", pos_hint={"center_x": 0.5, "y": 0},
                                        on_release=self.on_plus_button_click)
        self.overall.add_widget(self.content)
        self.overall.add_widget(self.create_task)
        self.add_widget(self.overall)
        self.delete_dialog = MDDialog(title="DELETE TASK", content="Are you sure you want to delete this task ?",
                                      size_hint=(.5, .5),
                                      buttons=[MDFlatButton(text="Cancel", on_press=lambda x: x.dismiss()),
                                               MDFlatButton(text="Delete",
                                                            on_press=lambda x: self.list.remove_widget())]
                                      )

        # popup widget
        self.popup_content = MDGridLayout(cols = 1)
        self.popup_input = MDTextField(hint_text="Enter your task")
        self.popup_selection_list = MDDropDownItem(items=["High Priority Task", "Medium Priority Task ", "Low Priority Task"],
                                                   position="bottom",
                                                   width_mult=6)
        button_container = MDGridLayout()
        button_container.add_widget(MDFlatButton(text="Create", on_press=self.popup.dismiss))
        button_container.add_widget(MDFlatButton(text="Cancel", on_press=self.popup.dismiss))

        self.popup_content.add_widget(self.popup_input)
        self.popup_content.add_widget(self.popup_selection_list)
        self.popup_content.add_widget(button_container)
        self.popup = Popup(title="SET TASK", content = self.popup_content)
        self.priority_level = str(self.popup_selection_list)
        self.task = str(self.popup_input)
        # END OF POPUP SECTION

        self.list = MDList()

    def add_new_widget(self):
        new_widget = TwoLineIconListItem(text=self.popup_input,
                                         secondary_text=self.priority_level,
                                         on_press = self.open_delete_dialog,
                                         icon="delete",
                                         )
        list.add_widget(new_widget)

    def open_delete_dialog(self, instance):
        self.delete_dialog.open()

    def save_task(self):
        contact_data = {
            "task": self.task,
            "priority": self.priority_level
        }
        try:
            with open("todo.json", "r") as file:
                    contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                # If the file doesn't exist or is not valid JSON, start with an empty list
                contacts = []

        contacts.append(contact_data)

        with open("todo.json", "w") as file:
           json.dump(contacts, file, indent=2)

    def on_plus_button_click(self, instance):
        self.popup.open()

    def save_popup(self, instance):
        self.add_new_widget()
        self.save_task()
        self.popup.dismiss()



class MyApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(Login(name="login"))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M2"
        return sm

    def change_theme(self, theme):
        self.theme_cls.theme_style = theme

    def change(self, next_page):
        MDApp.get_running_app().root.remove_widget(self)
        MDApp.get_running_app().root.add_widget(next_page)


MyApp().run()

# author: CEO1
