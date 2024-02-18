import pandas as pd

WELCOME_MSG: str = "\nWelcome to Protein Expression\n=============================="


class Main:
    MENU_MSG: str = "1.Activation Data\n2.Inhibition Data\n3.Save Changes\n4.Exit"

    SAVE_PATH: str = "./data/InputData.csv"
    ACT_INH_PATH: str = "./data/act_inh.csv"
    INPUT_DATA_PATH: str = "./data/InputData.csv"

    def __init__(self):
        self.act_inh: pd.DataFrame = None
        self.activation_data: pd.DataFrame = None
        self.input_data: pd.DataFrame = None
        self.inhibition_data: pd.DataFrame = None

    def read_files(self):
        self.act_inh = pd.read_csv(self.ACT_INH_PATH)
        self.act_inh = self.act_inh.drop(columns=["EFFECT", "MECHANISM"])

        self.activation_data = self.act_inh[self.act_inh['ACTIVATION'] == 1]
        self.inhibition_data = self.act_inh[self.act_inh['INHIBITION'] == 1]
        self.activation_data = self.activation_data.drop(columns=["ACTIVATION", "INHIBITION"])
        self.inhibition_data = self.inhibition_data.drop(columns=["ACTIVATION", "INHIBITION"])

        self.input_data = pd.read_csv(self.INPUT_DATA_PATH)

        if len(self.input_data.columns) == 1:
            self.input_data["ACTIVATION_POTENTIAL"] = [1.0 for _ in range(len(self.input_data))]
            self.input_data["INHIBITION_POTENTIAL"] = [1.0 for _ in range(len(self.input_data))]

    def inhibition_process(self, protein: str):
        products = self.inhibition_data[self.inhibition_data.iloc[:, 1] == protein].iloc[:, 0].values
        if len(products) == 0:
            print(f"Sorry, no records for {protein}")
            return
        sum = 0

        for product in products:
            print(f"Enter expression value of {product} (default = 1):", end=" ")
            exp_value = input()
            try:
                if exp_value == "":
                    exp_value = 1.0
                else:
                    exp_value = float(exp_value)
            except Exception:
                print("Please enter a numeric value")
                return
            sum += exp_value

        self.input_data.loc[self.input_data.iloc[:, 0] == protein, "INHIBITION_POTENTIAL"] = sum

    def activation_process(self, protein: str):
        products = self.activation_data[self.activation_data.iloc[:, 1] == protein].iloc[:, 0].values
        if len(products) == 0:
            print(f"Sorry, no records for {protein}")
            return
        sum = 0

        for product in products:
            print(f"Enter expression value of {product} (default = 1):", end=" ")
            exp_value = input()
            try:
                if exp_value == "":
                    exp_value = 1.0
                else:
                    exp_value = float(exp_value)
            except Exception:
                print("Please enter a numeric value")
                return
            sum += exp_value

        self.input_data.loc[self.input_data.iloc[:, 0] == protein, "ACTIVATION_POTENTIAL"] = sum

    def save_data(self):
        self.input_data.to_csv(self.SAVE_PATH, index=False)
        print(f"Data saved to {self.SAVE_PATH}")

    def get_choice(self):
        print("\nChoice: ", end=" ")
        choice = input()
        try:
            choice = int(choice)
        except Exception as e:
            print("Please enter a proper option")
            return

        if choice == 4:
            print("Bye.")
            exit(0)

        if choice == 3:
            self.save_data()
            return

        if choice != 1 and choice != 2:
            print("Not a valid option")
            return

        print("\nProtein: ", end=" ")
        protein = input()
        protein = protein.upper()

        if choice == 1:
            self.activation_process(protein)
        else:
            self.inhibition_process(protein)

    def menu(self):
        print(self.MENU_MSG)


def main():
    print(WELCOME_MSG)
    main = Main()
    main.read_files()
    main.menu()

    while True:
        main.get_choice()


if __name__ == '__main__':
    main()
