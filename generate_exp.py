import pandas as pd


class GenerateExpressionValue:
    WELCOME_MSG: str = ("This program generates a test expression value file. Here all proteins have an expression "
                        "value of 1")
    SAVE_PATH: str = "./data/expression_values.csv"
    PROTEIN_FILE_PATH: str = "./data/act_inh.csv"

    def generate(self) -> pd.DataFrame:
        df = pd.read_csv(self.PROTEIN_FILE_PATH)
        default_exp_values = [1 for _ in range(len(df))]
        exp_df = pd.DataFrame({"PROTEIN": df.loc[:, "ENTITYA"]})
        exp_df["EXPRESSION_VALUE"] = default_exp_values

        exp_df.to_csv(self.SAVE_PATH, index=False)

def main():
    genExpVal = GenerateExpressionValue()
    genExpVal.generate()


if __name__ == '__main__':
    main()
