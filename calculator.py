import pandas as pd
from units.df_func import calculate_wqi_for_row
import argparse

def process_wqi(input_file, output_file):
    """
    Calculate WQI for the input file and save the results to the output file.

    Parameters:
    input_file (str): The path to the input file (csv or excel).
    output_file (str): The path to the output file (csv or excel).
    """

    try:
        if input_file.endswith('.csv'):
            df = pd.read_csv(input_file)
        elif input_file.endswith('.xlsx') or input_file.endswith('.xls'):
            df = pd.read_excel(input_file)
        else:
            raise ValueError("Định dạng file không được hỗ trợ. Chỉ hỗ trợ .csv, .xlsx, .xls.")

        df['wqi'] = df.apply(calculate_wqi_for_row, axis=1)

        if output_file.endswith('.csv'):
            df.to_csv(output_file, index=False, encoding='utf-8')
        elif output_file.endswith('.xlsx'):
            df.to_excel(output_file, index=False)
        else:
            raise ValueError("Định dạng file đầu ra không được hỗ trợ. Chỉ hỗ trợ .csv, .xlsx.")

        print(f"Tính toán WQI thành công. Kết quả đã được lưu vào {output_file}")

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tính toán WQI từ file đầu vào và xuất ra file đầu ra.")
    parser.add_argument("input_file", help="Tên file đầu vào (csv hoặc excel)")
    parser.add_argument("output_file", help="Tên file đầu ra (csv hoặc excel)")

    args = parser.parse_args()

    process_wqi(args.input_file, args.output_file)