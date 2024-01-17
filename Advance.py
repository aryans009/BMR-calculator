from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import AsyncImage

class BMIBMRCalorieApp(MDApp):

    def change_theme(self):
        # Change theme colors
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Orange"
        self.theme_cls.theme_style = "Light"

    def calculate_bmr(self, instance):
        try:
            weight = float(self.weight.text)
            height = float(self.height.text)
            age = float(self.age.text)

            if self.gender.text.lower() == "male":
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            elif self.gender.text.lower() == "female":
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            else:
                self.result.text = "Please enter valid gender (male/female)"
                return

            self.result.text = f"Your BMR is: {bmr:.2f} calories/day"
        except ValueError:
            self.result.text = "Please enter valid information"

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight.text)
            height = float(self.height.text) / 100  # Convert height to meters

            bmi = weight / (height * height)

            self.result.text = f"Your BMI is: {bmi:.2f}"
        except ValueError:
            self.result.text = "Please enter valid information"

    def calculate_calories(self, instance):
        try:
            weight = float(self.weight.text)
            height = float(self.height.text)
            age = float(self.age.text)
            activity_level = float(self.activity_level.text)

            if self.gender.text.lower() == "male":
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            elif self.gender.text.lower() == "female":
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            else:
                self.result.text = "Please enter valid gender (male/female)"
                return

            calories = bmr * activity_level

            self.result.text = f"Your daily calorie intake is: {calories:.2f} calories/day"
        except ValueError:
            self.result.text = "Please enter valid information"

    def build(self):
        self.change_theme()
        screen = MDScreen()

        background_image = AsyncImage(source='avacrdo.png')

        layout = MDBoxLayout(orientation="vertical", padding="20dp", spacing="20dp")

        top_label = MDLabel(text="BMR, BMI & Calories Calculator", halign="center",
                            theme_text_color="Custom",
                            text_color=(0, 0.5, 0),
                            font_style="H5")
        layout.add_widget(top_label)

        self.weight = MDTextFieldRect(hint_text="Enter weight (in kg)")
        self.height = MDTextFieldRect(hint_text="Enter height (in cm)")
        self.age = MDTextFieldRect(hint_text="Enter age")
        self.gender = MDTextFieldRect(hint_text="Enter gender (male/female)")
        self.activity_level = MDTextFieldRect(hint_text="Enter activity level (1.2-1.9)")
        self.result = MDLabel(halign="center", theme_text_color="Primary", font_style="H6")

        calculate_bmr_button = MDRaisedButton(text="Calculate BMR", on_release=self.calculate_bmr)
        calculate_bmi_button = MDRaisedButton(text="Calculate BMI", on_release=self.calculate_bmi)
        calculate_calories_button = MDRaisedButton(text="Calculate Calories", on_release=self.calculate_calories)

        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(self.age)
        layout.add_widget(self.gender)
        layout.add_widget(self.activity_level)
        layout.add_widget(self.result)
        layout.add_widget(calculate_bmr_button)
        layout.add_widget(calculate_bmi_button)
        layout.add_widget(calculate_calories_button)

        screen.add_widget(background_image)

        screen.add_widget(layout)

        return screen

if __name__ == "__main__":
    BMIBMRCalorieApp().run()
