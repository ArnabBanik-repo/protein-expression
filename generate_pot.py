import pandas as pd


class GeneratePotential:
    INPUT_DATA_PATH: str = "./data/InputData.csv"
    ACT_INH_PATH: str = "./data/act_inh.csv"
    SAVE_PATH: str = "./data/InputData_generated_potential.csv"

    def __init__(self):
        try:
            self.input_df = pd.read_csv(self.INPUT_DATA_PATH)
            self.act_inh_df = pd.read_csv(self.ACT_INH_PATH)
        except Exception as e:
            print(e)

    def preprocess(self):
        self.act_inh_df = self.act_inh_df[["ENTITYA", "ENTITYB", "ACTIVATION", "INHIBITION"]]

        if len(self.input_df.columns) == 1:
            self.input_df["ACTIVATION_POTENTIAL"] = [0 for _ in range(len(self.input_df))]
            self.input_df["INHIBITION_POTENTIAL"] = [0 for _ in range(len(self.input_df))]

    def get_activation_potential(self, protein: str):
        products = self.act_inh_df[(self.act_inh_df.iloc[:, 1] == protein) & (self.act_inh_df.iloc[:, 2] == 1)].iloc[:,
                   0].values
        if len(products) == 0:
            return 0

        s = 0
        for _ in products:
            s += 1

        return s

    def get_inhibition_potential(self, protein: str):
        products = self.act_inh_df[(self.act_inh_df.iloc[:, 1] == protein) & (self.act_inh_df.iloc[:, 3] == 1)].iloc[:,
                   0].values
        if len(products) == 0:
            return 0

        s = 0
        for _ in products:
            s += 1

        return s

    def generate_potential(self):
        for ri, i in self.input_df.iterrows():
            for j in i:
                act_pot = self.get_activation_potential(j)
                inh_pot = self.get_inhibition_potential(j)

                self.input_df.loc[self.input_df.iloc[:, 0] == j, "ACTIVATION_POTENTIAL"] = act_pot
                self.input_df.loc[self.input_df.iloc[:, 0] == j, "INHIBITION_POTENTIAL"] = inh_pot

            if (ri + 1) % 10000 == 0:
                print(ri + 1)


def main():
    gp = GeneratePotential()
    gp.preprocess()
    gp.generate_potential()
    gp.input_df.to_csv(gp.SAVE_PATH, index=False)

    print(f"Generated the file in {gp.SAVE_PATH}")

if __name__ == '__main__':
    main()
